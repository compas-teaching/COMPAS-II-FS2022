import compas
from compas.datastructures import Mesh
from compas_plotters import Plotter

mesh = Mesh.from_obj(compas.get('faces.obj'))

vertex = mesh.get_any_vertex()
nbrs = mesh.vertex_neighbors(vertex)

vertexcolor = {}
vertexcolor[vertex] = (1, 0, 0)
edgecolor = {}
for nbr in nbrs:
    vertexcolor[nbr] = (0, 0, 1)
    edgecolor[vertex, nbr] = (0, 1, 0)
    edgecolor[nbr, vertex] = (0, 1, 0)

plotter = Plotter(figsize=(12, 7.5))

meshartist = plotter.add(mesh)
meshartist.edge_width = {edge: 2.0 for edge in edgecolor}
meshartist.draw_vertices(color=vertexcolor)
meshartist.draw_faces()
meshartist.draw_edges(color=edgecolor)

plotter.zoom_extents()
plotter.show()
