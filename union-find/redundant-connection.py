# https://leetcode.com/problems/redundant-connection/description/?envType=problem-list-v2&envId=union-find

# 684. Redundant Connection
# In this problem, a tree is an undirected graph that is connected and has no cycles.
# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
# The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an
# array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer
# that occurs last in the input.
# Example 1:
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# Example 2
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
# Constraints:
#     n == edges.length
#     3 <= n <= 1000
#     edges[i].length == 2
#     1 <= ai < bi <= edges.length
#     ai != bi
#     There are no repeated edges.
#     The given graph is connected.
from typing import List
class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        x_parent = self.find(x)
        y_parent = self.find(y)
        if x_parent == y_parent:
            return
        if self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        elif self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        else:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        UnionFind = DSU(n)
        for x, y in edges:
            if UnionFind.find(x) == UnionFind.find(y):
                return [x, y]
            UnionFind.union(x, y)

        return []
