# 994. Rotting Oranges
# You are given an m x n grid where each cell can have one of three values:

#     0 representing an empty cell,
#     1 representing a fresh orange, or
#     2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 10
#     grid[i][j] is 0, 1, or 2.


from collections import deque
from typing_extensions import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0]) 
        res = 0
        fresh_count = 0
        queue = deque()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1
                    
        if fresh_count == 0:
            return 0
        
        while queue:
            size = len(queue)
            if fresh_count == 0:
                break
            for _ in range(size):
                row, col = queue.popleft()
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_row = row + dx
                    new_col = col + dy
                    if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))
                        fresh_count -= 1
            res += 1
        return res if fresh_count == 0 else -1



# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         m=len(grid)
#         n=len(grid[0])
#         queue=deque()
#         directions=[(0,1),(0,-1),(1,0),(-1,0)]
#         fresh_cnt=0
#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c]==2:
#                     queue.append((r,c,0))
#                 elif grid[r][c]==1:
#                     fresh_cnt+=1
#         if fresh_cnt==0:
#             return 0
#         while queue:
#             r,c,minutes=queue.popleft()
#             for dr,dc in directions:
#                 nr,nc=r+dr,c+dc
#                 if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
#                     grid[nr][nc]=2
#                     fresh_cnt-=1
#                     queue.append((nr,nc,minutes+1))
#         return minutes if fresh_cnt==0 else -1