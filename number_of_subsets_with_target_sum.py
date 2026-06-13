# Subsequence Sums
# Given a sequence of integers named arr, find the number of continuous
# subsequences (sublist or subarray) in arr that sum up to s. A continuous
# subsequence can be defined as a sequence inbetween a start index and stop index
# (inclusive) of the sequence. For instance, [2, 3, 4] is a continuous subsequence
# of [1, 2, 3, 4, 5] , but [3, 5] and [4, 1] are not.
# PERFORMANCE REQUIREMENTS
# The length of arr is
# ≤
# ≤ 10,000. The contents of arr can range from -10000 to 10000.
# SAMPLE INPUTS & OUTPUTS
# arr = [1, 2, 3, -3, -2, -1], s = 0 -> 3
# # [3, -3], [2, 3, -3, -2], [1, 2, 3, -3, -2, -1]
# ------------------------------------------------------------
# arr = [1, 5, -2, 4, 0, -7, -3, 6], s = 4 -> 4
# # [1, 5, -2], [4], [4, 0], [1, 5, -2, 4, 0, -7, -3, 6]
# ------------------------------------------------------------
# arr = [9, -2, -5, 8, 6, -10, 0, -4], s = -1 -> 2
# # [-5, 8, 6, -10], [-5, 8, 6, -10, 0]

# from typing import List


# def subsequence_sums(arr: List[int], s: int) -> int:
#     memo = {}
#     N = len(arr)
#     def solve(remainder: int, index: int) -> int:
#         if remainder == 0:
#             memo[(remainder, index)] = 1
#             return memo[(remainder, index)]
#         if remainder < 0:
#             memo[(remainder, index)] = 0
#             return memo[(remainder, index)]
        
#         if memo[(remainder, index)]:
#             return memo[(remainder, index)]
        
#         if index >= N:
#             memo[(remainder, index)] = 0
#             return memo[(remainder, index)]


#         with_element = solve(remainder - arr[index], index + 1)
#         without_element = solve(remainder, index + 1)
#         memo[(remainder, index)] = with_element + without_element

#         return memo[(remainder, index)]
            
#     return solve(s, 0)

from collections import defaultdict
from typing import List


def subsequence_sums(arr: List[int], s: int) -> int:
    prefix_count: dict[int, int] = defaultdict(int)
    prefix_count[0] = 1

    running = 0
    count = 0

    for num in arr:
        running += num
        count += prefix_count[running - s]
        prefix_count[running] += 1

    return count

# from collections import defaultdict
# from itertools import accumulate

# def subsequence_sums(arr, s):
#     res, memo = 0, defaultdict(int)
#     for x in accumulate(arr, initial=0):
#         res += memo[x-s]
#         memo[x] += 1
#     return res

# itertools.accumulate() is a memory‑efficient iterator that applies a binary function cumulatively
# to the elements of an iterable, returning a new iterator with the accumulated results Python+1
# Basic syntax/
# itertools.accumulate(iterable, func=None)
# iterable: The input sequence (list, tuple, set, etc.).
# func (optional): A binary function to apply cumulatively.
# If None, defaults to operator.add (cumulative sum).
