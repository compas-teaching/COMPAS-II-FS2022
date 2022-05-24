from cmath import sqrt
import time
import os
import logging

import compas_slicer.utilities as utils
from compas_slicer.pre_processing import move_mesh_to_point
from compas_slicer.slicers import PlanarSlicer
from compas_slicer.post_processing import generate_brim
from compas_slicer.post_processing import generate_raft
from compas_slicer.post_processing import simplify_paths_rdp
from compas_slicer.post_processing import seams_smooth
from compas_slicer.print_organization import PlanarPrintOrganizer
from compas_slicer.print_organization import set_extruder_toggle
from compas_slicer.print_organization import add_safety_printpoints
from compas_slicer.print_organization import set_linear_velocity_constant
from compas_slicer.print_organization import set_blend_radius
from compas_slicer.utilities import save_to_json
from compas_slicer.utilities.utils import get_normal_of_path_on_xy_plane
from compas.geometry import Point
from compas.geometry import scale_vector, add_vectors
from compas_slicer.geometry import Path

from compas.datastructures import Mesh
from compas.geometry import Point

# ==============================================================================
# Logging
# ==============================================================================
logger = logging.getLogger('logger')
logging.basicConfig(format='%(levelname)s-%(message)s', level=logging.INFO)

# ==============================================================================
# Select location of data folder and specify model to slice
# ==============================================================================
DATA = os.path.join(os.path.dirname(__file__), 'data')
OUTPUT_DIR = utils.get_output_directory(DATA)  # creates 'output' folder if it doesn't already exist
MODEL = 'simple_vase_open_low_res_3.obj'

def create_overhang_texture(slicer, overhang_distance):
    """Creates a cool overhang texture"""

    print("Creating cool texture")

    for i, layer in enumerate(slicer.layers):
        if i > (len(slicer.layers)/3) :
            # for every layer on the top 2/3
            # print(layer)
            for j, path in enumerate(layer.paths):
                # print(path)
                # create an empty layer in which we can store our modified points
                new_path = []
                for k, pt in enumerate(path.points):
                    # for every fourth point (only even points)
                    if k % i == 0 or k % i == 10:
                        # get the normal of the point in relation to the mesh
                        normal = get_normal_of_path_on_xy_plane(k, pt, path, mesh=None)
                        # scale the vector by a number to move the point
                        normal_scaled = scale_vector(normal, -overhang_distance*((i/len(slicer.layers))**2))
                        # create a new point by adding the point and the normal vector
                        new_pt = add_vectors(pt, normal_scaled)
                        # recreate the new_pt values as compas_points
                        pt = Point(new_pt[0], new_pt[1], new_pt[2])

                    # append the points to the new path
                    new_path.append(pt)

                # replace the current path with the new path that we just created
                layer.paths[j] = Path(new_path, is_closed=path.is_closed)

def main():
    start_time = time.time()

    # ==========================================================================
    # Load mesh
    # ==========================================================================
    compas_mesh = Mesh.from_obj(os.path.join(DATA, MODEL))

    # ==========================================================================
    # Move to origin
    # ==========================================================================
    move_mesh_to_point(compas_mesh, Point(0, 0, 0))

    # ==========================================================================
    # Slicing
    # options: 'default': Both for open and closed paths. But slow
    #          'cgal':    Very fast. Only for closed paths.
    #                     Requires additional installation (compas_cgal).
    # ==========================================================================
    slicer = PlanarSlicer(compas_mesh, slicer_type="cgal", layer_height=3)
    slicer.slice_model()

    # ==========================================================================
    # Generate brim / raft
    # ==========================================================================
    # NOTE: Typically you would want to use either a brim OR a raft,
    # however, in this example both are used to explain the functionality
    # generate_brim(slicer, layer_width=3.0, number_of_brim_offsets=4)
    # generate_raft(slicer,
    #               raft_offset=20,
    #               distance_between_paths=5,
    #               direction="xy_diagonal",
    #               raft_layers=1)

    # ==========================================================================
    # Simplify the paths by removing points with a certain threshold
    # change the threshold value to remove more or less points
    # ==========================================================================
    simplify_paths_rdp(slicer, threshold=0.3)

    ############################################################################
    # INSERT OWN TEXTURE HERE - growing anomalies
    ############################################################################
    create_overhang_texture(slicer, overhang_distance=25)

    # ==========================================================================
    # Smooth the seams between layers
    # change the smooth_distance value to achieve smoother, or more abrupt seams
    # ==========================================================================
    seams_smooth(slicer, smooth_distance=7)

    # ==========================================================================
    # Prints out the info of the slicer
    # ==========================================================================
    slicer.printout_info()

    # ==========================================================================
    # Save slicer data to JSON
    # ==========================================================================
    save_to_json(slicer.to_data(), OUTPUT_DIR, 'slicer_data.json')

    # ==========================================================================
    # Initializes the PlanarPrintOrganizer and creates PrintPoints
    # ==========================================================================
    print_organizer = PlanarPrintOrganizer(slicer)
    print_organizer.create_printpoints()

    # ==========================================================================
    # Set fabrication-related parameters
    # ==========================================================================
    # set_extruder_toggle(print_organizer, slicer)
    # add_safety_printpoints(print_organizer, z_hop=10.0)
    # set_linear_velocity_constant(print_organizer, v=100.0)
    # set_blend_radius(print_organizer, d_fillet=10.0)

    # ==========================================================================
    # Prints out the info of the PrintOrganizer
    # ==========================================================================
    print_organizer.printout_info()

    # ==========================================================================
    # Converts the PrintPoints to data and saves to JSON
    # =========================================================================
    printpoints_data = print_organizer.output_printpoints_dict()
    utils.save_to_json(printpoints_data, OUTPUT_DIR, 'out_printpoints.json')

    end_time = time.time()
    print("Total elapsed time", round(end_time - start_time, 2), "seconds")


if __name__ == "__main__":
    main()
