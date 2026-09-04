# 2856. Minimum Array Length After Pair Removals
# Given an integer array num sorted in non-decreasing order.
# You can perform the following operation any number of times:
#     Choose two indices, i and j, where nums[i] < nums[j].
#     Then, remove the elements at indices i and j from nums. The remaining elements 
# retain their original order, and the array is re-indexed.
# Return the minimum length of nums after applying the operation zero or more times.
# Example 1:
# Input: nums = [1,2,3,4]
# Output: 2
# Explanation:
# Example 2:
# Input: nums = [1,1,2,2,3,3]
# Output: 0
# Explanation:
# Example 3:
# Input: nums = [1000000000,1000000000]
# Output: 2
# Explanation:
# Since both numbers are equal, they cannot be removed.
# Example 4:
# Input: nums = [2,3,4,4,4]
# Output: 1
# Explanation:
# Constraints:

#     1 <= nums.length <= 105
#     1 <= nums[i] <= 109
#     nums is sorted in non-decreasing order.

 
class Solution:
    def minLengthAfterRemovals(self, nums: list[int]) -> int:
         ans = 0
         i = 0
         n = len(nums)
         for j in range(n - n // 2, n):
             if nums[i] < nums[j]:
                ans += 1
                i +=1
         return n - 2 * ans


# class Solution:
#     def minLengthAfterRemovals(self, nums: list[int]) -> int:
       
#          left = 0
#          n = len(nums)
#          right = n // 2 + 1
#          while right - left > 1:
#              mid = (left + right) // 2
#              if self.is_possible(mid, nums, n):
#                 left = mid
#              else:
#                 right = mid
#          return n - 2 * left
     
#     def is_possible(self, mid: int, nums: list[int], n: int) -> bool:
#          for i in range(mid):
#              if nums[i] >= nums[n - mid + i]:
#                 return False
#          return True
         
# class Solution:
#     def minLengthAfterRemovals(self, nums: List[int]) -> int:
#         n = len(nums)
#         i = nums[n // 2]
#         cnt = bisect_right(nums, i) - bisect_left(nums, i)
#         return max(n % 2, 2 * cnt - n)