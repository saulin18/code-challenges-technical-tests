# 2466. Count Ways To Build Good Strings
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given the integers zero, one, low, and high, we can construct a string by starting with
# an empty string, and then at each step perform either of the following:

# Append the character '0' zero times.
# Append the character '1' one times.
# This can be performed any number of times.

# A good string is a string constructed by the above process having a
# length between low and high (inclusive).

# Return the number of different good strings that can be constructed satisfying these
# properties. Since the answer can be large, return it modulo 109 + 7.

# Example 1:

# Input: low = 3, high = 3, zero = 1, one = 1
# Output: 8
# Explanation:
# One possible valid good string is "011".
# It can be constructed as follows: "" -> "0" -> "01" -> "011".
# All binary strings from "000" to "111" are good strings in this example.
# Example 2:

# Input: low = 2, high = 3, zero = 1, one = 2
# Output: 5
# Explanation: The good strings are "00", "11", "000", "110", and "011".


# Constraints:

# 1 <= low <= high <= 105
# 1 <= zero, one <= low



class Solution:
     def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0 for _ in range(high + 1)]
        dp[0] = 1
        res = 0
        for i in range(1, high + 1):
                if i >= zero:
                    dp[i] += dp[i - zero] % MOD
                if i >= one:
                    dp[i] += dp[i - one]  % MOD
        for i in range(low, high + 1):
                res += dp[i] 
        
        return res % MOD   


# TLE
# class Solution:
#     def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
#         MOD = 10**9 + 7
#         def recursive(current_string: str, memo: dict):

#             string_length = len(current_string)

#             if string_length > high:
#                 return 0

#             if string_length in memo:
#                 return memo[string_length]

#             res = 1 if string_length >= low and string_length <= high else 0
#             # Add 0 * zero times
#             res += recursive(current_string + "0" * zero, memo)
            
#             # Add 1 * one times
            
#             res += recursive(current_string + "1" * one, memo)
            
#             memo[string_length] = res

#             return memo[string_length]
            
#         return recursive("", {}) % MOD    

           


class Solution:
     def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0 for _ in range(high + 1)]
        dp[0] = 1
        res = 0
        for i in range(1, high + 1):
                if i >= zero:
                    dp[i] += dp[i - zero] % MOD
                if i >= one:
                    dp[i] += dp[i - one]  % MOD
        for length, way in enumerate(dp):
            if length >= low and length <= high:
                res += way 
        
        return res % MOD   
             
        
        
             
             
             
             