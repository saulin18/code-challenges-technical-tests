# https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/?envType=problem-list-v2&envId=union-find

# 1319. Number of Operations to Make Network Connected
# There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where
# connections[i] = [ai, bi]
# represents a connection between computers ai and bi. Any computer can reach any other computer directly or
# indirectly through the network.
# You are given an initial computer network connections. You can extract certain cables between two directly
#  connected computers, and place them between any pair of disconnected computers to make them directly connected.
# Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.
# Example 1:
# Input: n = 4, connections = [[0,1],[0,2],[1,2]]
# Output: 1
# Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
# Example 2:
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
# Output: 2
# Example 3:
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
# Output: -1
# Explanation: There are not enough cables.
# Constraints:
#     1 <= n <= 105
#     1 <= connections.length <= min(n * (n - 1) / 2, 105)
#     connections[i].length == 2
#     0 <= ai, bi < n
#     ai != bi
#     There are no repeated connections.
#     No two computers are connected by more than one cable.


from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x == parent_y:
            return False
        if self.rank[parent_x] > self.rank[parent_y]:
            self.parent[parent_y] = parent_x
        elif self.rank[parent_x] < self.rank[parent_y]:
            self.parent[parent_x] = parent_y
        else:
            self.parent[parent_y] = parent_x
            self.rank[parent_x] += 1
        return True

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        uf = UnionFind(n)
        for x, y in connections:
            uf.union(x, y)
        connected_components = {uf.find(i) for i in range(n)}

        res = len(connected_components) - 1

        if len(connections) < n - 1:
            return -1

        return res
