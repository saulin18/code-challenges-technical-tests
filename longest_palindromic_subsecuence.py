# 516. Longest Palindromic Subsequence
# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another
# sequence by deleting some or no elements without changing
# the order of the remaining elements.
# Example 1:
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
# Constraints:
# 1 <= s.length <= 1000
# s consists only of lowercase English letters.
# https://leetcode.com/problems/longest-palindromic-subsequence/?envType=problem-list-v2&envId=xixy4dq7


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[0] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = 1

        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if not s[i] == s[j]:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    continue

                dp[i][j] = dp[i + 1][j - 1] + 2
                continue

        return dp[0][N - 1]
    
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         n = len(s)
#         memo = [[0 for _ in range(n)] for _ in range(n)]
#         def helper(l, r, s, memo):
#             if memo[l][r] > 0:
#                 return memo[l][r]
#             if l > r:
#                 return 0
#             if l == r:
#                 return 1
#             if s[l] == s[r]:
#                 memo[l][r] = 2 + helper(l+1, r-1, s, memo)
#             else:
#                 memo[l][r] = max(helper(l+1, r, s, memo), helper(l, r-1, s, memo))
            
#             return memo[l][r]
        
#         ans = helper(0, len(s) - 1, s, memo)
#         return ans
        
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         n = len(s)
#         prev_row = [0] * n

#         for r in range(n-1, -1, -1):
#             row = [0] * n
#             row[r] = 1

#             for c in range(r+1, n):
#                 if s[r] == s[c]:
#                     row[c] = prev_row[c-1] + 2
#                 else:
#                     row[c] = max(prev_row[c], row[c-1])
            
#             prev_row = row
        
#         return prev_row[n-1]


    # -------------With memoization--------------------------

    # # With memoization
    # memo = {}
    # def longestPalindromeSubseq(self, s: str) -> int:
    #     if not s:
    #         return 0
    #     if len(s) == 1:
    #         return 1
    #     if s in self.memo:
    #         return self.memo[s]
    #     first = 0
    #     last = len(s) - 1
    #     res = 0
    #     if s[first] == s[last]:
    #         res = 2 + self.longestPalindromeSubseq(s[1:-1])
    #     else:
    #         res = max(self.longestPalindromeSubseq(s[1:]), self.longestPalindromeSubseq(s[:-1]))
        
    #     self.memo[s] = res
    #     return res