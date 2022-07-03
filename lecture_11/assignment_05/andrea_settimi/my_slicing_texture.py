from compas_slicer.geometry import Path
from compas_slicer.utilities.utils import get_normal_of_path_on_xy_plane
from compas.geometry import Point
from compas.geometry import scale_vector, add_vectors

def create_overhang_texture(slicer, overhang_distance):
    for i,layer in enumerate(slicer.layers):
        if (i%2==0):
            for j,path in enumerate(layer.paths):
                new_path =[]
                for k,point in enumerate(path.points):
                    if (k%2 ==0) and (k%6==0):
                        normal = get_normal_of_path_on_xy_plane(k , point, path , mesh =None)
                        normal_scaled = scale_vector(normal, -1.5*overhang_distance)
                        new_pt = add_vectors(point, normal_scaled)
                        new_path.append(Point(new_pt[0], new_pt[1], new_pt[2]))
                    if (k%3 ==0) :
                        normal = get_normal_of_path_on_xy_plane(k , point, path , mesh =None)
                        normal_scaled = scale_vector(normal, 1*overhang_distance)
                        new_pt2 = add_vectors(point, normal_scaled)
                        new_path.append(Point(new_pt2[0], new_pt2[1], new_pt2[2]))
                    else:
                        new_path.append(point)
            layer.paths[j]= Path(new_path, is_closed= path.is_closed)