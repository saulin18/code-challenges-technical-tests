# 797. All Paths From Source to Target
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
# Example 1:
# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# Example 2:
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
# Constraints:
#     n == graph.length
#     2 <= n <= 15
#     0 <= graph[i][j] < n
#     graph[i][j] != i (i.e., there will be no self-loops).
#     All the elements of graph[i] are unique.
#     The input graph is guaranteed to be a DAG.

from collections import defaultdict, deque
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        res = []
        path = [0]

        def dfs(node, path):
            if node == len(graph) - 1:
                res.append(path[:])
                return
            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()

        return res

# class Solution:
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         adj = defaultdict(list)
#         n = 0
#         for i,v in enumerate(graph):
#             adj[i].extend(v)
#             n+=1
#         q = deque([(0,[0])])
#         # seen = set()
#         res = []
#         while q:
#             node,path = q.popleft()
#             if node == n-1:
#                 res.append(path)
#             # seen.add(node)
#             for nei in adj[node]:
#                 # if nei not in seen:
#                 q.append((nei,path + [nei]))
#         return res
