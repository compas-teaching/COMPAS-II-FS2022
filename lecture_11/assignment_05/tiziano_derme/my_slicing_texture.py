from compas_slicer.geometry import Path
from compas_slicer.utilities.utils import get_normal_of_path_on_xy_plane
from compas.geometry import Point
from compas.geometry import scale_vector, add_vectors

def create_overhang_texture(slicer, overhang_distance):
    for i, layer in enumerate(slicer.layers):
        if i % 2 == 0 and i > 0:
            # for every 2nd layer except the first one
            #print(layer)
            for j, path in enumerate(layer.paths):
                #print(path)
                #create an empty layer to store the all the modified points
                new_path = []
                for k, point in enumerate(path.points):
                    # iterate for every second point
                    if k % 2 == 0:
                        #get normal in reference to the mesh
                        normal = get_normal_of_path_on_xy_plane(k, point, path, mesh=None)
                        # scale the vector by a number to move the point 
                        normal_scaled = scale_vector(normal, -overhang_distance)
                        # create a mew point by adding the point an the normal vector
                        new_pt = add_vectors(point, normal_scaled)
                        #re create the new_pt valuies as compas_points
                        new_path.append(Point(new_pt[0], new_pt[1], new_pt[2]))
                    else:
                        new_path.append(point)
            #replace to current path with the new find 
            layer.paths[j] = Path(new_path, is_closed = path.is_closed)