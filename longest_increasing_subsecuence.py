# 300. Longest Increasing Subsequence
# Given an integer array nums, return the length of the longest
# strictly increasing subsequence.
# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101],
# therefore the length is 4.
# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
# Constraints:
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
# Follow up: Can you come up with an algorithm
# that runs in O(n log(n)) time complexity?


from typing import List


class Solution:
    # TLE
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)

    #     def recursive(index: int, previous: int, memo: dict) -> int:
    #         if index >= n:
    #             return 0

    #         if (index, previous) in memo:
    #             return memo[(index, previous)]

    #         without_current = recursive(index + 1, previous, memo)
    #         with_current = 0
    #         if previous < nums[index]:
    #             with_current = recursive(index + 1, nums[index], memo) + 1

    #         memo[(index, previous)] = max(without_current, with_current)
    #         return memo[(index, previous)]

    #     memo = {}
    #     return recursive(0, float('-inf'), memo)

    # This passes but it's not the best answer. Since we are
    # looking to construct number to number we can use simple binary search
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)

    #     dp = [1] * n

    #     max_length = float("-inf")

    #     for i in range(1, n):
    #         for j in range(0, n):
    #                 if nums[j] < nums[i]:
    #                     dp[i] = max(dp[i], dp[j] + 1)
    #                     max_length = max(max_length, dp[i])

    #     return max_length

    def lengthOfLIS(self, nums: List[int]) -> int:
        sequence = []

        def binary_search_(arr: List[int], target: int) -> int:
            left = 0
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                
                if arr[mid] >= target:
                    right = mid
                    continue
                  

                if arr[mid] <= target:
                     left = mid + 1
                     continue

            return left

        for num in nums:
            if not sequence or sequence[-1] < num:
                sequence.append(num)

            elif sequence[-1] > num:
                index = binary_search_(sequence, num)
                sequence[index] = num

        return len(sequence)

print(
    Solution.lengthOfLIS(
        Solution, [7,7,7,7,7,7,7]
    )
)

print(
    Solution.lengthOfLIS(
        Solution, [0,1,0,3,2,3]
    )
)

print(
    Solution.lengthOfLIS(
        Solution, [10,9,2,5,3,7,101,18]
    )
)
