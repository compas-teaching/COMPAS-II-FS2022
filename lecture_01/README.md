# COMPAS II: Introduction

Introduction to digital fabrication methods and the COMPAS ecosystem for digital fabrication: `core`, `fab`, `rrc`, `slicer`.
Brief overview of core data structures (network, mesh).
Remote procedure calls.

👉 [Slides](lecture_01.pdf)

## Examples

* Primitives
  * [Primitives](001_primitives.py)
  * [Operations](002_primitives_operations.py)
  * [Constructors](003_primitives_constructors.py)
  * [Equivalences to built-ins](004_primitives_equivalence.py)
  * [Transforms](005_primitives_transforms.py)
* Shapes
  * [Shapes](006_shapes.py)
  * [Shapes Artists](007_shapes_artist.py)
* Mesh datastructure
  * [Mesh Artist](010_mesh_artist.py)
  * [Mesh from scratch](013_mesh_from_scratch.py)
  * [Mesh stand-alone viewer](014_mesh_plotter.py)
  * [Queries: vertex degree](015_mesh_info_vertex_degree.py)
  * [Queries: vertices on boundary](016_mesh_info_vertices_on_boundary.py)
  * [Queries: face neighbors](017_mesh_info_face_neighbors.py)
  * [Queries: vertex neighbors](018_mesh_info_vertex_neighbors.py)
  * [Queries: edge strip](019_mesh_info_edge_strip.py)
  * [Queries: edge loop](020_mesh_info_edge_loop.py)
  * [Vertex normals: visualization](021_mesh_vertex_normals_artist.py)
  * [Flip cycles: visualization](022_mesh_flip_cycles_artist.py)
  * [Mesh queries: visualization](023_mesh_info_artist.py)
  * [Boolean operations with CGAL](024_mesh_booleans.py)
  * [Boolean operations: visualization](025_mesh_booleans_artist.py)

* Network datastructure
  * [Network from scratch](030_network_from_scratch.py)
  * [Network Artist](031_network_from_scratch_artist.py)
  * [Network attributes](032_network_node_attr_artist.py)
  * [Queries: node neighbors](033_network_neighbors.py)
  * [Queries: shortest path](034_network_info_shortest_path.py)
  * [Serialization](035_network_serialization.py)
  * [Serialization of complex types](036_network_serialization_complex_type.py)
  * [Network Koch snowflake](039_network_koch.py)

* Remote Procedure calls
  * [Basic remote procedure call](040_rpc_basic_example.py)
