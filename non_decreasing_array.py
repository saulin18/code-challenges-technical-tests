# 665. Non-decreasing Array
# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
# Example 1:
# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:
# Input: nums = [4,2,1]
# Output: false
# Explanation: You cannot get a non-decreasing array by modifying at most one element.
# Constraints:
# n == nums.length
# 1 <= n <= 104
# -105 <= nums[i] <= 105

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        number_of_peaks = 0
        index_of_peak = None

        for index in range(0, len(nums) - 1):
            num = nums[index]
            next_num = nums[index + 1]

            if num > next_num:
                number_of_peaks += 1
                index_of_peak = index
                if number_of_peaks > 1:
                    return False
        
        # base case, if there are no peaks, return True
        if index_of_peak is None:
            return True   
        
        # base case, if the peak is the first or the element in the middle return True
        # example: [1,3,2], [4,2,3]
        if index_of_peak == 0 or index == len(nums) - 2:
            return True   
            
        # if the peak is not the first or the element in the middle, we need to check if the 
        # previous and next elements are in the correct order
        if (
            index_of_peak < len(nums) - 2 and
            (nums[index_of_peak - 1] <= nums[index_of_peak + 1]
            or nums[index_of_peak] <= nums[index_of_peak + 2])
        ):
            return True
        
        return False
        
Solution().checkPossibility([1,3,2])
