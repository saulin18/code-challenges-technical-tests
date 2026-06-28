# 2587. Rearrange Array to Maximize Prefix Score
# You are given a 0-indexed integer array nums. You can rearrange the elements of nums
#  to any order (including the given order).

# Let prefix be the array containing the prefix sums of nums after rearranging it.
# In other words, prefix[i] is the sum of the elements from 0 to i in nums after
# rearranging it. The score of nums is the number of positive integers in the array prefix.
# Return the maximum score you can achieve.
# Example 1:
# Input: nums = [2,-1,0,1,-3,3,-3]
# Output: 6
# Explanation: We can rearrange the array into nums = [2,3,1,-1,-3,0,-3].
# prefix = [2,5,6,5,2,2,-1], so the score is 6.
# It can be shown that 6 is the maximum score we can obtain.
# Example 2:
# Input: nums = [-2,-3,0]
# Output: 0
# Explanation: Any rearrangement of the array will result in a score of 0.
# Constraints:

# 1 <= nums.length <= 105
# -106 <= nums[i] <= 106

from typing import List
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        def calculate_importance(element: int) -> int:
            if element <= 0:
                return -100 + element
            return element

        prefix_sum_arr = [0] * n
        nums.sort(key=lambda element: -calculate_importance(element))
        num_of_positives = 0
        for i in range(n):
            prefix_sum_arr[i] = prefix_sum_arr[i - 1] + nums[i]
            if prefix_sum_arr[i] > 0:
                num_of_positives += 1

        return num_of_positives

# class Solution:
#     def maxScore(self, nums: List[int]) -> int:
#         nums.sort(reverse=True)

#         #score = 0
#         total = 0
#         for i, n in enumerate(nums):
#             total += n
#             if total <= 0:
#                 return i
#             #if total:
#                 #score += 1
#         return len(nums)
#         #return score

# class Solution:
#     def maxScore(self, nums: List[int]) -> int:
#         positives = [num for num in nums if num > 0]
#         nonPositives = [num for num in nums if num <= 0]
#         arr = positives + sorted(nonPositives, reverse=True)
#         output = 0
#         s = 0
#         for num in arr:
#             s += num
#             if s > 0:
#                 output += 1

#         return output
        