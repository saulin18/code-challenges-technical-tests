# Maximum subarray sum
# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in
# an array or list of integers:
# For example:
# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6 (Sum of [4, -1, 2, 1])
# Easy case is when the list is made up of only positive numbers and the maximum
# sum is the sum of the whole array. If the list is made up of only negative numbers, 
# return 0 instead. Your solution should be fast, 
# it will be tested on very large arrays so slow solutions will time out.
# Empty list is considered to have zero greatest sum. Note that the empty 
# list or array is also a valid sublist/subarray.

from collections import defaultdict
from typing import List


def max_sequence(arr: List[int]) -> int:
    dp = [0 for _ in range(len(arr) + 1)]
    
    for i, num in enumerate(arr):
        dp[i] = max(dp[i - 1] + num, num)
    return max(dp)

def max_length_sub_array_doesnt_exceed_sum(arr: List[int], sum: int) -> int:
    # The elements in the window cannot be repeated
    freq = defaultdict(int)

    start = 0
    wsum = 0
    max_length = 0
    for end in range(len(arr)):
        freq[arr[end]] += 1
        wsum += arr[end] if freq[arr[end]] == 1 else 0
        while wsum > sum:
            freq[arr[start]] -= 1
            wsum -= arr[start] if freq[arr[start]] == 0 else 0
            start += 1
        max_length = max(max_length, end - start + 1)
    return max_length
