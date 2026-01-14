##Easy
#674. Longest Continuous Increasing Subsequence

#Given an unsorted array of integers nums, return the length of the longest continuous 
# increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.#
#
#A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is
# [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].#

#Example 1:
##Output: 3
#Input: nums = [1,3,5,4,7]
##Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements
# 5 and 7 are separated by element
#Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.


def findLengthOfLCIS(self, nums: list[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_length = 0
        
        actual_length = 1
        i = 0
        while i < len(nums) - 1:
            if i == 0:
                actual_length = 1
                max_length = 1
                i += 1
                continue
            
            if(nums[i] > nums[i - 1]):
                actual_length +=1
                max_length = max(max_length, actual_length)
            else:    
                actual_length = 1
            
            i+=1    
              
            
            