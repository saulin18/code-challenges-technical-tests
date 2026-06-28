from typing import List


class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum_arr = [0] * n
        suffix_min_arr = [float("inf")] * n
        res = float("-inf")

        # Compute prefix sum
        prefix_sum_arr[0] = nums[0]
        for i in range(1, n):
            prefix_sum_arr[i] = prefix_sum_arr[i - 1] + nums[i]

        # Compute suffix min

        for i in range(n - 2, -1, -1):
            suffix_min_arr[i] = min(suffix_min_arr[i + 1], nums[i + 1])

        for i in range(n - 1):
            score = prefix_sum_arr[i] - suffix_min_arr[i]
            res = max(res, score)
        return int(res) if res != float("-inf") else 0
