from enum import Enum
from pprint import pprint
from typing import Dict, Set, Union

import networkx as nx
import matplotlib.pyplot as plt


class CycleFoundError(Exception):
    pass


class Markers(Enum):
    NOT_VISITED = 0  # node not visited
    BEING_VISITED = 1  # node is currently being visited (traversing through the neighbors)
    VISITED = 2  # node visited


class Graph:
    def __init__(self, graph: Dict[str, Set], is_directed: bool = False):
        self.graph = graph
        self.is_directed = is_directed


# ----- Utilities -----

def print_graph(graph: Union[Graph, Dict[str, Set]], message: str) -> None:
    if isinstance(graph, Graph):
        graph = graph.graph
    print(message)
    pprint(graph)


def visualize_graph(graph: Graph) -> None:
    _graph = graph.is_directed and nx.DiGraph(graph.graph) or nx.Graph(graph.graph)
    nx.draw_networkx(_graph, with_labels=True, node_color="c", edge_color="k", font_size=10)
    plt.show()


# ----- Sample Graphs -----

class SampleGraphs:
    @staticmethod
    def undirected_cyclic_conn_graph() -> Graph:
        _graph = {
            'A': {'B', 'C'},
            'B': {'A', 'D', 'E'},
            'C': {'A', 'F'},
            'D': {'B'},
            'E': {'B', 'F'},
            'F': {'C', 'E'}
        }
        return Graph(graph=_graph, is_directed=False)

    @staticmethod
    def undirected_acyclic_conn_graph() -> Graph:
        _graph = {
            'A': {'B', 'C'},
            'B': {'A', 'D', 'E'},
            'C': {'A', 'F'},
            'D': {'B'},
            'E': {'B'},
            'F': {'C'}
        }
        return Graph(graph=_graph, is_directed=False)

    @staticmethod
    def undirected_cyclic_disconn_graph() -> Graph:
        _graph = {
            'A': {'B', 'C'},
            'B': {'A', 'D', 'E'},
            'C': {'A', 'F'},
            'D': {'B'},
            'E': {'B', 'F'},
            'F': {'C', 'E'},
            'G': {'H'},
            'H': {'G'}
        }
        return Graph(graph=_graph, is_directed=False)

    @staticmethod
    def undirected_acyclic_disconn_graph() -> Graph:
        _graph = {
            'A': {'B', 'C'},
            'B': {'A', 'D', 'E'},
            'C': {'A', 'F'},
            'D': {'B'},
            'E': {'B'},
            'F': {'C'},
            'G': {'H'},
            'H': {'G'}
        }
        return Graph(graph=_graph, is_directed=False)

    @staticmethod
    def directed_cyclic_conn_graph() -> Graph:
        _graph = {
            'A': {'B', 'C'},
            'B': {'D', 'E'},
            'C': {'E', 'F'},
            'D': {'A'},
            'E': set(),
            'F': set()
        }
        return Graph(graph=_graph, is_directed=True)

    @staticmethod
    def directed_acyclic_conn_graph() -> Graph:
        _graph = {
            'A': {'B', 'C'},
            'B': {'D', 'E'},
            'C': {'E', 'F'},
            'D': set(),
            'E': set(),
            'F': set()
        }
        return Graph(graph=_graph, is_directed=True)

    @staticmethod
    def directed_cyclic_disconn_graph() -> Graph:
        _graph = {
            'A': {'B', 'C'},
            'B': {'D', 'E'},
            'C': {'E', 'F'},
            'D': {'A'},
            'E': set(),
            'F': set(),
            'G': {'H'},
            'H': set()
        }
        return Graph(graph=_graph, is_directed=True)

    @staticmethod
    def directed_acyclic_disconn_graph() -> Graph:
        _graph = {
            'A': {'B', 'C'},
            'B': {'D', 'E'},
            'C': {'E', 'F'},
            'D': set(),
            'E': set(),
            'F': set(),
            'G': {'H'},
            'H': set()
        }
        return Graph(graph=_graph, is_directed=True)
