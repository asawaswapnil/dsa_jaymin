from typing import Dict, Set

from graph import SampleGraphs, print_graph
from unionfind import DisjointSetUnion


def find_cycles_undirected_using_edge_count(graph: Dict[str, Set]) -> bool:
    """
    Check if a cycle exists in an undirected graph using number of edges and numer of nodes
    If number of edges > number of nodes => graph has a cycle
    """
    def get_edge_count(graph):
        num_edges = 0
        for node, nbrs in graph.items():
            for nbr in nbrs:
                num_edges += 1
                graph[nbr].remove(node)  # bidirected edges in an undirected graph
        return num_edges  # if not removing bidirectional edges, return num_edges // 2

    num_nodes = len(graph.keys())
    num_edges = get_edge_count(graph)
    return num_edges >= num_nodes


def find_cycles_undirected_union_find(graph: Dict[str, Set]) -> bool:
    """
    Check if a cycle exists in an undirected graph using Disjoint Set Union
    Even if a single union operation is not performed => graph has a cycle
    """
    dsu = DisjointSetUnion()
    dsu.make_set(graph.keys())

    visited = set()
    for node, nbrs in graph.items():
        for nbr in nbrs:
            if nbr not in visited:
                # skip neighbors that are already visited
                # this makes sure same edge is not reconsidered twice; eg: A -- B is same as B -- A for undirected graph
                union_performed = dsu.union_set(node, nbr)
                if not union_performed:
                    return True
        visited.add(node)
    return False


def find_cycles_undirected_dfs(graph: Dict[str, Set]) -> bool:
    """
    Check if a cycle exists in an undirected graph using DFS and `prev` pointer
    """
    def _dfs(graph, node, prev, visited):
        visited.add(node)
        for nbr in graph[node]:
            if nbr != prev:  # ignore bidirected edges in an undirected graph causing trivial cycles
                if nbr in visited:
                    return True  # cycle found
                if _dfs(graph, nbr, node, visited):
                    return True
        return False  # all neighbors visited, no cycle found so far

    visited = set()
    for node in graph:
        if node not in visited:
            if _dfs(graph, node, '#', visited):
                return True
    return False


def find_cycles_directed_dfs(graph: Dict[str, Set]) -> bool:
    """
    Check if a cycle exists in a directed graph using DFS and visit markers method
    """
    def _dfs(graph, node, markers):
        markers[node] = 1
        for nbr in graph[node]:
            if markers[nbr] == 1:
                return True  # cycle found
            if _dfs(graph, nbr, markers):
                return True
        markers[node] = 2
        return False  # all neighbors visited, no cycle found so far

    markers = dict.fromkeys(graph, 0)
    for node in graph:
        if markers[node] == 0:
            if _dfs(graph, node, markers):
                return True
    return False


if __name__ == '__main__':
    undirected_cyclic_graph = SampleGraphs.undirected_cyclic_conn_graph().graph
    undirected_acyclic_graph = SampleGraphs.undirected_acyclic_conn_graph().graph
    directed_cyclic_graph = SampleGraphs.directed_cyclic_conn_graph().graph
    directed_acyclic_graph = SampleGraphs.directed_acyclic_conn_graph().graph

    print_graph(undirected_cyclic_graph, message="\nUndirected Cyclic Graph")
    print_graph(undirected_acyclic_graph, message="\nUndirected Acyclic Graph")
    print_graph(directed_cyclic_graph, message="\nDirected Cyclic Graph")
    print_graph(directed_acyclic_graph, message="\nDirected Acyclic Graph")

    print("\n=> Find cycle in an Undirected Graph using edge count")
    print("\n-> Undirected Cyclic Graph")
    print("Found: {}".format(find_cycles_undirected_using_edge_count(graph=undirected_cyclic_graph)))
    print("\n-> Undirected Acyclic Graph")
    print("Found: {}".format(find_cycles_undirected_using_edge_count(graph=undirected_acyclic_graph)))

    print("\n=> Find cycle in an Undirected Graph using Disjoint Set Union (Union-Find)")
    print("\n-> Undirected Cyclic Graph")
    print("Found: {}".format(find_cycles_undirected_union_find(graph=undirected_cyclic_graph)))
    print("\n-> Undirected Acyclic Graph")
    print("Found: {}".format(find_cycles_undirected_union_find(graph=undirected_acyclic_graph)))

    print("\n=> Find cycle in an Undirected Graph using DFS")
    print("\n-> Undirected Cyclic Graph")
    print("Found: {}".format(find_cycles_undirected_dfs(graph=undirected_cyclic_graph)))
    print("\n-> Undirected Acyclic Graph")
    print("Found: {}".format(find_cycles_undirected_dfs(graph=undirected_acyclic_graph)))

    print("\n=> Find cycle in a Directed Graph using DFS")
    print("\n-> Directed Cyclic Graph")
    print("Found: {}".format(find_cycles_directed_dfs(graph=directed_cyclic_graph)))
    print("\n-> Directed Acyclic Graph")
    print("Found: {}".format(find_cycles_directed_dfs(graph=directed_acyclic_graph)))



