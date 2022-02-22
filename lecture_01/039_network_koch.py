import math

from compas.artists import Artist
from compas.datastructures import Network
from compas.geometry import Point
from compas.geometry import Rotation
from compas.geometry import Vector

lsys = "A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A-A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A-A-A++A-A-A-A++A-A++A-A++A-A-A-A++A"

network = Network()
step = 1.
pt = Point(0, 0, 0)
v = Vector(1, 0, 0)


def draw(network, point, vector, s, step, last_node=None):
    for c in s:
        if c == 'A':
            point = point + vector * step
            a = network.add_node(x=point.x, y=point.y, z=point.z)
            if last_node != None:
                network.add_edge(last_node, a)
            last_node = a
        elif c == '-':
            R = Rotation.from_axis_and_angle((0, 0, 1), math.radians(60))
            vector.transform(R)
        elif c == '+':
            R = Rotation.from_axis_and_angle((0, 0, 1), math.radians(-60))
            vector.transform(R)


draw(network, pt, v, lsys, step)

artist = Artist(network, layer='network')
artist.clear_layer()
artist.draw_nodes()
artist.draw_edges()
