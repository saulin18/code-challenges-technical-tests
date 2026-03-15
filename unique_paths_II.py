# 63. Unique Paths II
# You are given an m x n integer array grid. There is a robot initially located at
# the top-left corner (i.e., grid[0][0]). The robot tries to move to the
# bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The testcases are generated so that the answer will be less than or equal to 2 * 109.
# Example 1:
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# Example 2:
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
# Constraints:
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.


from typing import List


def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:

    if obstacleGrid[0][0] == 1:
        return 0

    dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
    number_of_rows = len(obstacleGrid)
    number_of_cols = len(obstacleGrid[0])
    dp[0][0] = 1

    obstacle_on_row_border = False
    for row in range(number_of_rows):
        if obstacleGrid[row][0] == 1:
            obstacle_on_row_border = True
            dp[row][0] = 0
            continue
        dp[row][0] = 1 if obstacle_on_row_border is False else 0

    obstacle_on_col_border = False
    for col in range(number_of_cols):
        if obstacleGrid[0][col] == 1:
            obstacle_on_col_border = True
            dp[0][col] = 0
            continue
        dp[0][col] = 1 if obstacle_on_col_border is False else 0

    for col in range(1, number_of_cols):
        for row in range(1, number_of_rows):
            if obstacleGrid[row][col] == 1:
                dp[row][col] = 0
                continue
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

    return dp[number_of_rows - 1][number_of_cols - 1]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
obstacleGridTiny = [[0, 1, 0, 0]]
print(uniquePathsWithObstacles(obstacleGrid))
print(uniquePathsWithObstacles(obstacleGridTiny))
