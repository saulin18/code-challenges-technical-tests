
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_zeroes = 0
        num_ones = 0
        num_twos = 0
        
        for num in nums:
                if num == 0:
                    num_zeroes +=1
                if num == 1:
                    num_ones +=1
                if num == 2:
                    num_twos +=1
            
        for i in range(len(nums)):
            
            if num_zeroes > 0:
                nums[i] = 0
                num_zeroes -=1
                continue
            
            if num_ones > 0:
                nums[i] = 1
                num_ones -=1
                continue
            
            if num_twos > 0:
                nums[i] = 2
                num_twos -=1
                continue
            
        return nums
                
            
        
        