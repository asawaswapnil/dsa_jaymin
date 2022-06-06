import random
from collections import deque
from typing import Dict, Set

from graph import SampleGraphs, print_graph


def dfs_recursive(graph: Dict[str, Set], node: str, visited: Set) -> Set:
    """
    Recursive DFS
    Works for all types of graphs {directed, undirected, cyclic, acyclic, connected, disconnected}
    """
    visited.add(node)
    for nbr in graph[node] - visited:
        dfs_recursive(graph, nbr, visited)
    return visited


def dfs_iterative(graph: Dict[str, Set], start_node: str) -> Set:
    """
    Iterative DFS
    Works for all types of graphs {directed, undirected, cyclic, acyclic, connected, disconnected}
    """
    visited = set()
    stack = [start_node]
    while stack:
        node = stack.pop()
        visited.add(node)
        stack.extend(graph[node] - visited)
    return visited


def bfs_iterative(graph: Dict[str, Set], start_node: str) -> Set:
    """
    Iterative BFS
    Works for all types of graphs {directed, undirected, cyclic, acyclic, connected, disconnected}
    """
    visited = set()
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        visited.add(node)
        queue.extend(graph[node] - visited)
    return visited


if __name__ == '__main__':
    graph = SampleGraphs.undirected_cyclic_conn_graph().graph
    nodes = list(graph.keys())
    start_node = random.choice(nodes)

    print_graph(graph, message="\nGraph")
    print("\nStart Node")
    print(start_node)

    print("\n=> Depth-first Search Recursive")
    print(dfs_recursive(graph=graph, node=start_node, visited=set()))

    print("\n=> Depth-first Search Iterative")
    print(dfs_iterative(graph=graph, start_node=start_node))

    print("\n=> Breadth-first Search Iterative")
    print(bfs_iterative(graph=graph, start_node=start_node))

