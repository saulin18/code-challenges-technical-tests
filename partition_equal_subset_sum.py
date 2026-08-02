# 416. Partition Equal Subset Sum
# Given an integer array nums, return true if you can partition the array into
# two subsets such that the sum of the elements in both subsets is equal or
# false otherwise.
# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
# Constraints:
#     1 <= nums.length <= 200
#     1 <= nums[i] <= 100
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_of_nums = sum(nums) 

        if sum_of_nums % 2 != 0:
            return False

        target = sum_of_nums // 2
        n = len(nums)
        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(1, n + 1):
         for j in range(target, -1, -1):
            num = nums[i - 1]

            if j >= num:
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]
    
    
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total_sum = sum(nums)

#         # If sum is odd, we cannot divide it into two equal subsets
#         if total_sum % 2 != 0:
#             return False

#         target = total_sum // 2

#         @cache
#         def canFindSum(idx: int, rem: int) -> bool:
#             if rem == 0:
#                 return True
#             if idx >= len(nums) or rem < 0:
#                 return False

#             # Decision 1: Include nums[idx], Decision 2: Exclude nums[idx]
#             return canFindSum(idx + 1, rem - nums[idx]) or canFindSum(idx + 1, rem)

#         return canFindSum(0, target)
                
                


            




        