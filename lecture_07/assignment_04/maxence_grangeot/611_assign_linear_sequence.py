import os

import compas
from compas.utilities import pairwise

HERE = os.path.dirname(__file__)

# Load assembly
filename = os.path.join(HERE, '601_assembly_design.json')
assembly = compas.json_load(filename)

# Define connectivity as a linear sequence of integers
linear_sequence = sorted(assembly.parts(), key=lambda p: int(p.key))
for a, b in pairwise(linear_sequence):
    assembly.add_connection(a, b)

print([part.key for part in linear_sequence])

# Save assembly
filename = os.path.join(HERE, '602_assembly_sequenced.json')
compas.json_dump(assembly, filename, pretty=True)
