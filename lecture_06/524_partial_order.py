from compas.datastructures import Network
from compas_plotters import Plotter

n = Network()

n.add_edge(1, 2)
n.add_edge(1, 3)
n.add_edge(1, 5)
n.add_edge(1, 7)

n.add_edge(2, 4)
n.add_edge(2, 6)
n.add_edge(2, 10)

n.add_edge(3, 6)
n.add_edge(3, 9)

n.add_edge(4, 8)

n.add_edge(5, 10)

print(n.summary())

visited = set()


def layout(node, y=1):
    if node in visited:
        return
    visited.add(node)

    nodes_in_row = list(n.nodes_where({"y": y}))
    n.node_attributes(node, "xyz", [len(nodes_in_row), y, 0])

    for nb in n.neighbors_out(node):
        layout(nb, y + 1)


root = 1
layout(root)

plotter = Plotter(figsize=(12, 7.5))
artist = plotter.add(n)
artist.node_size = 2

# Workaround until this is merged: https://github.com/compas-dev/compas/pull/1029
artist._nodecollection.remove()
artist._edgecollection.remove()
artist._nodecollection = None
artist._edgecollection = None

artist.draw()
artist.draw_nodelabels(dict(zip(n.nodes(), n.nodes())))

plotter.zoom_extents()
plotter.show()
