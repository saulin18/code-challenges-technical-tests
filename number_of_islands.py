# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
# return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#
# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0

        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    count += 1
                    Solution.determine_if_is_a_valid_island(grid, row, col, rows, cols)

    def determine_if_is_a_valid_island(
        grid: List[List[str]],
        current_x: int,
        current_y: int,
        total_rows: int,
        total_cols: int,
    ):
        if (
            current_x < 0
            or current_x > total_rows - 1
            or current_y < 0
            or current_y > total_cols - 1
            or grid[current_x][current_y] == "0"
        ):
            return

        grid[current_x][current_y] = "0"

        Solution.determine_if_is_a_valid_island(
            grid, current_x + 1, current_y, total_rows, total_cols
        )
        Solution.determine_if_is_a_valid_island(
            grid, current_x - 1, current_y, total_rows, total_cols
        )
        Solution.determine_if_is_a_valid_island(
            grid, current_x, current_y + 1, total_rows, total_cols
        )
        Solution.determine_if_is_a_valid_island(
            grid, current_x, current_y - 1, total_rows, total_cols
        )
