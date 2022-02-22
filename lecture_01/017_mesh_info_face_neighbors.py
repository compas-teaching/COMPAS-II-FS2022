import compas
from compas.datastructures import Mesh
from compas_plotters import Plotter

mesh = Mesh.from_obj(compas.get('faces.obj'))

face = mesh.get_any_face()
nbrs = mesh.face_neighbors(face)

facecolor = {}
facecolor[face] = (1, .8, .8)
for nbr in nbrs:
    facecolor[nbr] = (.8, 1, .8)

plotter = Plotter(figsize=(12, 7.5))

meshartist = plotter.add(mesh)
meshartist.draw_vertices()
meshartist.draw_faces(color=facecolor)
meshartist.draw_facelabels(text={face: str(mesh.face_degree(face)) for face in mesh.faces()})

plotter.zoom_extents()
plotter.show()
