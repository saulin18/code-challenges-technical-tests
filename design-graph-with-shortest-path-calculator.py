# 2642. Design Graph With Shortest Path Calculator
# There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. The edges of the graph are
# initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from
#  fromi to toi with the cost edgeCosti.
# Implement the Graph class:
#Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
#addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. It is guaranteed that there is no edge between the two
# nodes before adding this one.
#int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. If no path exists, return -1. The cost of a
#  path is the sum of the costs of the edges in the path.
# Example 1:
# Input
# ["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
# [[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
# Output
# [null, 6, -1, null, 6]
# Explanation
# Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
# g.shortestPath(3, 2); // return 6. The shortest path from 3 to 2 in the first diagram above is 3 -> 0 -> 1 -> 2 with a total cost of 3 + 2 + 1 = 6.
# g.shortestPath(0, 3); // return -1. There is no path from 0 to 3.
# g.addEdge([1, 3, 4]); // We add an edge from node 1 to node 3, and we get the second diagram above.
# g.shortestPath(0, 3); // return 6. The shortest path from 0 to 3 now is 0 -> 1 -> 3 with a total cost of 2 + 4 = 6.
# Constraints:
#     1 <= n <= 100
#     0 <= edges.length <= n * (n - 1)
#     edges[i].length == edge.length == 3
#     0 <= fromi, toi, from, to, node1, node2 <= n - 1
#     1 <= edgeCosti, edgeCost <= 106
#     There are no repeated edges and no self-loops in the graph at any point.
#     At most 100 calls will be made for addEdge.
#     At most 100 calls will be made for shortestPath.
from collections import defaultdict
from heapq import heapify, heappush, heappop
from typing import List
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adj_list = defaultdict(list)
        for origin, to, cost in edges:
            self.adj_list[origin].append((to, cost))

    def addEdge(self, edge: List[int]) -> None:
        origin, to, cost = edge
        self.adj_list[origin].append((to, cost))

    def shortestPath(self, node1: int, node2: int) -> int:

        distances = {i: float("inf") for i in range(self.n)}
        distances[node1] = 0
        my_queue = []
        heapify(my_queue)
        heappush(my_queue, (0, node1))
        for i in range(self.n):
            if i != node1:
                heappush(my_queue, (float("inf"), i))

        while my_queue:
            cost, node = heappop(my_queue)

            if cost > distances[node]:
                continue

            if node == node2:
                return cost

            for neighbour, cost_of_neighbour in self.adj_list[node]:
                dist = cost + cost_of_neighbour
                if dist < distances[neighbour]:
                    distances[neighbour] = dist
                    heappush(my_queue, (dist, neighbour))

        return -1


# DON'T USE A DICT IF THE POSSIBLE NODE VALUES ARE FROM 0 TO N, lol
# class Graph:

#     def __init__(self, n: int, edges: List[List[int]]):
#         self.size = n
#         self.vertices = defaultdict(list)
#         for start, end, weight in edges:
#             self.vertices[start].append((end, weight))

#     def addEdge(self, edge: List[int]) -> None:
#         start, end, weight = edge
#         self.vertices[start].append((end, weight))

#     def shortestPath(self, node1: int, node2: int) -> int:
#         dist = [float('inf')] * self.size
#         dist[node1] = 0
#         heap = []
#         heapq.heappush(heap, (dist[node1], node1))
#         while heap:
#             current_dist, current_node = heapq.heappop(heap)
#             if current_node == node2:
#                 return current_dist
#             if current_dist > dist[node2]:
#                 continue
#             for neighbor_node, neighbor_dist in self.vertices[current_node]:
#                 if current_dist + neighbor_dist < dist[neighbor_node]:
#                     dist[neighbor_node] = current_dist + neighbor_dist
#                     heapq.heappush(heap, (dist[neighbor_node], neighbor_node))
#         return -1



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
