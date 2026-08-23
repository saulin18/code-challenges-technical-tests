# 354. Russian Doll Envelopes
# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

# One envelope can fit into another if and only if both the width and height of one envelope are greater than the
# other envelope's width and height.
# Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).
# Note: You cannot rotate an envelope.
# Example 1:
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
# Example 2:
# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
# Constraints:
#     1 <= envelopes.length <= 105
#     envelopes[i].length == 2
#     1 <= wi, hi <= 105


from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [envelopes[0][1]]
        n = len(envelopes)
        for i in range(1, n):
            _, height  = envelopes[i]

            if height > dp[-1]:
                dp.append(height)
                continue
            index = bisect_left(dp, height)
            dp[index] = height

        return len(dp)


# class Solution:
#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         envelopes.sort(key=lambda envelopes:(envelopes[0],-envelopes[1]))

#         tails = []

#         for width, height in envelopes:
#             index = bisect_left(tails, height)

#             if index == len(tails):
#                 tails.append(height)
#             else:
#                 tails[index] = height

        
#         return len(tails)







