# 2824. Count Pairs Whose Sum is Less than Target
# Given a 0-indexed integer array nums of length n and an integer target, 
# return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
# Example 1:
# Input: nums = [-1,1,2,3,1], target = 2
# Output: 3
# Explanation: There are 3 pairs of indices that satisfy the conditions in the statement:
# - (0, 1) since 0 < 1 and nums[0] + nums[1] = 0 < target
# - (0, 2) since 0 < 2 and nums[0] + nums[2] = 1 < target 
# - (0, 4) since 0 < 4 and nums[0] + nums[4] = 0 < target
# Note that (0, 3) is not counted since nums[0] + nums[3] is not strictly less than the target.
# Example 2:
# Input: nums = [-6,2,5,-2,-7,-1,3], target = -2
# Output: 10
# Explanation: There are 10 pairs of indices that satisfy the conditions in the statement:
# - (0, 1) since 0 < 1 and nums[0] + nums[1] = -4 < target
# - (0, 3) since 0 < 3 and nums[0] + nums[3] = -8 < target
# - (0, 4) since 0 < 4 and nums[0] + nums[4] = -13 < target
# - (0, 5) since 0 < 5 and nums[0] + nums[5] = -7 < target
# - (0, 6) since 0 < 6 and nums[0] + nums[6] = -3 < target
# - (1, 4) since 1 < 4 and nums[1] + nums[4] = -5 < target
# - (3, 4) since 3 < 4 and nums[3] + nums[4] = -9 < target
# - (3, 5) since 3 < 5 and nums[3] + nums[5] = -3 < target
# - (4, 5) since 4 < 5 and nums[4] + nums[5] = -8 < target
# - (4, 6) since 4 < 6 and nums[4] + nums[6] = -4 < target
# Constraints:
# 1 <= nums.length == n <= 50
# -50 <= nums[i], target <= 50

from typing import List

# class Solution:
#     def countPairs(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         left = 0
#         right = len(nums) - 1
#         count = 0
#         while left <= right:
#             # mid = left + (right - left) // 2
            
#             sum = nums[left] + nums[right]
            
#             if sum < target:
#                 count += (right - left)
#                 left +=1
                
#             if sum >= target:
#                 right -=1

#         return count
    
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            # j > i y nums[j] < target - nums[i]
            need = target - nums[i]
            j = Solution.bisect_left(nums, need, i + 1, n)
            ans += j - i - 1
        return ans
    
    def bisect_left(self, nums, target, left, right):
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left