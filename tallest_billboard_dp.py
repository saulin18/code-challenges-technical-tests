# 956. Tallest Billboard
# You are installing a billboard and want it to have
# the largest height. The billboard will have two steel
# supports, one on each side. Each steel support must be an equal height.
# You are given a collection of rods that can be
# welded together. For example,
# if you have rods of lengths 1, 2, and 3, you
# can weld them together to make a support of length 6.
# Return the largest possible height of your billboard installation.
# If you cannot support the billboard, return 0.
# Example 1:
# Input: rods = [1,2,3,6]
# Output: 6
# Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
# Example 2:
# Input: rods = [1,2,3,4,5,6]
# Output: 10
# Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
# Example 3:
# Input: rods = [1,2]
# Output: 0
# Explanation: The billboard cannot be supported, so we return 0.
# Constraints:

# 1 <= rods.length <= 20
# 1 <= rods[i] <= 1000
# sum(rods[i]) <= 5000

from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        neg = float("-inf")
        memo: dict[tuple[int, int], int] = {}

        def recursive(i: int, diff: int, memo: dict) -> int:
            if i == n:
                return 0 if diff == 0 else neg

            if (i, diff) in memo:
                return memo[(i, diff)]

            option1 = recursive(i + 1, diff, memo)

            option2 = recursive(i + 1, diff + rods[i], memo)

            option3 = recursive(i + 1, diff - rods[i], memo)

            memo[(i, diff)] = max(option1, option2, option3)
            return memo[(i, diff)]

        return recursive(0, 0, 0, memo)
