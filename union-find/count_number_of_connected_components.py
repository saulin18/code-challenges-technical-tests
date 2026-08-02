# 2685. Count the Number of Complete Components
# You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1.
# You are given a 2D integer
# array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.
# Return the number of complete connected components of the graph.
# A connected component is a subgraph of a graph in which there exists a path between any
# two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.
# A connected component is said to be complete if there exists an edge between every pair of its vertices.
# Example 1:
# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
# Output: 3
# Explanation: From the picture above, one can see that all of the components of this graph are complete.
# Example 2:
# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
# Output: 1
# Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between
# every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not
# complete since there is no edge between vertices 4 and 5. Thus, the number of complete components
# in this graph is 1.
# Constraints:
#     1 <= n <= 50
#     0 <= edges.length <= n * (n - 1) / 2
#     edges[i].length == 2
#     0 <= ai, bi <= n - 1
#     ai != bi
#     There are no repeated edges.


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n
        self.edges = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            self.edges[rootX] += 1
            return

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
            self.update_size_and_edges(rootY, rootX)
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
            self.update_size_and_edges(rootX, rootY)
        else:
            self.parent[rootX] = rootY
            self.rank[rootY] += 1
            self.update_size_and_edges(rootY, rootX)

    def update_size_and_edges(self, x: int, y: int):
        self.size[x] += self.size[y]
        self.edges[x] += self.edges[y] + 1

    def isComplete(self, x: int) -> bool:
        root = self.find(x)
        return self.edges[root] == self.size[root] * (self.size[root] - 1) // 2


class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])

        # seen = set()
        # return sum(
        #     1
        #     for i in range(n)
        #     if uf.isComplete(i) and uf.find(i) not in seen and not seen.add(uf.find(i))
        # )
        count = 0
        seen = set()
        for i in range(n):
            root = uf.find(i)
            if root not in seen and uf.isComplete(root):
                seen.add(root)
                count += 1
        return count




# class Solution:
#     def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
#         graph = defaultdict(list)
#         visited = set()
#         ans = 0
        
#         for edge in edges:
#             graph[edge[0]].append(edge[1])
#             graph[edge[1]].append(edge[0])

#         def dfs(node):
#             nonlocal nodes, edges_count

#             visited.add(node)
#             nodes += 1
#             edges_count += len(graph[node])

#             for nei in graph[node]:
#                 if nei not in visited:
#                    dfs(nei)

#         for node in range(n):
#             if node in visited:
#                 continue
#             nodes = 0
#             edges_count = 0
#             dfs(node)
            
#             if edges_count == nodes*(nodes-1):
#                 ans += 1
    
#         return ans