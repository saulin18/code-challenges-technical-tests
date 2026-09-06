# 3904. Smallest Stable Index II
# You are given an integer array nums of length n and an integer k.
# For each index i, define its instability score as max(nums[0..i]) - min(nums[i..n - 1]).
# In other words:
#     max(nums[0..i]) is the largest value among the elements from index 0 to index i.
#     min(nums[i..n - 1]) is the smallest value among the elements from index i to index n - 1.
# An index i is called stable if its instability score is less than or equal to k.
# Return the smallest stable index. If no such index exists, return -1.
# Example 1:
# Input: nums = [5,0,1,4], k = 3
# Output: 3
# Explanation:
#     At index 0: The maximum in [5] is 5, and the minimum in [5, 0, 1, 4] is 0, so the instability score is 5 - 0 = 5.
#     At index 1: The maximum in [5, 0] is 5, and the minimum in [0, 1, 4] is 0, so the instability score is 5 - 0 = 5.
#     At index 2: The maximum in [5, 0, 1] is 5, and the minimum in [1, 4] is 1, so the instability score is 5 - 1 = 4.
#     At index 3: The maximum in [5, 0, 1, 4] is 5, and the minimum in [4] is 4, so the instability score is 5 - 4 = 1.
#     This is the first index with an instability score less than or equal to k = 3. Thus, the answer is 3.
# Example 2:
# Input: nums = [3,2,1], k = 1
# Output: -1
# Explanation:
#     At index 0, the instability score is 3 - 1 = 2.
#     At index 1, the instability score is 3 - 1 = 2.
#     At index 2, the instability score is 3 - 1 = 2.
#     None of these values is less than or equal to k = 1, so the answer is -1.
# Example 3:
# Input: nums = [0], k = 0
# Output: 0
# Explanation:
# At index 0, the instability score is 0 - 0 = 0, which is less than or equal to k = 0. Therefore, the answer is 0.
# Constraints:
#     1 <= nums.length <= 105
#     0 <= nums[i] <= 109
#     0 <= k <= 109

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_max = [0] * (n + 1)
        suffix_min = [0] * (n + 1)
        prefix_max[0] = nums[0]
        suffix_min[n - 1] = nums[n - 1]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])
            suffix_min[n - i - 1] = min(suffix_min[n - i], nums[n - i - 1])
        for i in range(n):
            if prefix_max[i] - suffix_min[i] <= k:
                return i
        return -1
    
    
# class Solution:
#     def firstStableIndex(self, nums: list[int], k: int) -> int:
#         min_arr = [nums[-1]] * len(nums)
#         for i in range(len(nums) - 2, -1, -1):
#             min_arr[i] = min(nums[i], min_arr[i + 1])
#         max_from_left = float('-inf')
#         for i, num in enumerate(nums):
#             max_from_left = max(max_from_left, num)
#             min_from_right = min_arr[i]
#             if max_from_left - min_from_right <= k:
#                 return i
#         return -1