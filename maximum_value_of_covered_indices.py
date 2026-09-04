# 3952. Maximum Total Value of Covered Indices
# You are given an integer array nums of length n and a binary string s of length n,
# where s[i] == '1' means index i initially contains a token and s[i] == '0' means it does not.
# You may perform the following operation any number of times:
#     Choose a token currently located at index i, where i > 0, such that this token has not been moved before.
#     Move this token from index i to index i - 1.
# An index is considered covered if it contains a token after all moves.
# Return an integer denoting the maximum total value of nums at the covered indices after optimally performing the operations.
# Example 1:
# Input: nums = [9,2,6,1], s = "0101"
# Output: 15
# Explanation:
#     Initially, indices 1 and 3 contain tokens.
#     Move the token from index 3 to index 2.
#     Move the token from index 1 to index 0.
#     The covered indices are [0, 2], so the total value is nums[0] + nums[2] = 9 + 6 = 15.
# Example 2:
# Input: nums = [5,1,4], s = "001"
# Output: 4
# Explanation:
#     Initially, only index 2 contains a token.
#     It is optimal to leave the token at index 2.
#     The covered index is [2], so the total value is nums[2] = 4.
# Example 3:
# Input: nums = [9,3,5], s = "011"
# Output: 14
# Explanation:
#     Initially, indices 1 and 2 contain tokens.
#     Move the token from index 1 to index 0.
#     The covered indices are [0, 2], so the total value is nums[0] + nums[2] = 9 + 5 = 14.
# Constraints:
#     1 <= n == nums.length == s.length <= 105
#     1 <= nums[i] <= 105
#     ​​​​​​​s[i] is either '0' or '1'


from typing import List


class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        ans = 0
        start_of_block = None

        for i in range(len(nums)):
            if s[i] == "1":
                if start_of_block is None:
                    start_of_block = i
            elif start_of_block is not None:
                ans += self._block_value(nums, start_of_block, i)
                start_of_block = None

        if start_of_block is not None:
            ans += self._block_value(nums, start_of_block, len(nums))

        return ans

    def _block_value(self, nums: List[int], start: int, end: int) -> int:
     
        if start == 0:
            return sum(nums[start:end])

        window = nums[start - 1 : end]
        return sum(window) - min(window)


# class Solution:
#     def maxTotal(self, nums: List[int], s: str) -> int:
#         i = 0
#         prefix_sum = [0]
#         for num in nums:
#             prefix_sum.append(prefix_sum[-1] + num)
#
#         ans = 0
#         while i < len(nums):
#             if s[i] == "0":
#                 i += 1
#                 continue
#             j = i
#             while j < len(nums) and s[j] == "1":
#                 j += 1
#
#             if i == 0:
#                 ans += prefix_sum[j] - prefix_sum[i]
#             else:
#                 window = nums[i - 1 : j]
#                 min_value = min(window)
#                 ans += (prefix_sum[j] - prefix_sum[i - 1]) - min_value
#             i = j
#         return ans
