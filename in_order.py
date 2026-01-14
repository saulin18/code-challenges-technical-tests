
#Given an integer array nums, find the subarray with the largest sum, and return its sum.
#Example 1:
#
#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#Example 2:
#
#Input: nums = [1]
#Output: 1
#Explanation: The subarray [1] has the largest sum 1.
#Example 3:
#
#Input: nums = [5,4,-1,7,8]
#Output: 23
#Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#Constraints:
#1 <= nums.length <= 105
#-104 <= nums[i] <= 104
#Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# Using the kadane algorithm
def maxSubArray(nums):
    
    max_current = 0
    max_global = float('-inf')
    
    for i, number in enumerate(nums):
        max_current += number
        
        if max_current > max_global:
            max_global = max_current
            
        if max_current < 0:
            max_current = 0
    
    return max_global

# Using a divide and conquer approach with recursion
# sum
def maxSubArray(nums: list[int]) -> int:
    
    length_of_each_sub_array = len(nums) // 2
    
    def calc_arr_sum_recursively(arr: list[int], stop: int, max_current: int, max_global: int, index: int) -> int:
        
        if index == stop:
            return max_global
        
        max_current += arr[index]
        
        if max_current > max_global:
            max_global = max_current
            
        if max_current < 0:
            max_current = 0
            
        return calc_arr_sum_recursively(arr, stop, max_current, max_global, index + 1)
    
    left_sub_array_sum = calc_arr_sum_recursively(nums, length_of_each_sub_array, 0, float('-inf'), 0)
    right_sub_array_sum = calc_arr_sum_recursively(nums[length_of_each_sub_array:], len(nums) - length_of_each_sub_array, 0, float('-inf'), 0)
        
    max_sum = max(left_sub_array_sum, right_sub_array_sum, left_sub_array_sum + right_sub_array_sum)
    
    return max_sum
        
        