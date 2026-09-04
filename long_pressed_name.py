# 925. Long Pressed Name
# Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed,
# and the character will be typed 1 or more times.
# You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name,
# with some characters (possibly none) being long pressed.
# Example 1:
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# Example 2:
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it was not in the typed output.
# Constraints:
#     1 <= name.length, typed.length <= 1000
#     name and typed consist of only lowercase English letters.


from collections import defaultdict


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        j = 0
        i = 0
        n = len(name)
        while i < n:

            if j >= len(typed):
                return False

            if typed[j] == name[i]:
                i += 1
                j += 1
                continue

            if j > 0 and typed[j] == typed[j - 1] and name[i - 1] == typed[j - 1]:
                j += 1
                continue
            elif typed[j] != name[i]:
                return False

        for index in range(j + 1, len(typed)):
            if typed[index] != typed[index - 1]:
                return False

        return i == n


# class Solution:
#     def isLongPressedName(self, name: str, typed: str) -> bool:
#         n_p = 0
#         t_p = 0
        
#         while t_p < len(typed):
#             if n_p < len(name) and name[n_p] == typed[t_p]:
#                 n_p += 1
#                 t_p += 1
#             elif t_p > 0 and typed[t_p] == typed[t_p - 1]:
#                 t_p += 1
#             else:
#                 return False
        
#         return n_p == len(name)

# class Solution:
#     def isLongPressedName(self, name: str, typed: str) -> bool:
#         i, j = 0, 0
#         n, m = len(name), len(typed)

#         while j < m:
#             # 1. Characters match: advance both pointers
#             if i < n and name[i] == typed[j]:
#                 i += 1
#                 j += 1
#             # 2. Long press detected: current typed matches the previous typed char
#             elif j > 0 and typed[j] == typed[j - 1]:
#                 j += 1
#             # 3. Mismatch that isn't a valid long press
#             else:
#                 return False

#         # Ensure all characters in name were consumed
#         return i == n