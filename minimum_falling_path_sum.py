# 931. Minimum Falling Path Sum
# Given an n x n array of integers matrix,
# return the minimum sum of any falling path through matrix.
# A falling path starts at any element in the
# first row and chooses the element in the next row
# that is either directly below or diagonally left/right.
# Specifically, the next element from position (row, col)
# will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

# Example 1:
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
# Example 2
# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.
# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100

from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]

        # The first status is the firsts elements of the first row always
        for col in range(0, cols):
            dp[0][col] = matrix[0][col]

        for row in range(1, rows):
            for col in range(0, cols):
                if col == 0:
                    dp[row][col] = matrix[row][col] + min(
                        dp[row - 1][col], dp[row - 1][col + 1]
                    )
                elif col == cols - 1:
                    dp[row][col] = matrix[row][col] + min(
                        dp[row - 1][col - 1], dp[row - 1][col]
                    )
                else:
                    dp[row][col] = matrix[row][col] + min(
                        dp[row - 1][col - 1], dp[row - 1][col], dp[row - 1][col + 1]
                    )
        return min(dp[rows - 1])
