# 3612. Process String with Special Operations I
# You are given a string s consisting of lowercase English letters and the special characters: *, #, and %.
# Build a new string result by processing s according to the following rules from left to right:
#     If the letter is a lowercase English letter append it to result.
#     A '*' removes the last character from result, if it exists.
#     A '#' duplicates the current result and appends it to itself.
#     A '%' reverses the current result.
# Return the final string result after processing all characters in s.
# Example 1:
# Input: s = "a#b%*"
# Output: "ba"
# Explanation:
# i	s[i]	Operation	Current result
# 0	'a'	Append 'a'	"a"
# 1	'#'	Duplicate result	"aa"
# 2	'b'	Append 'b'	"aab"
# 3	'%'	Reverse result	"baa"
# 4	'*'	Remove the last character	"ba"
# Thus, the final result is "ba".
# Example 2:
# Input: s = "z*#"
# Output: ""
# Explanation:
# i	s[i]	Operation	Current result
# 0	'z'	Append 'z'	"z"
# 1	'*'	Remove the last character	""
# 2	'#'	Duplicate the string	""
# Thus, the final result is "".
# Constraints:
#     1 <= s.length <= 20
#     s consists of only lowercase English letters and special characters *, #, and %.

import re
class Solution:
    # Build a new string result by processing s according to the following rules from left to right:
    # If the letter is a lowercase English letter append it to result.
    # A '*' removes the last character from result, if it exists.
    # A '#' duplicates the current result and appends it to itself.
    # A '%' reverses the current result.

    def processStr(self, s: str) -> str:
        rev = False
        n = len(s)
        res = []

        regex = "^[a-z]$"

        for i in range(n):
            # lower case letter
           if s[i].islower():
            res.append(s[i])
            continue

           if s[i] == '*':
            res.pop() if len(res) > 0 else None
            
           if s[i] == '#':
               res += res[:]
               continue
           
           
           if s[i] == '%':
                res.reverse()
        return "".join(res)

# class Solution:
#     def processStr(self, s: str) -> str:
#         res = ''
#         for c in s:
#             if c == '*':
#                 if len(res) > 0:
#                     res = res[:-1]
#             elif c == '#':
#                 res += res
#             elif c == '%':
#                 res = res[-1::-1]
#             else:
#                 res += c
#         return res