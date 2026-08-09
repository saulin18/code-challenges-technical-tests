# 2772. Apply Operations to Make All Array Elements Equal to Zero
# You are given a 0-indexed integer array nums and a positive integer k.
# You can apply the following operation on the array any number of times:
#     Choose any subarray of size k from the array and decrease all its elements by 1.
# Return true if you can make all the array elements equal to 0, or false otherwise.
# A subarray is a contiguous non-empty part of an array.
# Example 1:
# Input: nums = [2,2,3,1,1,0], k = 3
# Output: true
# Explanation: We can do the following operations:
# - Choose the subarray [2,2,3]. The resulting array will be nums = [1,1,2,1,1,0].
# - Choose the subarray [2,1,1]. The resulting array will be nums = [1,1,1,0,0,0].
# - Choose the subarray [1,1,1]. The resulting array will be nums = [0,0,0,0,0,0].
# Example 2:
# Input: nums = [1,3,1,1], k = 2
# Output: false
# Explanation: It is not possible to make all the array elements equal to 0.
# Constraints:
#     1 <= k <= nums.length <= 105
#     0 <= nums[i] <= 106

from typing_extensions import List
class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        diff = [0] * (len(nums) + 1)
        for i, v in enumerate(nums):
            if i: diff[i] += diff[i - 1]
            v += diff[i]
            # if diff[i] + v == 0:
            #     continue
            if v == 0: continue
            if v < 0: return False
          
            if i + k > len(nums): return False
            diff[i] -= v
            diff[i + k] += v
        return True



# class Solution:
#     def checkArray(self, nums: List[int], k: int) -> bool:
#         n = len(nums)

#         diff = [0] * (n + 1)

#         active = 0
#         for i in range(0, n):
#             active += diff[i]

#             effective = nums[i] - active

#             if effective > 0:
#                 if i + k > n:
#                     return False
#                 active += effective
#                 diff[i + k] -= effective
#             elif effective < 0:
#                 return False
        
#         return True


# class Solution:
#     def checkArray(self, nums: List[int], k: int) -> bool:
#         # pick k, and reduce k consecutive integers by 1
#         # [2,2,3,0,0]
#         # At any time for operation to work, you need to start with max value, and need to reduce 
#         # starting at first element, decrease next k values by 1, and if any number becomes negative that is a failure.
#         n = len(nums)

#         # diff[i] tells us how much decrement effect starts/ends here
#         diff = [0] * (n + 1)

#         current_decrement = 0

#         for i in range(n):
#             # Apply any decrement effects ending/starting here
#             current_decrement += diff[i]

#             # What value remains at this index after previous operations?
#             remaining = nums[i] - current_decrement

#             if remaining < 0:
#                 return False

#             if remaining > 0:
#                 # Need to start 'remaining' operations here
#                 if i + k > n:
#                     return False

#                 current_decrement += remaining
#                 diff[i + k] -= remaining

#         return True