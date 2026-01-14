# 169. Majority Element
# Easy
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
# The input is generated such that a majority element will exist in the array.

# Follow-up: Could you solve the problem in linear time and in O(1) space?


#class Solution(object):
#    def majorityElement(self, nums):
#        # First a simple approach O(n) space and time
#
#        hashmap = {}
#
#        for num in nums:
#            if hashmap.get(num) is None:
#                hashmap[num] = 0
#            else:
#                hashmap[num] += 1
#            
#            if hashmap[num] >= len(nums) // 2:
#                return num
#        print(hashmap)
#        return None     
   
def majorityElement(nums):
    
    # Now we use a O(1) space approach using Boyer-Moore Voting Algorithm
    
    count = 0
    # In this case the candidate will be our number
    candidate = 0
    
    for i in range(len(nums)):
        if count == 0:
            candidate = nums[i]
        if nums[i] == candidate:
            count += 1   
        else:
            count -= 1  
 
    return candidate    

majorityElement([2, 2, 1, 1, 1, 2, 2])