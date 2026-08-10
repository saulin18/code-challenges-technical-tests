# 848. Shifting Letters
# You are given a string s of lowercase English letters and an integer array shifts of the same length.
# Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').
#     For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
# Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.
# Return the final string after all such shifts to s are applied.
# Example 1:
# Input: s = "abc", shifts = [3,5,9]
# Output: "rpl"
# Explanation: We start with "abc".
# After shifting the first 1 letters of s by 3, we have "dbc".
# After shifting the first 2 letters of s by 5, we have "igc".
# After shifting the first 3 letters of s by 9, we have "rpl", the answer.
# Example 2:
# Input: s = "aaa", shifts = [1,2,3]
# Output: "gfd"
# Constraints:
#     1 <= s.length <= 105
#     s consists of lowercase English letters.
#     shifts.length == s.length
#     0 <= shifts[i] <= 109


from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        start = 0
        for i in range(n):
            diff[start] += shifts[i]
            diff[i + 1] -= shifts[i]

        result = []
        current_shift = 0
        for i in range(n):
            current_shift += diff[i]
            result.append(chr((ord(s[i]) - ord('a') + current_shift) % 26 + ord('a')))

        return "".join(result)


# class Solution:
#     def shiftingLetters(self, s: str, shifts: List[int]) -> str:
#         result = list(s)
#         total_shift = 0

#         for i in range(len(s) - 1, -1, -1):
#             total_shift = (total_shift + shifts[i]) % 26
#             value = ord(s[i]) - ord('a')
#             value = (value + total_shift) % 26

#             result[i] = chr(value + ord('a'))

#         return ''.join(result)