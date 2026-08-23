# 646. Maximum Length of Pair Chain
# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
# Return the length longest chain which can be formed.
# You do not need to use up all the given intervals. You can select pairs in any order.
# Example 1:
# Input: pairs = [[1,2],[2,3],[3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4].
# Example 2:
# Input: pairs = [[1,2],[7,8],[4,5]]
# Output: 3
# Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
# Constraints:
#     n == pairs.length
#     1 <= n <= 1000
#     -1000 <= lefti < righti <= 1000
from functools import cache
class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        res = 1
        n = len(pairs)
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        initial_start, initial_end = sorted_pairs[0][0], sorted_pairs[0][1]

        for index_of_interval in range(1, n ):
            start, end = sorted_pairs[index_of_interval][0], sorted_pairs[index_of_interval][1]

            if initial_end < start:
                res +=1
                initial_start = start
                initial_end = end
                
        return res


# class Solution:
#     def findLongestChain(self, pairs: List[List[int]]) -> int:
#         """
#         Sort pairs
#         """
#         pairs.sort()
#         n = len(pairs)

#         dp = [0] * (n + 1)
#         dp[-2] = 1
#         for i in range(n - 2, -1, -1):
#             end = pairs[i][1]
#             j = i + 1
#             while j < n and pairs[j][0] <= end:
#                 j += 1
#             dp[i] = max(dp[i+1], 1 + dp[j])

#         return dp[0]


# class Solution:
#     def findLongestChain(self, pairs: List[List[int]]) -> int:
#         pairs.sort(key=lambda x: x[1])

#         count = 0
#         pb = float('-inf')
#         for a, b in pairs:
#             if pb < a:
#                 count+=1
#                 pb = b 
        
#         return count

# class Solution:
#     def findLongestChain(self, pairs: List[List[int]]) -> int:
#         pairs.sort()
#         n = len(pairs)
#         @cache
#         def dp(i):
#             if i == len(pairs)-1: 
#                 return 1         
#             if i >= len(pairs): 
#                 return 0
#             j = i+1
#             while j < len(pairs):            
#                 if pairs[j][0] > pairs[i][1]:
#                     break
#                 j+= 1                
            
#             return max(dp(i+1), dp(j)+1)
#         return dp(0)
        



                
        