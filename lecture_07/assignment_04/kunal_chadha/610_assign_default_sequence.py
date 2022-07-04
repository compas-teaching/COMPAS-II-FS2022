import os

import compas
from compas.utilities import pairwise

HERE = os.path.dirname(__file__)

# Load assembly
filename = os.path.join(HERE, '601_assembly_design.json')
assembly = compas.json_load(filename)

# Reset assembly connectivity
assembly.graph.edge = {i: {} for i in assembly.graph.nodes()}
assembly.graph.adjacency = {i: {} for i in assembly.graph.nodes()}

# Define connectivity as a linear sequence dependant on implementation details (NOT a good idea!)
linear_sequence = list(assembly.parts())
for a, b in pairwise(linear_sequence):
    assembly.add_connection(a, b)

print([part.key for part in linear_sequence])

# Save assembly
filename = os.path.join(HERE, '602_assembly_sequenced.json')
compas.json_dump(assembly, filename)
