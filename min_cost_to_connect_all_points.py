# 1584. Min Cost to Connect All Points
# You are given an array points representing integer coordinates of some points on a 2D-plane,
# where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance
# between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected
# if there is exactly one simple path between any two points.

# Example 1:
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation:
# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
# Example 2:
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
# Constraints:
# 1 <= points.length <= 1000
# -106 <= xi, yi <= 106
# All pairs (xi, yi) are distinct.

from typing import List

from heapq import heappush, heappop


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        min_heap = []

        def manhattan_distance(p1: List[int], p2: List[int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        heappush(min_heap, (0, points[0]))

        total_cost_of_connecting_all_points = 0

        while min_heap:
            cost, node = heappop(min_heap)

            if tuple(node) in visited:
                continue
            visited.add(tuple(node))

            total_cost_of_connecting_all_points += cost

            for next_node in points:
                if tuple(next_node) not in visited:
                    next_cost = manhattan_distance(node, next_node)
                    heappush(min_heap, (next_cost, next_node))
            if len(visited) == len(points):
                break
        return total_cost_of_connecting_all_points


# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         q = [(float('inf'), x, y) for x, y in points]
#         res = 0
#         while q:
#             dist, x, y = heappop(q)
#             res += dist if dist != float('inf') else 0
#             for index, (d, i, j) in enumerate(q):
#                 nd = abs(x-i) + abs(y-j)
#                 if nd < d:
#                     q[index] = (nd, i, j)
#             heapify(q)
#         return res

# import heapq

# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:

#         n = len(points)

#         minHeap = [(0, 0)]   # (cost, node)

#         visited = set()

#         minDist = [float('inf')] * n
#         minDist[0] = 0

#         totalCost = 0

#         while len(visited) < n:

#             cost, node = heapq.heappop(minHeap)

#             if node in visited:
#                 continue

#             visited.add(node)
#             totalCost += cost

#             x1, y1 = points[node]

#             for nei in range(n):

#                 if nei in visited:
#                     continue

#                 x2, y2 = points[nei]

#                 dist = abs(x1 - x2) + abs(y1 - y2)

#                 if dist < minDist[nei]:

#                     minDist[nei] = dist
#                     heapq.heappush(minHeap, (dist, nei))

#         return totalCost