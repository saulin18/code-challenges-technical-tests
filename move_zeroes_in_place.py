# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining 
# the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
# Constraints:
#     1 <= nums.length <= 104
#     -231 <= nums[i] <= 231 - 1
# Follow up: Could you minimize the total number of operations done?

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
       
       n = len(nums)
       count_of_zeroes = 0

    #    if nums[0] == 0:
    #         count_of_zeroes +=1
    #         nums.pop(0) if n > 1 else None
       if n == 1:
        return
       i = 0
       
       write_index = 0
       for read_index in range(n):
           if nums[read_index] != 0:
               nums[write_index] = nums[read_index]
               write_index += 1
       for i in range(write_index, n):
            nums[i] = 0
    
      
        