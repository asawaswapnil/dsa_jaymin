import copy
from collections import deque
from typing import Dict, Set, List, Optional

from graph import SampleGraphs, CycleFoundError, print_graph


def top_sort_dfs(graph: Dict[str, Set]) -> Optional[List]:
    """
    Using DFS and visit tracking markers/flags
    0 => node not visited
    1 => node is currently being visited (traversing through the neighbors)
    2 => node visited
    Topological sorting can only be found for directed acyclic graphs
    """
    def _top_sort(graph, node, markers, top_stack):
        markers[node] = 1
        for nbr in graph[node]:
            if markers[nbr] == 1:
                raise CycleFoundError("Graph is cyclic, topological sort not possible!")
            if markers[nbr] == 0:
                _top_sort(graph, nbr, markers, top_stack)
        markers[node] = 2
        top_stack.append(node)

    markers = dict.fromkeys(graph, 0)
    top_stack = []
    for node in graph.keys():
        if markers[node] == 0:
            try:
                _top_sort(graph, node, markers, top_stack)
            except CycleFoundError as ce:
                print(ce)
                return None
    return list(reversed(top_stack))


def top_sort_bfs(graph: Dict[str, Set]) -> Optional[List]:
    """
    Using BFS and Indegree of nodes - Kahn's Algorithm
    Intuition:
    - Repeatedly remove nodes without any dependencies from the graph and add them to topological sorting
    - As nodes without dependencies are removed from the graph (along with their outgoing edges), new nodes without
      dependencies should become free
    - Repeat this process until all nodes are processed or a cycle is discovered
    Topological sorting can only be found for directed acyclic graphs
    """
    def _get_in_degrees(graph):
        in_degrees = {n: 0 for n in graph.keys()}
        for node, nbrs in graph.items():
            for nbr in nbrs:
                in_degrees[nbr] += 1
        return in_degrees

    in_degrees = _get_in_degrees(graph)
    queue = deque([n for n, ind in in_degrees.items() if ind == 0])  # initialize queue with nodes with 0 incoming edges
    top_ordering = []
    while queue:
        node = queue.popleft()
        top_ordering.append(node)  # add independent node to topological sorting
        for nbr in graph[node]:
            in_degrees[nbr] -= 1  # reduce the indegree of all neighbors of this node by 1 as this node will be removed
            if in_degrees[nbr] == 0:
                queue.append(nbr)  # if the nbr has 0 incoming edges after updating indegree, add nbr to queue
        del graph[node]  # delete node as it's now added to topological sorting

    # if graph has a cycle, there will be a point in time when there are no new nbrs (nodes) without any incoming edges
    # which will terminate the loop as the queue never gets refilled
    if graph:
        print("Graph is cyclic, topological sort not possible!")
        return None
    return top_ordering


if __name__ == '__main__':
    directed_cyclic_graph = SampleGraphs.directed_cyclic_conn_graph().graph
    directed_acyclic_graph = SampleGraphs.directed_acyclic_conn_graph().graph

    print_graph(directed_cyclic_graph, message="\nDirected Cyclic Graph")
    print_graph(directed_acyclic_graph, message="\nDirected Acyclic Graph")

    print("\n=> Topological Sort using DFS Color Marker Method")
    print("\n-> Directed Cyclic Graph")
    print(top_sort_dfs(graph=directed_cyclic_graph))
    print("\n-> Directed Acyclic Graph")
    print(top_sort_dfs(graph=directed_acyclic_graph))

    print("\n=> Topological Sort using BFS Indegree Method - Kahn's Algorithm")
    print("\n-> Directed Cyclic Graph")
    print(top_sort_bfs(graph=copy.deepcopy(directed_cyclic_graph)))
    print("\n-> Directed Acyclic Graph")
    print(top_sort_bfs(graph=copy.deepcopy(directed_acyclic_graph)))

