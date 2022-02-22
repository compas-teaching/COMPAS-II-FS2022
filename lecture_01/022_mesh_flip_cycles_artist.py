import compas
from compas.datastructures import Mesh
from compas.artists import Artist

mesh = Mesh.from_obj(compas.get('tubemesh.obj'))
mesh.flip_cycles()

artist = Artist(mesh, layer='Tubemesh')
artist.clear_layer()
artist.draw()
artist.draw_vertexnormals()
