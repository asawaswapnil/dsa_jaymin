# Data Structures & Algorithms

Python implementations and examples of commonly used data structures and algorithms

## Setup

- Python 3.7+
- `pip install -r requirements.txt` (only required for visualizing graphs)

## Quick Links

- [Graph](graph)
  - [Utility Methods](graph/__init__.py)
    - Print a readable representation of the graph in console (`print_graph`)
    - Create an image representing the graph structure (`visualize_graph`)
  - [Sample Graphs](graph/__init__.py)
    - Sample graphs (adjacency list representation) for all permutations under {directed, undirected, cyclic, acyclic, connected, disconnected} (`SampleGraphs`)
  - [Traversals](graph/traversals.py)
    - Recursive and iterative depth-first search
    - Iterative breadth-first search
  - [Paths](graph/paths.py)
    - Find paths in a graph using iterative depth-first search and breadth-first search
  - [Cycles](graph/cycles.py)
    - Find cycles in an undirected graph using.. 
      - .. information on number of edges and nodes
      - .. the union-find data structure
      - .. recursive depth-first search
    - Find cycles in a directed graph using recursive depth-first search
  - [Connected Components](graph/connected_components.py)
    - Find number of connected components in a graph using depth-first search and breadth-first search
    - Find number of connected components in an undirected graph using the union-find data structure
  - [Topological Sorting](graph/topological_sorting.py)
    - Find topological sorting of a graph using.. 
      - .. depth-first search and visit markers (same as DFS coloring method from CLRS)
      - .. breadth-first search and node indegrees (Kahn's algorithm)
  - [Graph Valid Tree](graph/valid_tree.py)
    - Check if an undirected graph is a valid tree using.. 
      - .. information on number of edges and nodes
      - .. depth-first search
    - Check if a directed graph is a valid tree using depth-first search
- [Union-Find](unionfind/__init__.py)
  - Implementation of the Disjoint Set Union data structure with union-by-rank and union-by-size
- [Trees](tree)
  - [Utility Methods](tree/__init__.py)
  - [Sample Trees](tree/__init__.py)
    - Sample trees used for examples with their visual structure (`SampleTrees`)
  - [Traversals](tree/traversals.py)
    - Depth-first: recursive and iterative inorder, preorder and postorder traversals
    - Breadth-first: iterative levelorder and levelorder grouped traversals
  - [Trie](tree/trie.py)
    - A basic implementation of Trie (Prefix Tree) using a Hashmap
  - [ParseTree](tree/parse_tree.py)
    - An implementation of a Parse Tree to evaluate simple mathematical expressions
- [Linear DSA](linear)
  - [Sorting](linear/sorting)
    - [Merge Sort](linear/sorting/merge_sort.py)
    - [Quick Sort](linear/sorting/quick_sort.py)
    - [Counting Sort](linear/sorting/counting_sort.py)
    - [Radix Sort](linear/sorting/radix_sort.py)
  - [Selection](linear/selection)
    - [Quick Select](linear/selection/quick_select.py)
  - [Binary Search](linear/binary_search)
    - A generalized Binary Search [template](linear/binary_search/README.md) and it's applications
  - [Ring Buffer](linear/ring_buffer)
    - [Basic](linear/ring_buffer/ring_buffer_basic.py) (illustrative) and [optimized](linear/ring_buffer/ring_buffer_optimized.py) implementations of ring buffer (also called circular buffer or circular queue)
- [Dynamic Programming](dp)
  - Python implementations of problems from [Coderbyte DP series](https://www.youtube.com/watch?v=oBt53YbR9Kk)
  - [Memoization](dp/memoization)
  - [Tabulation](dp/tabulation)
- [Miscellaneous](misc)
  - [ID Allocator](misc/id_allocator)
    - An efficient version of an ID allocator using a Binary Heap
  - [Hit Counter](misc/hit_counter)
    - An implementation of a hit counter that keeps track of number of requests for different methods of a key-value store
    in past `n` seconds.
