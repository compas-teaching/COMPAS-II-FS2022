import os
import random

import compas
from compas.datastructures import Datastructure
from compas.datastructures import Network


class Weight(Datastructure):
    def __init__(self, value=None):
        self.value = value

    @property
    def data(self):
        return {'value': self.value}

    @data.setter
    def data(self, data):
        self.value = data['value']


network = Network.from_obj(compas.get('grid_irregular.obj'))

for node in network.nodes():
    network.node_attribute(node, 'weight', Weight(random.choice(range(20))))

print(network.summary())

# Serialize network to JSON and back
filename = os.path.join(os.path.dirname(__file__), '..', 'data', '034_network_serialization_complex_type.json')

network.to_json(filename, pretty=True)
print(network.summary())
print(f'Saved to {filename}')

network2 = Network.from_json(filename)
print(network2.summary())
