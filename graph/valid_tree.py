import random
from typing import Dict, Set

from graph import SampleGraphs, print_graph

"""
An undirected graph can only be a valid tree if graph is connected (only one connected component) and it has no cycles. 
Check the following conditions:
    1. Total number of edges = number of vertices - 1
        - If number of edges < number of vertices - 1 => graph is disconnected
        - If number of edges > number of vertices - 1 => graph has a cycle
    2. All nodes in the graph must be visited in a single-pass DFS started from any node in the graph
If for some reason information regarding number of edges is not available, a DFS can be used to detect cycles in graph

For a directed graph, number of edges cannot be used to check if it has a cycle or whether it's connected. Also, a single 
pass DFS is not enough. To check if a directed graph is a valid tree, perform a full DFS (multiple passes are allowed unless 
all nodes are discovered) and verify the following:
    1. There are no cycles
    2. Number of connected components == 1  
"""


def graph_valid_tree_undirected_using_num_edges(graph: Dict[str, Set]) -> bool:
    def _get_num_edges(graph):
        num_edges = 0
        for node, nbrs in graph.items():
            for _ in nbrs:
                num_edges += 1
        return num_edges // 2

    def _dfs(graph, node, visited):
        visited.add(node)
        for nbr in graph[node] - visited:
            _dfs(graph, nbr, visited)

    nodes = list(graph.keys())
    num_nodes = len(nodes)
    num_edges = _get_num_edges(graph)

    if num_edges != num_nodes - 1:
        return False  # if num_edges > num_nodes - 1 => cycle exist; num_edges < num_nodes - 1 => graph disconnected

    visited = set()
    _dfs(graph=graph, node=random.choice(nodes), visited=visited)  # Run DFS only once (single pass)

    return len(visited) == num_nodes


def graph_valid_tree_undirected_using_dfs(graph: Dict[str, Set]) -> bool:
    def _dfs_find_cycles(graph, node, prev, visited):
        visited.add(node)
        for nbr in graph[node]:
            if nbr != prev:  # ignore bidirected edges in an undirected graph causing trivial cycles
                if nbr in visited:
                    return True
                if _dfs_find_cycles(graph, nbr, node, visited):
                    return True
        return False

    nodes, visited = list(graph.keys()), set()
    return not _dfs_find_cycles(graph, random.choice(nodes), "#", visited) and len(visited) == len(nodes)


def graph_valid_tree_directed_using_dfs(graph: Dict[str, Set]) -> bool:
    def _dfs_find_cycles(graph, node, markers):
        markers[node] = 1
        for nbr in graph[node]:
            if markers[nbr] == 1:
                return True
            if _dfs_find_cycles(graph, nbr, markers):
                return True
        markers[node] = 2
        return False

    conn_comps, markers = 0, dict.fromkeys(graph, 0)
    for node in graph:
        if markers[node] == 0:
            conn_comps += 1
            if _dfs_find_cycles(graph, node, markers):
                return False
    return conn_comps == 1


if __name__ == '__main__':
    valid_undirected_graph = SampleGraphs.undirected_acyclic_conn_graph().graph
    invalid_undirected_graph = SampleGraphs.undirected_cyclic_conn_graph().graph
    valid_directed_graph = SampleGraphs.directed_acyclic_conn_graph().graph
    invalid_directed_graph = SampleGraphs.directed_acyclic_disconn_graph().graph

    print_graph(valid_undirected_graph, message="\nUndirected Connected Acyclic Graph - Valid")
    print_graph(invalid_undirected_graph, message="\nUndirected Connected Cyclic Graph - Invalid")
    print_graph(valid_directed_graph, message="\nDirected Connected Acyclic Graph - Valid")
    print_graph(invalid_directed_graph, message="\nDirected Disconnected Acyclic Graph - Invalid")

    print("\n=> Check if an Undirected Graph is a valid tree using number of edges and DFS")
    print("\n-> Undirected Connected Acyclic Graph - Valid")
    print(graph_valid_tree_undirected_using_num_edges(graph=valid_undirected_graph))
    print("\n-> Undirected Connected Cyclic Graph - Invalid")
    print(graph_valid_tree_undirected_using_num_edges(graph=invalid_undirected_graph))

    print("\n=> Check if an Undirected Graph is a valid tree using only DFS")
    print("\n-> Undirected Connected Acyclic Graph - Valid")
    print(graph_valid_tree_undirected_using_dfs(graph=valid_undirected_graph))
    print("\n-> Undirected Connected Cyclic Graph - Invalid")
    print(graph_valid_tree_undirected_using_dfs(graph=invalid_undirected_graph))

    print("\n=> Check if a Directed Graph is a valid tree using DFS and connected components")
    print("\n-> Directed Connected Acyclic Graph - Valid")
    print(graph_valid_tree_directed_using_dfs(graph=valid_directed_graph))
    print("\n-> Directed Disconnected Acyclic Graph - Invalid")
    print(graph_valid_tree_directed_using_dfs(graph=invalid_directed_graph))
