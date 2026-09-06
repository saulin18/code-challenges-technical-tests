# 115. Distinct Subsequences
# Given two strings s and t, return the number of distinct subsequences of s which equals t.
# The test cases are generated so that the answer fits on a 32-bit signed integer.
# Example 1:
# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit
# Example 2:
# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
# Constraints:
#     1 <= s.length, t.length <= 1000
#     s and t consist of English letters.

 
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        len_of_s = len(s)
        len_of_t = len(t)

        dp = [[0 for _ in range(len_of_s)] for _ in range(len_of_t)]

        for i in range(len_of_s):
            if s[i] == t[0]:
                dp[0][i] = dp[0][i - 1] + 1 if i > 0 else 1
            else:
                dp[0][i] = dp[0][i - 1] if i > 0 else 0
        for j in range(1, len_of_t):
            for i in range(1, len_of_s):
                if s[i] == t[j]:
                    dp[j][i] = dp[j - 1][i - 1] + dp[j][i - 1]
                else:
                    dp[j][i] = dp[j][i - 1]
        return dp[len_of_t - 1][len_of_s - 1]


# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         n = len(s)
#         m = len(t)

#         dp = [[0] * (m+1) for _ in range(n+1)]

#         for i in range(0, n+1):
#             dp[i][0] = 1

#         for j in range(1, m+1):
#             dp[0][j] = 0

#         for i in range(1,n+1):
#             for j in range(1, m+1):
#                 if s[i-1] == t[j-1]:
#                     dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
#                 else:
#                     dp[i][j] = dp[i-1][j]

#         return dp[n][m]

# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         # n1 = len(s)
#         # n2 = len(t)
#         # dp = [[-1]*n2 for _ in range(n1)]

#         # def dfs(i, j):
#         #     if j == n2:
#         #         return 1
#         #     if i == n1:
#         #         return 0
#         #     if dp[i][j] == -1:
#         #         dp[i][j] = dfs(i+1, j)
#         #         if s[i] == t[j]:
#         #             dp[i][j] += dfs(i+1, j+1)
#         #     return dp[i][j]
#         # return dfs(0,0)
#         # rows = len(s)
#         # cols = len(t)
#         # dp = [[0]*(cols+1) for _ in range(rows+1)]
#         # for r in range(rows+1):
#         #     dp[r][0] = 1
#         # for r in range(1, rows+1):
#         #     for c in range(1, cols+1):
#         #         dp[r][c] = dp[r-1][c]
#         #         if s[r-1] == t[c-1]:
#         #             dp[r][c] += dp[r-1][c-1]
#         # return dp[rows][cols]

#         rows = len(s)
#         cols = len(t)

#         dp = [0] * (cols + 1)
#         dp[0] = 1

#         for r in range(1, rows + 1):
#             for c in range(cols, 0, -1):
#                 if s[r - 1] == t[c - 1]:
#                     dp[c] += dp[c - 1]

#         return dp[cols]


# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         if len(t) > len(s):
#             return 0

#         memo = {}

#         def dfs(i, j):
#             if i == len(s) or j == len(t) or len(s) - i < len(t) - j:
#                 return int(j == len(t))
#             if (i, j) in memo:
#                 return memo[(i, j)]

#             ans = dfs(i + 1, j)
#             if s[i] == t[j]:
#                 ans += dfs(i + 1, j + 1)
#             memo[(i, j)] = ans
#             return ans

#         return dfs(0, 0)
        

