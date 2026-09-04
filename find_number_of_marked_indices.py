# 2576. Find the Maximum Number of Marked Indices
# You are given a 0-indexed integer array nums.
# Initially, all of the indices are unmarked. You are allowed to make this operation
# any number of times:
#     
# Pick two different unmarked indices i and j such that 2 * nums[i] <= nums[j], then mark i and j.
# Return the maximum possible number of marked indices in nums using the 
# above operation any number of times.
# Example 1:
# Input: nums = [3,5,2,4]
# Output: 2
# Explanation: In the first operation: pick i = 2 and j = 1, the operation is 
# allowed because 2 * nums[2] <= nums[1]. Then mark index 2 and 1.
# It can be shown that there's no other valid operation so the answer is 2.
# Example 2:
# Input: nums = [9,2,5,4]
# Output: 4
# Explanation: In the first operation: pick i = 3 and j = 0, the operation is
# allowed because 2 * nums[3] <= nums[0]. Then mark index 3 and 0.
# In the second operation: pick i = 1 and j = 2, the operation is 
# allowed because 2 * nums[1] <= nums[2]. Then mark index 1 and 2.
# Since there is no other operation, the answer is 4.
# Example 3:
# Input: nums = [7,6,8]
# Output: 0
# Explanation: There is no valid operation to do, so the answer is 0.
# Constraints:
#     1 <= nums.length <= 105
#     1 <= nums[i] <= 109



# class Solution:
#     def maxNumOfMarkedIndices(self, nums: list[int]) -> int:
#         nums.sort()
#         left = 0
#         k = 0
#         n = len(nums)
#         right = n // 2 + 1
#         while left < right: 
#             mid = left + (right - left) // 2
            
#             if self._is_possible(0, mid, n, nums, k):
#                 left = mid
#                 k = mid
#             else:
#                 right = mid
            
#         return k * 2
#     def _is_possible(self, k: int, mid: int, n: int, nums: list[int], actual_k: int) -> bool:
       
      
#         for i in range(mid):
#             if nums[i] * 2 <= nums[n - mid + i]:
#                 k += 1
#             else:
#                 return False
#         return True




class Solution:
    def maxNumOfMarkedIndices(self, nums: list[int]) -> int:
        nums.sort()
        left = 0
        count = 0
        right = (len(nums) + 1) // 2

        while right < len(nums):
            if nums[left] * 2 <= nums[right]:
                count += 1
                left += 1
         
            right += 1
        return count * 2
    
    
# # Time:  O(nlogn)
# # Space: O(1)

# # sort, greedy, two pointers
# class Solution(object):
#     def maxNumOfMarkedIndices(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         left = 0
#         for right in range((len(nums)+1)//2, len(nums)):
#             if nums[right] >= 2*nums[left]:
#                 left += 1
#         return left*2


# # Time:  O(nlogn)
# # Space: O(1)
# # sort, greedy, two pointers
# class Solution2(object):
#     def maxNumOfMarkedIndices(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         left = 0
#         for right in range(len(nums)):
#             if nums[right] >= 2*nums[left]:
#                 left += 1
#         return min(left, len(nums)//2)*2