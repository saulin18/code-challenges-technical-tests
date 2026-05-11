# 1091. Shortest Path in Binary Matrix
# Given an n x n binary matrix grid, return the length of the shortest clear
# path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell
# (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.
# Example 1:
# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:
# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
# Constraints:
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1

from typing import List

from collections import deque


from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])

        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
            [1, 1],
            [-1, -1],
            
            [1, -1],
            [-1, 1],
        ]

        my_queue = deque()
        my_queue.append((0, 0, 0))
        visited = set()
        while my_queue:
            curr_x, curr_y, length = my_queue.popleft()

            if (curr_x, curr_y) in visited:
                continue

            if curr_x == rows - 1 and curr_y == cols - 1 and grid[curr_x][curr_y] == 0:
                    return length + 1
                    

            visited.add((curr_x, curr_y))

            for x, y in directions:
                new_x = curr_x + x
                new_y = curr_y + y
                if (
                    0 <= new_x <= rows - 1
                    and 0 <= new_y <= cols - 1
                    and (new_x, new_y) not in visited
                    and grid[new_x][new_y] == 0
            ):
                    my_queue.append((new_x, new_y, length + 1))

        return -1
