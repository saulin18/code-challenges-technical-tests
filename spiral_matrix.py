
# Given an m x n matrix, return all elements of the matrix in spiral order.
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


from typing import List



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix:
            return []
        
        results = []
        
        number_of_rows = len(matrix)
        number_of_cols = len(matrix[0])
        top, bottom, left, right = 0, number_of_rows - 1, 0, number_of_cols - 1
        
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                results.append(matrix[top][col])
            top += 1

           
            for row in range(top, bottom + 1):
                results.append(matrix[row][right])
            right -=1

            if top <= bottom:    
                for col in range(right, left - 1, -1):
                    results.append(matrix[bottom][col])
                bottom -=1
            if left <= right:
                for row in range(bottom, top  - 1, - 1):
                    results.append(matrix[row][left])
                left +=1
        
        return results                
                
        