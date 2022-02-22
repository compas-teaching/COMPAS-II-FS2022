import random

from compas.datastructures import Mesh
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=10, nx=10)

edge = random.choice(list(mesh.edges()))
strip = mesh.edge_strip(edge)

vertex_color = {
    strip[0][0]: (1.0, 0.7, 0.7),
    strip[0][1]: (1.0, 0.0, 0.0),
}

edge_width = {}
for u, v in strip:
    edge_width[u, v] = 5.0

meshartist = plotter.add(mesh, sizepolicy='relative', edgewidth=edge_width, vertexcolor=vertex_color, vertexsize=10)

plotter.zoom_extents()
plotter.show()
