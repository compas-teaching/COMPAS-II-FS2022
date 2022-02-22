import os
import random

import compas
from compas.datastructures import Network

network = Network.from_obj(compas.get('grid_irregular.obj'))

for node in network.nodes():
    network.node_attribute(node, 'weight', random.choice(range(20)))

print(network.summary())

# Serialize network to JSON and back
filename = os.path.join(os.path.dirname(__file__), '..', 'data', '033_network_serialization.json')

network.to_json(filename, pretty=True)
print(network.summary())
print(f'Saved to {filename}')

network2 = Network.from_json(filename)
print(network2.summary())
