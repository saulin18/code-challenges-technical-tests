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


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x == parent_y:
            return
        if self.rank[parent_x] < self.rank[parent_y]:
            self.parent[parent_x] = parent_y
        elif self.rank[parent_x] > self.rank[parent_y]:
            self.parent[parent_y] = parent_x
        else:
            self.parent[parent_y] = parent_x
            self.rank[parent_x] += 1

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


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
    
    def solve_with_dsu(self, board: List[List[str]]) -> None:
        def index(r: int, c: int) -> int:
            return r * cols + c
        rows = len(board)
        cols = len(board[0])
        dsu = DSU(rows * cols + 1)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                        # rows * cols is the dummy node for the edge nodes
                        dsu.union(index(r, c), rows * cols)
                    else:
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if board[r + dr][c + dc] == 'O':
                                dsu.union(index(r, c), index(r + dr, c + dc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and not dsu.is_connected(index(r, c), rows * cols):
                    board[r][c] = 'X'
        
        
        
        

   
        
        
        

                    