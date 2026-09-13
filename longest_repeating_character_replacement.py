# 424. Longest Repeating Character Replacement
# You are given a string s and an integer k. You can choose any character of the
# string and change it to any other uppercase English character. You can perform this
#  operation at most k times.
# Return the length of the longest substring containing the same letter you
#  can get after performing the above operations.
# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
# Constraints:

#     1 <= s.length <= 105
#     s consists of only uppercase English letters.
#     0 <= k <= s.length


from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        ocurrences_map: dict[str, int] = {}
        left = 0

        highest_ocurrence = 0
        for end in range(n):
            char = s[end]

            if char not in ocurrences_map:
                ocurrences_map[char] = 1
            else:
                ocurrences_map[char] += 1
            highest_ocurrence = max(highest_ocurrence, ocurrences_map[char])
            while left < n and end - left + 1 - highest_ocurrence > k:
                char_going_out = s[left]

                ocurrences_map[char_going_out] -= 1

                if ocurrences_map[char_going_out] == 0:
                    del ocurrences_map[char_going_out]

                length_of_window = end - left + 1

                left += 1

            length_of_window = end - left + 1
            res = max(res, length_of_window)

        return res
