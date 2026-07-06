# from typing import List


# 2602. Minimum Operations to Make All Array Elements Equal
# You are given an array nums consisting of positive integers.
# You are also given an integer array queries of size m. For the ith query, you want to make all of the elements of 
# nums equal to queries[i]. You can perform the following operation on the array any number of times:
# Increase or decrease an element of the array by 1.
# Return an array answer of size m where answer[i] is the minimum number of operations to make all 
# elements of nums equal to queries[i].
# Note that after each query the array is reset to its original state.
# Example 1:
# Input: nums = [3,1,6,8], queries = [1,5]
# Output: [14,10]
# Explanation: For the first query we can do the following operations:
# - Decrease nums[0] 2 times, so that nums = [1,1,6,8].
# - Decrease nums[2] 5 times, so that nums = [1,1,1,8].
# - Decrease nums[3] 7 times, so that nums = [1,1,1,1].
# So the total number of operations for the first query is 2 + 5 + 7 = 14.
# For the second query we can do the following operations:
# - Increase nums[0] 2 times, so that nums = [5,1,6,8].
# - Increase nums[1] 4 times, so that nums = [5,5,6,8].
# - Decrease nums[2] 1 time, so that nums = [5,5,5,8].
# - Decrease nums[3] 3 times, so that nums = [5,5,5,5].
# So the total number of operations for the second query is 2 + 4 + 1 + 3 = 10.
# Example 2:
# Input: nums = [2,9,6,3], queries = [10]
# Output: [20]
# Explanation: We can increase each value in the array to 10. The total number of operations will be 8 + 1 + 4 + 7 = 20.
# Constraints:
#     n == nums.length
#     m == queries.length
#     1 <= n, m <= 105
    # 1 <= nums[i], queries[i] <= 109
    
    
import bisect
from typing import List
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        queries_length = len(queries)
        prefix_sum = [0] * (n + 1)
        prefix_sum[1] = nums[0]
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        ans = [0] * queries_length
        for i in range(queries_length):
            index = bisect.bisect_left(nums, queries[i])
            # 3 5 6 8 9
            # 45 - 31  
            left_sum = prefix_sum[index]
            left_count = index * queries[i] 
            right_sum = prefix_sum[n] - left_sum 
            right_count = n - index 

            ans[i] = (left_count - left_sum) + right_sum - (right_count * queries[i])

        return ans
    
    
from bisect import bisect_left
from itertools import accumulate
from typing import List


# class Solution:
#     def minOperations(
#         self,
#         nums: List[int],
#         queries: List[int]
#     ) -> List[int]:

#         nums.sort()

#         n = len(nums)

#         # prefix[i] = sum of nums[0:i]
#         prefix = [0] + list(accumulate(nums))

#         ans = []

#         total_sum = prefix[-1]

#         for q in queries:

#             # first index with value >= q
#             idx = bisect_left(nums, q)

#             # left side
#             left_count = idx
#             left_sum = prefix[idx]

#             left_cost = q * left_count - left_sum

#             # right side
#             right_count = n - idx
#             right_sum = total_sum - prefix[idx]

#             right_cost = right_sum - q * right_count

#             ans.append(left_cost + right_cost)

#         return ans


# import bisect
# from bisect import bisect_right
# from typing import List

# class Solution:
#     def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
#         nums.sort()
#         n = len(nums)
#         prefix = [0] * (n + 1)
#         for i in range(n):
#             prefix[i + 1] = prefix[i] + nums[i]
#         res = []
#         for q in queries:
#             idx = bisect_right(nums, q)
#             left_sum = prefix[idx]
#             right_sum = prefix[n] - prefix[idx]
#             left_cnt = idx
#             right_cnt = n - idx
#             ops = q * left_cnt - left_sum + right_sum - q * right_cnt
#             res.append(ops)
#         return res

        

