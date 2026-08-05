# https://leetcode.com/problems/surrounded-regions/description/?envType=problem-list-v2&envId=union-find
# 130. Surrounded Regions
# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
#     Connect: A cell is connected to adjacent cells horizontally or vertically.
#     Region: To form a region connect every 'O' cell.
#     Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. 
# Such regions are completely enclosed by 'X' cells.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
# Example 1:
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation:
# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.
# Example 2:
# Input: board = [["X"]]
# Output: [["X"]]
# Constraints:
#     m == board.length
#     n == board[i].length
#     1 <= m, n <= 200
#     board[i][j] is 'X' or 'O'.


from typing_extensions import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def dfs(r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] == 'X' or board[r][c] == '#':
                return
            board[r][c] = '#'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            c = 0
            if board[r][c] == 'O':
                dfs(r, c)
            c = cols - 1
            if board[r][c] == 'O':
                dfs(r, c)
        
        for c in range(cols):
            r = 0
            if board[r][c] == 'O':
                dfs(r, c)
            r = rows - 1
            if board[r][c] == 'O':
                dfs(r, c)
                
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '#':
                    board[r][c] = 'O'
                    continue
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        
        

                    