
# 55. Jump Game
# Medium
# You are given an integer array nums. You are initially positioned 
# at the array's first index, and each element in the array represents
# your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.
# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, 
# which makes it impossible to reach the last index.
# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

# from typing import List

# class Solution:TLE
#     def canJump(self, nums: List[int]) -> bool:
    
#         def recursive(index: int, memo: dict) -> int:
            
#             if index in memo:
#                 return memo[index]

#             if index > len(nums) - 1:
#                 memo[index] = True
#                 return True
            
#             max_distance_at_curr = nums[index]
            
#             if index == len(nums) - 1:
#                 memo[index] = True
#                 return True
                
#             if max_distance_at_curr == 0 and index != len(nums) - 1:
#                memo[index] = False
#                return memo[index]
            
            
#             for step in range(1, max_distance_at_curr + 1):
#                 acumm_value = memo.get(index, False)
      
#                 if acumm_value:
#                     return True

#                 new_ans = acumm_value or recursive(index + step, memo)
#                 if new_ans:
#                     return True
                
#             return False
        
#         return recursive(0, {})
        
        

from typing import List


# class Solution: TLE 
#     def canJump(self, nums: List[int]) -> bool:  
#        N = len(nums)
#        dp = [False] * N
#        dp[0] = True
#        for i in range(1, N):
#         for j in range(i):
#             if dp[j] and j + nums[j] >= i:
#                 dp[i] = True
#                 break
#        return dp[N - 1]

class Solution:
     # GREEDY APPROACH
     def canJump(self, nums: List[int]) -> bool:  
        N = len(nums)
        max_reachable = 0
        for i in range(N):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + nums[i])
            if max_reachable >= N - 1:
                return True
        return False