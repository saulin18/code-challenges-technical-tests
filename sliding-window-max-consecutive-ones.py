
#485. Max Consecutive Ones
#Easy
#Topics
#premium lock icon
#Companies
#Hint
#Given a binary array nums, return the maximum number of consecutive 1's in the array.

#Example 1:
#
#Input: nums = [1,1,0,1,1,1]
#Output: 3
#Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
#Example 2:
#
#Input: nums = [1,0,1,1,0,1]
#Output: 2
 
def findMaxConsecutiveOnes(nums):
    
    
    # We can use a sliding-window-approach
    start = 0
    max_length = 0
    current_length = 0
    
    for end in range(len(nums)):
        if nums[end] == 1:
            current_length += 1   
        else:
            start = end + 1
            current_length = 0
            
        max_length = max(max_length, current_length)
        
    return max_length    
       