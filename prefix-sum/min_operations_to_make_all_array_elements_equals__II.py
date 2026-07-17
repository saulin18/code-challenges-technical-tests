# Given an integer array nums of size n, return the minimum number of moves required to make all array 
# elements equal.
# In one move, you can increment or decrement an element of the array
# by 1.
# Test cases are designed so that the answer will fit in a 32-bit integer.
# Example 1:
# Input: nums = [1,2,3]
# Output: 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
# Example 2:
# Input: nums = [1,10,2,9]
# Output: 16
# Constraints:
#     n == nums.length
#     1 <= nums.length <= 105
#     -109 <= nums[i] <= 109
# from typing import List
# class Solution:
#     def minMoves2(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         prefix_sum = [0] * (n + 1)
#         min_moves = float("inf")

#         for i in range(n):
#             prefix_sum[i + 1] = prefix_sum[i] + nums[i]

#         for i in range(n):
#             num = nums[i]
#             count = i * num
#             left_prefix = prefix_sum[i]
#             right_sum = prefix_sum[n] - prefix_sum[i + 1]
#             right_count = n - i - 1
#             cost = count - left_prefix + right_sum - (right_count * num)
#             min_moves = min(min_moves, cost )

#         return min_moves
# class Solution:
#     def minMoves2(self, nums: List[int]) -> int:
#         nums.sort()
#         ops = 0 
#         median = nums[len(nums)//2] 
#         for i in nums: 
#             ops += abs(i-median) 
#         return ops