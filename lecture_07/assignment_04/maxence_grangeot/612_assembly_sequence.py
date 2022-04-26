import os

import compas
from compas.topology import breadth_first_ordering

HERE = os.path.dirname(__file__)

# Load assembly
filename = os.path.join(HERE, '602_assembly_sequenced.json')
assembly = compas.json_load(filename)

sequence = breadth_first_ordering(assembly.graph.adjacency, "0")
print(sequence)
