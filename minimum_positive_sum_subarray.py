# 3364. Minimum Positive Sum Subarray
# You are given an integer array nums and two integers l and r. Your task is to find the minimum sum of a subarray whose
#  size is between l and r (inclusive) and whose sum is greater than 0.
# Return the minimum sum of such a subarray. If no such subarray exists, return -1.
# A subarray is a contiguous non-empty sequence of elements within an array.
# Example 1:
# Input: nums = [3, -2, 1, 4], l = 2, r = 3
# Output: 1
# Explanation:
# The subarrays of length between l = 2 and r = 3 where the sum is greater than 0 are:
#     [3, -2] with a sum of 1
#     [1, 4] with a sum of 5
#     [3, -2, 1] with a sum of 2
#     [-2, 1, 4] with a sum of 3
# Out of these, the subarray [3, -2] has a sum of 1, which is the smallest positive sum. Hence, the answer is 1.
# Example 2:
# Input: nums = [-2, 2, -3, 1], l = 2, r = 3
# Output: -1
# Explanation:
# There is no subarray of length between l and r that has a sum greater than 0. So, the answer is -1.
# Example 3:
# Input: nums = [1, 2, 3, 4], l = 2, r = 4
# Output: 3
# Explanation:
# The subarray [1, 2] has a length of 2 and the minimum sum greater than 0. So, the answer is 3.
# Constraints:
# 1 <= nums.length <= 100
# 1 <= l <= r <= nums.length
# -1000 <= nums[i] <= 1000

from sortedcontainers import SortedList
class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        min_sum = float("inf")
        n = len(nums)
        
        for i in range(n):
            total_sum = 0
            if i + l > n - 1:
                continue
            for k in range(i, i + l):
                
                total_sum += nums[k]
            if total_sum > 0:
                min_sum = min(min_sum, total_sum)
                
            for j in range(i + l, i + r):
                if j < n:
                    total_sum += nums[j]
                if total_sum > 0:
                    min_sum = min(min_sum, total_sum)
            
        return int(min_sum) if min_sum != float("inf") else -1
                
                
                
# class Solution2:
#     def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
#         ans = float("inf")
#         q = [0]
#         for n in nums:
#             q.append(q[-1] + n)
#         sl = SortedList()
#         for j in range(l, len(q)):
#             sl.add(q[j - l])
#             if j - r - 1 >= 0:
#                 sl.remove(q[j - r - 1])
#             k =  sl.bisect_left(q[j])
#             if k:
#                 ans = min(ans, q[j] - sl[k - 1])
#         return -1 if ans == float("inf") else ans





        