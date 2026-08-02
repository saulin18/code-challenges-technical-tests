from typing import Sequence
from collections import defaultdict

# 1928. Minimum Cost to Reach Destination in Time
# There is a country of n cities numbered from 0 to n - 1 where all the cities are connected by bi-directional roads.
# The roads are represented as a 2D integer array edges where edges[i] = [xi, yi, timei] denotes a road between cities
#  xi and yi that
# takes timei minutes to travel.
#
# There may be multiple roads of differing travel times connecting the same two cities,
#  but no road connects a city to itself.
# Each time you pass through a city, you must pay a passing fee.
# This is represented as a 0-indexed integer array passingFees of length n where passingFees[j] is the amount of dollars you must pay
# when you pass through city j.
# In the beginning, you are at city 0 and want to reach city n - 1 in maxTime minutes or less. The cost of your journey is the summation
# of passing fees for each city that you passed through at some moment of your journey (including the source and destination cities).
# Given maxTime, edges, and passingFees, return the minimum cost to complete your journey, or -1 if you cannot complete it
# within maxTime minutes.
# Example 1:
# Input: maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
# Output: 11
# Explanation: The path to take is 0 -> 1 -> 2 -> 5, which takes 30 minutes and has $11 worth of passing fees.
# Example 2:
# Input: maxTime = 29, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
# Output: 48
# Explanation: The path to take is 0 -> 3 -> 4 -> 5, which takes 26 minutes and has $48 worth of passing fees.
# You cannot take path 0 -> 1 -> 2 -> 5 since it would take too long.
# Example 3:
# Input: maxTime = 25, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
# Output: -1
# Explanation: There is no way to reach city 5 from city 0 within 25 minutes.
# Constraints:
#     1 <= maxTime <= 1000
#     n == passingFees.length
#     2 <= n <= 1000
#     n - 1 <= edges.length <= 1000
#     0 <= xi, yi <= n - 1
#     1 <= timei <= 1000
#     1 <= passingFees[j] <= 1000
#     The graph may contain multiple edges between two nodes.
#     The graph does not contain self loops.
from heapq import heapify, heappop, heappush


class Solution:

    def minCost(self, maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:
        res = 0

        # Nodes from 0 to n - 1
        n = len(passingFees)

        adj_list = defaultdict(list)

        for node1, node2, time in edges:
            adj_list[node1].append((node2, time))
            adj_list[node2].append((node1, time))

        # fee, distance, node
        # the priority queue (min-heap) always order by the value of the first element
        my_priority_queue : Sequence[tuple[int, int, int]] = [(passingFees[0], 0, 0)]
        heapify(my_priority_queue)

        distances_and_fees_to_node = [[float("inf") for _ in range(maxTime + 1)] for _ in range(n)]
        distances_and_fees_to_node[0][0] = passingFees[0]

        while my_priority_queue:
            fee, distance, node = heappop(my_priority_queue)
            
            if fee > distances_and_fees_to_node[node][distance]:
                continue

            if node == n - 1:
                return fee

            for neightbour, time in adj_list[node]:
                neightbour_fee = passingFees[neightbour]

                if distance + time > maxTime:
                    continue

                if distances_and_fees_to_node[neightbour][distance + time] > fee + neightbour_fee:
                    distances_and_fees_to_node[neightbour][distance + time] = fee + neightbour_fee
                    heappush(my_priority_queue, (fee + neightbour_fee, distance + time, neightbour))


        return -1



"""
Run a BFS and ensure that time is within bounds
Algo
INitialization
1. Initialize by making a map from source_city -> [destination_city, time, cost]
2. BFS algo
2.1 Pick node with minimum cost from the node
2.2 add it to min-heap with cost = cur_cost + cost needed, cur_time+time_needed
2.3 repeat until we reach node n-1 within time
2.4 if node is never reached, then return -1
2.5 if cur_min is > maxTime then return -1

TC: O(NlogE)
SC: O(n)


- We are sorting by cost
- if a node is visited later, then cost is already higher. In this case, only consider if time is < prev_seentime 
"""
# import heapq
# import heapq
# from typing import List

# class Solution:
#     def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
#         n = len(passingFees)
#         graph = [[] for _ in range(n)]
#         for u, v, t in edges:
#             graph[u].append((v, t))
#             graph[v].append((u, t))

#         best_time = [float('inf')] * n
#         best_time[0] = 0
#         heap = [(passingFees[0], 0, 0)]  # (cost, time, node)

#         while heap:
#             cost, time, node = heapq.heappop(heap)
#             if node == n - 1:
#                 return cost                      # first pop = min cost (cost-ordered)
#             for nxt, t in graph[node]:
#                 nt = time + t
#                 if nt <= maxTime and nt < best_time[nxt]:
#                     best_time[nxt] = nt          # only push on strict time improvement
#                     heapq.heappush(heap, (cost + passingFees[nxt], nt, nxt))
#         return -1
        