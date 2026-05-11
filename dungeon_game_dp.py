
# 174. Dungeon Game
# The demons had captured the princess and imprisoned her in the bottom-right 
# corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. 
# Our valiant knight was initially positioned in the top-left room and must fight 
# his way through dungeon to rescue the princess.

# The knight has an initial health point represented by a positive integer. 
# If at any point his health point drops to 0 or below, he dies immediately.

# Some of the rooms are guarded by demons (represented by negative integers), 
# so the knight loses health upon entering these rooms; other rooms are either empty
# (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

# To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

# Return the knight's minimum initial health so that he can rescue the princess.

# Note that any room can contain threats or power-ups, even the first room the knight enters and 
# the bottom-right room where the princess is imprisoned.
# Example 1:
# Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
# Output: 7
# Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
# Example 2:
# Input: dungeon = [[0]]
# Output: 1
# Constraints:
# m == dungeon.length
# n == dungeon[i].length
# 1 <= m, n <= 200
# -1000 <= dungeon[i][j] <= 1000

from typing import List
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        dp = [[0] * cols for _ in range(rows)]
        
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if row == rows - 1 and col == cols - 1:
                    dp[row][col] = max(1, 1 - dungeon[row][col])
                elif row == rows - 1:
                    dp[row][col] = max(1, dp[row][col + 1] - dungeon[row][col])
                elif col == cols - 1:
                    dp[row][col] = max(1, dp[row + 1][col] - dungeon[row][col])
                else:
                    dp[row][col] = max(1, min(dp[row + 1][col], dp[row][col + 1]) - dungeon[row][col])
        return dp[0][0]
    
    
# class Solution:
#     def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
#         # This problem is best solved using Dynamic Programming from the bottom-right
#         # to the top-left. At each cell, we calculate the minimum health needed 
#         # to reach the princess (at the bottom-right) from that cell.
        
#         rows = len(dungeon)
#         cols = len(dungeon[0])
        
#         # dp[i][j] represents the minimum health needed before entering cell (i, j)
#         dp = [[0] * cols for _ in range(rows)]
        
#         # Base case: The knight must have at least 1 HP after entering the princess's cell.
#         # So, health_at_start + dungeon[rows-1][cols-1] >= 1
#         dp[rows-1][cols-1] = max(1, 1 - dungeon[rows-1][cols-1])
        
#         # Fill the last row (can only move right)
#         for j in range(cols - 2, -1, -1):
#             dp[rows-1][j] = max(1, dp[rows-1][j+1] - dungeon[rows-1][j])
            
#         # Fill the last column (can only move down)
#         for i in range(rows - 2, -1, -1):
#             dp[i][cols-1] = max(1, dp[i+1][cols-1] - dungeon[i][cols-1])
            
#         # Fill the rest of the DP table
#         for i in range(rows - 2, -1, -1):
#             for j in range(cols - 2, -1, -1):
#                 # The knight chooses the path that requires less health
#                 min_health_on_exit = min(dp[i+1][j], dp[i][j+1])
#                 dp[i][j] = max(1, min_health_on_exit - dungeon[i][j])
                
#         return dp[0][0]