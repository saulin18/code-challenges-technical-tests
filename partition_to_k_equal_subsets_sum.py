# 698. Partition to K Equal Sum Subsets
# Given an integer array nums and an integer k, return true if it is possible to divide 
# this array into k non-empty subsets whose sums are all equal.
# Example 1:
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
# Example 2
# Input: nums = [1,2,3,4], k = 3
# Output: false


from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target = total_sum // k
        
        seen = [False] * len(nums)
        
        # if any(num > target for num in nums):
        #     return False
        
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        def backtrack(index: int, current_sum: int, 
                       subsets: int) -> bool:
            if subsets == k:
                return True
        
            if current_sum == target:
                return backtrack(0, 0, subsets + 1)
            
            for i in range(index, len(nums)):
                if seen[i] or current_sum + nums[i] > target:
                    continue
                seen[i] = True
                if backtrack(i + 1, current_sum + nums[i], subsets):
                    return True
                seen[i] = False
            return False
        return backtrack(0, 0, 0)
