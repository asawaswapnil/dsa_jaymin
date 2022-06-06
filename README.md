# Data Structures & Algorithms

Simple Python implementations of commonly used data structures and algorithms

## Setup

- Python 3.x
- `pip install -r requirements.txt` (only required for visualizing graphs)

## Quick Links

- [Graph](graph)
  - [Utility Methods](graph/__init__.py)
    - Print a readable representation of the graph in console (`print_graph`)
    - Create an image representing the graph structure (`visualize_graph`)
  - [Sample Graphs](graph/__init__.py)
    - Sample graphs (adjacency list representation) for all permutations under {directed, undirected, cyclic, acyclic, connected, disconnected} (`SampleGraphs`)
  - [Traversals](graph/traversals.py)
    - Recursive depth-first search (`dfs_recursive`)
    - Iterative depth-first search (`dfs_iterative`)
    - Iterative breadth-first search (`bfs_iterative`)
  - [Paths](graph/paths.py)
    - Find paths in a graph using iterative depth-first search (`dfs_paths`)
    - Find paths in a graph using iterative breadth-first search (`bfs_paths`)
  - [Cycles](graph/cycles.py)
    - Find cycles in an undirected graph using information on number of edges and nodes (`find_cycles_undirected_using_edge_count`)
    - Find cycles in an undirected graph using union-find data structure (`find_cycles_undirected_union_find`)
    - Find cycles in an undirected graph using recursive depth-first search (`find_cycles_undirected_dfs`)
    - Find cycles in a directed graph using recursive depth-first search (`find_cycles_directed_dfs`)
  - [Connected Components](graph/connected_components.py)
    - Find number of connected components in a graph using depth-first search (`conn_comps_using_dfs`)
    - Find number of connected components in a graph using breadth-first search (`conn_comps_using_bfs`)
    - Find number of connected components in an undirected graph using union-find data structure (`conn_comps_using_dfs`)
  - [Topological Sorting](graph/topological_sorting.py)
    - Find topological sorting of a graph using depth-first search and visit markers (same as DFS coloring method from CLRS) (`top_sort_dfs`)
    - Find topological sorting of a graph using breadth-first search and node indegrees (Kahn's algorithm) (`top_sort_bfs`)
  - [Graph Valid Tree](graph/valid_tree.py)
    - Check if an undirected graph is a valid tree using information on number of edges and nodes (`graph_valid_tree_undirected_using_num_edges`)
    - Check if an undirected graph is a valid tree using depth-first search (`graph_valid_tree_undirected_using_dfs`)
    - Check if a directed graph is a valid tree using depth-first search (`graph_valid_tree_directed_using_dfs`)
- [Union-Find](unionfind/__init__.py)
  - Implementation of the data structure with union-by-rank and union-by-size (`DisjointSetUnion`)
- [Tree](tree)
