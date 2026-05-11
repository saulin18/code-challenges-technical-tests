# 64. Minimum Path Sum
# Given a m x n grid filled with non-negative numbers, find a path from
# top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.
# Example 1:
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12

from typing import List


# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:

#         rows = len(grid)
#         cols = len(grid[0])

#         def recursive(
#             current_x: int, current_y: int, memo: dict
#         ) -> int:
#             # Invalid branch
#             if current_x >= rows or current_x < 0 or current_y >= cols or current_y < 0:
#                 return float("inf")

#             actual_grid_element = grid[current_x][current_y]

#             if current_x == rows - 1 and current_y == cols - 1:
#                 return actual_grid_element

#             if (current_x, current_y) in memo:
#                 return memo[(current_x, current_y)]

#             move_right = recursive(
#                 current_x + 1, current_y, memo
#             )

#             move_down = recursive(
#                 current_x, current_y + 1, memo
#             )

#             memo[(current_x, current_y)] = actual_grid_element + min(
#                 move_right, move_down
#             )
#             return memo[(current_x, current_y)]

#         memo = {}
#         return recursive(0, 0, memo)
    

# Iterative approach

class Solution:
        def minPathSum(self, grid: List[List[int]]) -> int:
            rows = len(grid)
            cols = len(grid[0])
            dp = [[0] * cols for _ in range(rows)]
            dp[0][0] = grid[0][0]
            
            # Columns in the first row, always the sum of the previous column and the current column
            for col in range(1, cols):
                dp[0][col] = dp[0][col - 1] + grid[0][col]
            # Rows in the first column, always the sum of the previous row and the current row
            for row in range(1, rows):
                dp[row][0] = dp[row - 1][0] + grid[row][0]
            # For the rest of the grid, the sum of the minimum of the previous row and column and the current cell
            for row in range(1, rows):
                for col in range(1, cols):
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]
            return dp[rows - 1][cols - 1]
