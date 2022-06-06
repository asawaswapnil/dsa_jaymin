from collections import deque
from typing import Dict, Set, List, Optional
from graph import SampleGraphs, print_graph


def dfs_paths(graph: Dict[str, Set], start: str, goal: str) -> Optional[List]:
    """
    Find path from start node to goal node using DFS
    Works for all types of graphs {directed, undirected, cyclic, acyclic}
    """
    visited = set()
    stack = [(start, [start])]  # stack entries are of the form: Tuple(node, path_so_far)
    while stack:
        node, path = stack.pop()
        visited.add(node)
        for nbr in graph[node] - visited:
            if nbr == goal:
                return path + [nbr]
            else:
                stack.append((nbr, path + [nbr]))
    print("Path from start node: '{}' to goal node: '{}' not found in graph".format(start, goal))
    return None


def bfs_paths(graph: Dict[str, Set], start: str, goal: str) -> Optional[List]:
    """
    Find path from start node to goal node using DFS
    Works for all types of graphs {directed, undirected, cyclic, acyclic}
    """
    visited = set()
    queue = deque([(start, [start])])  # queue entries are of the form: Tuple(node, path_so_far)
    while queue:
        node, path = queue.popleft()
        visited.add(node)
        for nbr in graph[node] - visited:
            if nbr == goal:
                return path + [nbr]
            else:
                queue.append((nbr, path + [nbr]))
    print("Path from start node: '{}' to goal node: '{}' not found in graph".format(start, goal))
    return None


if __name__ == '__main__':
    undirected_graph = SampleGraphs.undirected_cyclic_conn_graph().graph
    directed_graph = SampleGraphs.directed_cyclic_conn_graph().graph
    disconnected_graph = SampleGraphs.directed_cyclic_disconn_graph().graph
    start_node = 'A'
    goal_node = 'F'
    unreachable_goal_node = 'G'

    print_graph(undirected_graph, message="\nUndirected Graph")
    print_graph(directed_graph, message="\nDirected Graph")
    print_graph(disconnected_graph, message="\nDirected Disconnected Graph")
    print("\nStart Node")
    print(start_node)
    print("\nGoal Node")
    print(goal_node)
    print("\nUnreachable Goal Node in Disconnected Graph")
    print(unreachable_goal_node)

    print("\n=> DFS Paths")
    print("\n-> Undirected Graph")
    print(dfs_paths(undirected_graph, start_node, goal_node))
    print("\n-> Directed Graph")
    print(dfs_paths(directed_graph, start_node, goal_node))
    print("\n-> Disconnected Graph")
    print(dfs_paths(disconnected_graph, start_node, unreachable_goal_node))

    print("\n=> BFS Paths")
    print("\n-> Undirected Graph")
    print(bfs_paths(undirected_graph, start_node, goal_node))
    print("\n-> Directed Graph")
    print(bfs_paths(directed_graph, start_node, goal_node))
    print("\n-> Disconnected Graph")
    print(bfs_paths(disconnected_graph, start_node, unreachable_goal_node))

