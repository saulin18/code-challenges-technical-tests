# Strongly connected components
# Write a function strongly_connected_components which accepts a graph represented
# as an adjacency list, and returns a list containing set of connected components.
# Examples:
# # Graph from the image
# # The vertexes are numbered as follows:
# # (0, 1, 2, 3, 4, 5, 6, 7) = (a, b, e, f, c, g, d, h).
# # The list in the i-th position of the adjacency list
# # contains vertices that have an incoming edge from vertex i.
# # For example, from vertex 1 <=> (b), you can get to vertices
# # [2, 3, 4] <=> (e, f, c).
# >>> graph = [[1], [2, 3, 4], [0, 3], [5],
#              [5, 6], [3], [4, 7], [5, 6]]
# >>> strongly_connected_components(graph)
# [{3, 5}, {4, 6, 7}, {0, 1, 2}]

# # One more sample
# >>> graph = [[1], [2], [3, 4], [0], [5], [6], [4, 7], []]
# >>> strongly_connected_components(graph)
# [{7}, {4, 5, 6}, {0, 1, 2, 3}]
# Note: in python scipy is disabled.

from collections import defaultdict
from enum import Enum
from typing import List


def strongly_connected_components(graph: list[list[int]]):
    # index -> graph[index]

    def build_adj_list(graph: list[list[int]]) -> dict[int, list[int]]:
        adj_list = defaultdict(list)
        for i in range(len(graph)):
            adj_list[i] = graph[i]
        return adj_list

    class NodeStates(Enum):
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

    def generate_transpose(adj_list: dict[int, list[int]]) -> dict[int, list[int]]:
        transpose_adj_list = defaultdict(list)
        for i in range(len(adj_list)):
            for neighbor in adj_list[i]:
                transpose_adj_list[neighbor].append(i)
        return transpose_adj_list

    def record_finish_order(
        node: int,
        res: dict[NodeStates, list[int]],
        node_states: dict[int, NodeStates],
        adj_list: dict[int, list[int]],
    ):
        node_states[node] = NodeStates.VISITING

        for edge in adj_list[node]:
            if node_states[edge] == NodeStates.UNVISITED:
                record_finish_order(edge, res, node_states, adj_list)

        node_states[node] = NodeStates.VISITED
        res[node_states[node]].append(node)

    def get_finishing_order(
        adj_list: dict[int, list[int]],
    ) -> dict[NodeStates, list[int]]:
        res = defaultdict(list)
        node_states = {i: NodeStates.UNVISITED for i in range(len(adj_list))}

        for node in adj_list.keys():
            if node_states[node] == NodeStates.UNVISITED:
                record_finish_order(node, res, node_states, adj_list)

        return res

    def dfs(node, scc, node_states, adj_list):
        node_states[node] = NodeStates.VISITING
        scc.add(node)

        for edge in adj_list[node]:
            if node_states[edge] == NodeStates.UNVISITED:
                dfs(edge, scc, node_states, adj_list)

        node_states[node] = NodeStates.VISITED

    def find_scc_in_transpose(
        transpose: dict[int, list[int]],
        finishing_order: dict[NodeStates, list[int]],
        adj_list: dict[int, list[int]],
    ) -> list[set[int]]:
        sccs: List[set] = []

        node_states = {i: NodeStates.UNVISITED for i in range(len(adj_list))}

        for node in reversed(finishing_order[NodeStates.VISITED]):
            scc = set()
            if node_states[node] == NodeStates.UNVISITED:
                dfs(node, scc, node_states, transpose)
                sccs.append(scc)
                
        return sccs

    adj_list = build_adj_list(graph)
    transpose = generate_transpose(adj_list)

    finishing_order = get_finishing_order(adj_list)

    sccs = find_scc_in_transpose(transpose, finishing_order, adj_list)

    return sccs
