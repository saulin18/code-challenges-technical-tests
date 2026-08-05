# https://leetcode.com/problems/max-area-of-island/description/?envType=problem-list-v2&envId=union-find
# 695. Max Area of Island
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
# You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.
# Example 1:
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0]
# ,[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
# Constraints:
#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 50
#     grid[i][j] is either 0 or 1.

from typing import List
class DSU:
    def __init__(self, grid: List[List[int]]):
        self.parent = {}
        self.rank = {}
        self.size = {}
        self.max_size = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.parent[(i, j)] = (i, j)
                    self.rank[(i, j)] = 0
                    self.size[(i, j)] = 1
                    self.max_size = 1
                    
                    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
                self.size[rootX] += self.size[rootY]
        self.max_size = max(self.max_size, self.size[rootX], self.size[rootY])
        return self.max_size
    
    def getMaxSize(self):
        return self.max_size
 
 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dsu = DSU(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i + 1 < len(grid) and grid[i + 1][j] == 1:
                        dsu.union((i, j), (i + 1, j))
                    if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                        dsu.union((i, j), (i, j + 1))
        return dsu.getMaxSize()
        
    

# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         if not grid:
#             return 0

#         rows, cols = len(grid), len(grid[0])

#         def dfs(r, c):
#             if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
#                 return 0
#             grid[r][c] = 0
#             return (1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r, c+1) + dfs(r, c-1))

#         max_area = 0
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 1:
#                     max_area = max(max_area, dfs(r, c))
#         return max_area


 

        


        