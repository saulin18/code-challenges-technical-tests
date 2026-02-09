# 1380. Lucky Numbers in a Matrix
# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
# Example 1:
# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 2:
# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 3:
# Input: matrix = [[7,8],[1,2]]
# Output: [7]
# Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= n, m <= 50
# 1 <= matrix[i][j] <= 105.
# All elements in the matrix are distinct.


def luckyNumbers(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    row_number = len(matrix)
    
    def get_min_in_row(row_index: int) -> int:
        min_value = min(matrix[row_index])
        return min_value
    
    def get_max_in_col(col_index: int) -> int:
        max_value = max(matrix[i][col_index] for i in range(row_number))
        return max_value
    
    for i in range(row_number):
        min_in_row = get_min_in_row(i)
        col_index = matrix[i].index(min_in_row)
        max_in_col = get_max_in_col(col_index)
        
        if min_in_row == max_in_col:
            return [min_in_row]