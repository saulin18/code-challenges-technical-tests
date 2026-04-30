# 2915. Length of the Longest Subsequence That ss to Target
# You are given a 0-indexed array of integers nums, and an integer target.
# Return the length of the longest subsequence of nums that ss up to target.
# If no such subsequence exists, return -1.
# A subsequence is an array that can be derived from another array by deleting
# some or no elements without changing the order of the remaining elements.

# Example 1:
# Input: nums = [1,2,3,4,5], target = 9
# Output: 3
# Explanation: There are 3 subsequences with a s equal to 9: [4,5], [1,3,5],
# and [2,3,4]. The longest subsequences are [1,3,5], and [2,3,4]. Hence, the answer is 3.
# Example 2:

# Input: nums = [4,1,3,2,1,5], target = 7
# Output: 4
# Explanation: There are 5 subsequences with a s equal to 7: [4,3],
# [4,1,2], [4,2,1], [1,1,5], and [1,3,2,1]. The longest subsequence is [1,3,2,1]. Hence, the answer is 4.
# Example 3:

# Input: nums = [1,1,5,4,5], target = 3
# Output: -1
# Explanation: It can be shown that nums
# has no subsequence that ss up to 3.
# Constraints:
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
# 1 <= target <= 1000


# from typing import List
# TLE
# class Solution:
#     def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:

#         N = len(nums)
#         def recursive(
#             index: int, curr_s: int, memo: dict, number_of_elements: int
#         ) -> int:

#             if curr_s == target:
#                 memo[(index, curr_s)] = 0
#                 return 0

#             if index == N and curr_s != target:
#                 memo[(index, curr_s)] = -1
#                 return -1

#             # INVALID BRANCH
#             if curr_s > target:
#                 memo[(index, curr_s)] = -1
#                 return -1

#             if (index, curr_s) in memo:
#                 return memo[(index, curr_s)]

#             without_element = recursive(
#                 index + 1, curr_s, memo, number_of_elements
#             )

#             with_element = recursive(
#                 index + 1, curr_s + nums[index], memo, number_of_elements + 1
#             )

#             memo[(index, curr_s)] = max(
#                 with_element + 1 if with_element != -1 else with_element, without_element
#             )

#             return memo[(index, curr_s)]

#         res = recursive(0, 0, {}, 0)

#         return res if res > 0 else -1

from typing import List


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:

        N = len(nums)
        dp = [[-1 for _ in range(target + 1)] for _ in range(N + 1)]
        dp[0][0] = 0

        for i in range(N + 1):
            dp[i][0] = 0
        for index in range(1, N + 1):
            for s in range(1, target + 1):
                if s < nums[index - 1]:
                    dp[index][s] = dp[index - 1][s]
                else:
                    dp[index][s] = max(
                        dp[index - 1][s],
                        (
                            dp[index - 1][s - nums[index - 1]] + 1
                            if dp[index - 1][s - nums[index - 1]] != -1
                            else -1
                        ),
                    )
        return dp[N][target] if dp[N][target] > 0 else -1



def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:

    dp = [-1 for _ in range(target + 1)]
    dp[0] = 0
    for x in nums:
        for s in range(target, x - 1, -1):
            if dp[s - x] != -1:
                dp[s] = max(dp[s], dp[s - x] + 1)
    return dp[target] if dp[target] != -1 else -1
