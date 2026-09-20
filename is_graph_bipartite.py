# 785. Is Graph Bipartite?
# There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D 
# array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v 
# in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:
#     There are no self-edges (graph[u] does not contain u).
#     There are no parallel edges (graph[u] does not contain duplicate values).
#     If v is in graph[u], then u is in graph[v] (the graph is undirected).
#     The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge 
# in the graph connects a node in set A and a node in set B.
# Return true if and only if it is bipartite.
# Example 1:
# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: There is no way to partition the nodes into two independent sets such that every edge connects 
# a node in one and a node in the other.
# Example 2:
# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
# Constraints:
#     graph.length == n
#     1 <= n <= 100
#     0 <= graph[u].length < n
#     0 <= graph[u][i] <= n - 1
#     graph[u] does not contain u.
#     All the values of graph[u] are unique.
#     If graph[u] contains v, then graph[v] contains u.

# class DSU_with_rollbacks_and_bipartite_check:
#     def __init__(self, n):
#         self.parent = list(range(n))

#         self.size = [1] * n
#         self.comps = n
#         self.is_bipartite = True
#         self.color = [0] * n

#     def find(self, x: int) -> tuple[int, int]:
#         parent = x
#         parity = 0
#         while self.parent[parent] != parent:
#             parity ^= self.color[parent]
#             parent = self.parent[parent]

#         return parent, parity

#     def union(self, x: int, y: int) -> bool:
#         x, parity_x = self.find(x)
#         y, parity_y = self.find(y)

#         if x == y:
#             is_bipartite = parity_x != parity_y
#             if not is_bipartite:
#                 return False
#             return True

#         if self.size[x] < self.size[y]:
#             x, y = y, x
#             parity_x, parity_y = parity_y, parity_x
#         self.parent[y] = x
                
#         self.color[y] = parity_x ^ parity_y ^ 1
#         self.size[x] += self.size[y]
#         self.comps -= 1
#         return True

#     def get_comps(self):
#         return self.comps


#     def get_size(self, x: int) -> int:
#         return self.size[self.find(x)[0]]

#     def get_parent(self, x: int) -> int:
#         return self.parent[self.find(x)[0]]



# class Solution:
#     def isBipartite(self, graph: list[list[int]]) -> bool:
#         dsu = DSU_with_rollbacks_and_bipartite_check(len(graph))
#         for i in range(len(graph)):
#             for j in graph[i]:
#                 if not dsu.union(i, j):
#                     return False
#         return True


from collections import deque

# class Solution:
#     def isBipartite(self, graph: list[list[int]]) -> bool:
#         n = len(graph)
#         remaining = [1] * n
#         colored = [-1] * n
#         bipartite = True
#         queue = deque()
#         for i in range(n):
#             if remaining[i] == 0 or not bipartite:
#                 continue
#             queue.append(i)
#             colored[i] = 0
#             while queue:
#                 u = queue.popleft()
#                 remaining[u] = 0
#                 for v in graph[u]:
#                     if colored[v] == -1:
#                         colored[v] = colored[u] ^ 1
#                         queue.append(v)
#                         remaining[v] = 0
#                     if colored[v] == colored[u]:
#                         return False
       
#         return True
    
    
from collections import deque
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n=len(graph)
        colour=[-1]*n
        queue=deque()
        for i in range(n):
            if colour[i]==-1:
                colour[i]=0
                queue.append(i)
                
                while queue:
                    node=queue.popleft()
                    for i in graph[node]:
                        if colour[i]==-1:
                            colour[i]=1-colour[node]
                            queue.append(i)
                        elif colour[i]==colour[node]:
                            return False
        return True

                