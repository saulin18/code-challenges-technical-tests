# 1437. Check If All 1's Are at Least Length K Places Away
# Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, 
# otherwise return false.
# Example 1:
# Input: nums = [1,0,0,0,1,0,0,1], k = 2
# Output: true
# Explanation: Each of the 1s are at least 2 places away from each other.
# Example 2:
# Input: nums = [1,0,0,1,0,1], k = 2
# Output: false
# Explanation: The second 1 and third 1 are only one apart from each other.
# Constraints:
#     1 <= nums.length <= 105
#     0 <= k <= nums.length
#     nums[i] is 0 or 1

 

 
class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:

        last_one_distance = 999

        for i in range(len(nums)):
            if nums[i] == 1 and last_one_distance == 999:
                last_one_distance = 0
                continue


            if nums[i] == 1 and last_one_distance != 999:

                if last_one_distance < k:
                    return False
                else: 
                    last_one_distance = 0
                    continue

               
            last_one_distance +=1

        return True
            
        
    from typing import List

# class Solution:
#     def kLengthApart(self, nums: List[int], k: int) -> bool:
#         prev = -1
#         for i, v in enumerate(nums):
#             if v == 1:
#                 if prev != -1 and i - prev <= k:
#                     return False
#                 prev = i
#         return True