import compas
from compas.datastructures import Mesh
from compas_plotters import Plotter

mesh = Mesh.from_obj(compas.get('faces.obj'))

plotter = Plotter()

meshartist = plotter.add(mesh)
meshartist.draw_vertices()
meshartist.draw_faces()

plotter.zoom_extents()
plotter.show()
