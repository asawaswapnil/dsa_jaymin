# Data Structures & Algorithms

Python implementations and examples of commonly used data structures and algorithms

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
    - Recursive depth-first search
    - Iterative depth-first search
    - Iterative breadth-first search
    - Iterative breadth-first search optimized
  - [Paths](graph/paths.py)
    - Find paths in a graph using iterative depth-first search
    - Find paths in a graph using iterative breadth-first search
    - Find paths in a graph using optimized iterative breadth-first search
  - [Cycles](graph/cycles.py)
    - Find cycles in an undirected graph using information on number of edges and nodes
    - Find cycles in an undirected graph using union-find data structure
    - Find cycles in an undirected graph using recursive depth-first search
    - Find cycles in a directed graph using recursive depth-first search
  - [Connected Components](graph/connected_components.py)
    - Find number of connected components in a graph using depth-first search
    - Find number of connected components in a graph using breadth-first search
    - Find number of connected components in an undirected graph using union-find data structure
  - [Topological Sorting](graph/topological_sorting.py)
    - Find topological sorting of a graph using depth-first search and visit markers (same as DFS coloring method from CLRS)
    - Find topological sorting of a graph using breadth-first search and node indegrees (Kahn's algorithm)
  - [Graph Valid Tree](graph/valid_tree.py)
    - Check if an undirected graph is a valid tree using information on number of edges and nodes
    - Check if an undirected graph is a valid tree using depth-first search
    - Check if a directed graph is a valid tree using depth-first search
- [Union-Find](unionfind/__init__.py)
  - Implementation of the data structure with union-by-rank and union-by-size
- [Trees](tree)
- [Linear Data Structures](linear)
  - [Ring Buffer](linear/ring_buffer)
    - [Basic](linear/ring_buffer/ring_buffer_basic.py) (illustrative) and [optimized](linear/ring_buffer/ring_buffer_optimized.py) implementations of ring buffer (also called circular buffer or circular queue)
- [Dynamic Programming](dp)
  - Python implementations of problems from [Coderbyte DP series](https://www.youtube.com/watch?v=oBt53YbR9Kk)
  - [Memoization](dp/memoization)
  - [Tabulation](dp/tabulation)
