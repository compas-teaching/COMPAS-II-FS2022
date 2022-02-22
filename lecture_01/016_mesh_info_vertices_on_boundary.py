import compas
from compas.datastructures import Mesh
from compas_plotters import Plotter

mesh = Mesh.from_obj(compas.get('faces.obj'))

plotter = Plotter(figsize=(12, 7.5))

meshartist = plotter.add(mesh)
meshartist.draw_vertices(
    color={vertex: (1, 0, 0) for vertex in mesh.vertices_on_boundary()},
)
meshartist.draw_faces()

plotter.zoom_extents()
plotter.show()
