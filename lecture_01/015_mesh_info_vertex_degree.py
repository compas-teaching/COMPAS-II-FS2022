import compas
from compas.datastructures import Mesh
from compas_plotters import Plotter

mesh = Mesh.from_obj(compas.get('faces.obj'))

plotter = Plotter()

meshartist = plotter.add(mesh, sizepolicy='absolute', vertexsize=30)
meshartist.draw_vertices()
meshartist.draw_vertexlabels(text={vertex: str(mesh.vertex_degree(vertex)) for vertex in mesh.vertices()})
meshartist.draw_faces()

plotter.zoom_extents()
plotter.show()
