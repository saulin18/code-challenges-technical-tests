# 1192. Critical Connections in a Network
# There are n servers numbered from 0 to n - 1
# connected by undirected server-to-server connections forming a
# network where connections[i] = [ai, bi] represents a connection
# between servers ai and bi. Any server can reach other servers
# directly or indirectly through the network.

# A critical connection is a connection that, if removed, will make some servers
# unable to reach some other server.

# Return all critical connections in the network in any order.
# Example 1:

# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
# Example 2:

# Input: n = 2, connections = [[0,1]]
# Output: [[0,1]]


# Constraints:

# 2 <= n <= 105
# n - 1 <= connections.length <= 105
# 0 <= ai, bi <= n - 1
# ai != bi
# There are no repeated connections.

from typing import List
from collections import defaultdict

# def tarjan(nodo_actual, padre):
#     visitados.add(nodo_actual)
#     low[nodo_actual] = timer[0]  # noqa: F823
#     disc[nodo_actual] = timer[0]
#     timer[0] += 1  # noqa: F841
#     child = 0

#     for v in adj_list[nodo_actual]:
#         if v == padre:
#             continue
#         if v not in visitados:
#             child += 1
#             tarjan(v, nodo_actual)
#             low[nodo_actual] = min(low[nodo_actual], low[v])
#             if padre != -1 and low[v] >= disc[nodo_actual]:
#                 articulation_points.add(nodo_actual)
#         else:
#             low[nodo_actual] = min(low[nodo_actual], disc[v])
#     if padre == -1 and child > 1:
#         articulation_points.add(nodo_actual)


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:

        if n == 2:
            return connections

        adj_list = defaultdict(list)
        low = [-1] * (n + 1)
        disc = [-1] * (n + 1)
        timer = [1]
        for u, v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)

        critical_connections = set()
        visited = set()

        def tarjan(node, parent):
            visited.add(node)
            low[node] = timer[0]
            disc[node] = timer[0]
            timer[0] += 1
            child = 0
            for neighbour in adj_list[node]:
                if neighbour == parent:
                    continue
                if neighbour not in visited:
                    child += 1
                    tarjan(neighbour, node)
                    low[node] = min(low[node], low[neighbour])
                    if parent != -1 and low[neighbour] > disc[node]:
                        critical_connections.add((node, neighbour))
                else:
                    low[node] = min(low[node], disc[neighbour])
            if parent == -1 and child > 1:
                critical_connections.add((node, parent))

        for i in range(n):
            if i not in visited:
                tarjan(i, i)

        return list(critical_connections)