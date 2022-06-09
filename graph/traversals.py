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
    Iterative DFS - works for all types of graphs {directed, undirected, cyclic, acyclic, connected, disconnected}
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
    Iterative BFS - works for all types of graphs {directed, undirected, cyclic, acyclic, connected, disconnected}
    """
    visited = set()
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        visited.add(node)
        queue.extend(graph[node] - visited)
    return visited


def bfs_iterative_optimized(graph: Dict[str, Set], start_node: str) -> Set:
    """
    Iterative BFS optimized - works for all types of graphs {directed, undirected, cyclic, acyclic, connected, disconnected}
    1. Reduced memory consumption
    2. Fewer dequeue operations

    Ordinary BFS:
    - initial state
        - visited: {}, queue: [start]
    - while queue not empty
        - dequeue node
        - add node to visited set
        - for each neighbor that is not visited so far
            - enqueue neighbor

    Optimized BFS:
    - initial state
        - visited: {start}, queue: [start]
    - while queue not empty
        - dequeue node
        - for each neighbor that is not visited so far
            - add neighbor to visited set
            - enqueue neighbor

    Basically, visiting a neighbor first before enqueuing it makes sure there are fewer neighbors not visited next time
    which makes sure queue size increases slowly compared to ordinary BFS which means less memory usage and fewer dequeue
    operations on an average

    Very efficient for fully connected, dense graphs

    It is also very useful for problems where BFS is used to reach from point A to point B in minimum hops with multiple
    possible paths from point A to point B such that minimum nodes are visited
    Even ordinary BFS in general, will always find the shortest path from point A to point B, but with ordinary BFS, it's
    not guaranteed that the minimum possible number of nodes will be visited in the process
    """
    visited = {start_node}
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        for nbr in graph[node] - visited:
            visited.add(nbr)
            queue.append(nbr)
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

    print("\n=> Breadth-first Search Iterative Level order Optimized")
    print(bfs_iterative_optimized(graph=graph, start_node=start_node))
