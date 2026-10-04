# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/?envType=problem-list-v2&envId=9id9ahz7

# 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

# Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges
# where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi.
# A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles
# and with the minimum possible total edge weight.

# Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST
# edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the
# other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.
# Note that you can return the indices of the edges in any order.
# Example 1:

# Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
# Output: [[0,1],[2,3,4,5]]
# Explanation: The figure above describes the graph.
# The following figure shows all the possible MSTs:

# Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
# The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.

# Example 2:

# Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
# Output: [[],[0,1,2,3]]
# Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.


# Constraints:

#     2 <= n <= 100
#     1 <= edges.length <= min(200, n * (n - 1) / 2)
#     edges[i].length == 3
#     0 <= ai < bi < n
#     1 <= weighti <= 1000
#     All pairs (ai, bi) are distinct.
class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.rank: list[int] = [0] * (n)
        self.parent: list[int] = [i for i in range(n)]

    def find(self, x) -> int:
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        parx = self.find(x)
        pary = self.find(y)

        if parx == pary:
            return False

        if self.rank[parx] < self.rank[pary]:
            self.parent[parx] = pary

        elif self.rank[pary] < self.rank[parx]:
            self.parent[pary] = parx
        else:
            self.parent[pary] = parx
            self.rank[parx] += 1

        self.n -= 1
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: list[list[int]]
    ) -> list[list[int]]:

        edges_set = sorted(enumerate(edges), key=lambda x: x[1][2])
        mst_weight = self.find_mst(n, [edge for _, edge in edges_set])
        critical = []
        pseudo_critical = []

        for index, (u, v, w) in edges_set:

            # weight without the edge
            weight_of_minimum_spanning_tree = self.find_mst(
                n, [edge for i, edge in edges_set if i != index]
            )
            if weight_of_minimum_spanning_tree > mst_weight:
                critical.append(index)
            elif weight_of_minimum_spanning_tree < mst_weight:
                critical.append(index)
            else:
                weigth_with_edge = self.find_mst(
                    n, [[u, v, w]] + [edge for _, edge in edges_set if _ != index]
                )

                if weigth_with_edge == mst_weight:
                    pseudo_critical.append(index)

        return [critical, pseudo_critical]

    def find_mst(self, n: int, edges: list[list[int]]) -> int:
        uf = UnionFind(n)
        mst_weight = 0
        for i, (u, v, w) in enumerate(edges):
            if uf.union(u, v):
                mst_weight += w
        return mst_weight

    # def find_bridges(self, adj_list: dict[int, list[tuple[int, int]]] , n: int) -> list[tuple[int, int]]:
    #         visited = [False] * n
    #         disc = [1] * n
    #         low = [1] * n
    #         bridges: list[tuple[int, int]]  = []
    #         timer = [0]
    #         def tarjan(node: int, parent: int = -1) -> None:
    #             nonlocal timer, adj_list, visited, disc, low, bridges
    #             disc[node] = low[node] = timer[0]
    #             timer[0] +=1
    #             visited[node] = True

    #             for neighbour, weight in adj_list[node]:
    #                 if neighbour == parent:
    #                     continue
    #                 if visited[neighbour]:
    #                     #low[node] = min(low[node], disc[neighbour])
    #                     continue
    #                 tarjan(neighbour, node)
    #                 visited[neighbour] = True

    #                 if low[neighbour] > disc[node]:
    #                     bridges.append((node, neighbour))

    #                 low[node] = min(low[node], low[neighbour])

    #         tarjan(0)
    #         return bridges
