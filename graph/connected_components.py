from collections import deque
from typing import Dict, Set

from graph import SampleGraphs, print_graph
from unionfind import DisjointSetUnion


def conn_comps_using_dfs(graph: Dict[str, Set]) -> int:
    """
    Find connected components in a graph using DFS
    Works for all types of graphs {directed, undirected, cyclic, acyclic}
    """
    def _dfs(graph, node, visited):
        visited.add(node)
        for nbr in graph[node] - visited:
            _dfs(graph, nbr, visited)

    visited = set()
    comps = 0
    for node in graph:
        if node not in visited:
            comps += 1
            _dfs(graph, node, visited)
    return comps


def conn_comps_using_bfs(graph: Dict[str, Set]) -> int:
    """
    Find connected components in a graph using BFS
    Works for all types of graphs {directed, undirected, cyclic, acyclic}
    """
    def _bfs(graph, start, visited):
        queue = deque([start])
        while queue:
            node = queue.popleft()
            visited.add(node)
            queue.extend(graph[node] - visited)

    visited = set()
    comps = 0
    for node in graph:
        if node not in visited:
            comps += 1
            _bfs(graph, node, visited)
    return comps


def conn_comps_undirected_union_find(graph: Dict[str, Set]) -> int:
    """
    Find connected components in an undirected graph using Disjoint Set Union
    Works for both cyclic and acyclic undirected graphs
    """
    dsu = DisjointSetUnion()
    dsu.make_set(graph.keys())

    for node, nbrs in graph.items():
        for nbr in nbrs:
            dsu.union_set(node, nbr)

    return dsu.get_disjoint_set_count()


if __name__ == '__main__':
    undirected_connected_graph = SampleGraphs.undirected_cyclic_conn_graph().graph
    undirected_disconnected_graph = SampleGraphs.undirected_cyclic_disconn_graph().graph

    print_graph(undirected_connected_graph, message="\nUndirected Connected Graph")
    print_graph(undirected_disconnected_graph, message="\nUndirected Disconnected Graph")

    print("\n=> Connected Components in a graph using DFS; works for all types of graphs {directed, undirected, cyclic, acyclic}")
    print("\n-> Connected Graph")
    print(conn_comps_using_dfs(graph=undirected_connected_graph))
    print("\n-> Disconnected Graph")
    print(conn_comps_using_dfs(graph=undirected_disconnected_graph))

    print("\n=> Connected Components in a graph using BFS; works for all types of graphs {directed, undirected, cyclic, acyclic}")
    print("\n-> Connected Graph")
    print(conn_comps_using_bfs(graph=undirected_connected_graph))
    print("\n-> Disconnected Graph")
    print(conn_comps_using_bfs(graph=undirected_disconnected_graph))

    print("\n=> Connected Components in an Undirected Graph using Disjoint Set Union (Union-Find)")
    print("\n-> Undirected Connected Graph")
    print(conn_comps_undirected_union_find(graph=undirected_connected_graph))
    print("\n-> Undirected Disconnected Graph")
    print(conn_comps_undirected_union_find(graph=undirected_disconnected_graph))
