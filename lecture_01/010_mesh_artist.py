import compas
from compas.artists import Artist
from compas.datastructures import Mesh

mesh = Mesh.from_obj(compas.get('hypar.obj'))

artist = Artist(mesh)
a = artist.draw()
