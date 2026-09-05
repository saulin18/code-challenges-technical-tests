# Valid Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# Two strings are anagrams if they contain the same characters, with each character appearing the same number of times, 
# regardless of order.
# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true
# Example 2
# Input: s = "jar", t = "jam"
# Output: false
# Example 3:
# Input: s = "x", t = "x"
# Output: tru
# Constraints
#     1 <= s.length, t.length <= 5 * 10^4
#     s and t consist of lowercase English letters.
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars_of_s = defaultdict(int)

        for char in s:
            chars_of_s[char] += 1
        for char in t:
            if char not in chars_of_s or chars_of_s[char] == 0:
                return False
            chars_of_s[char] -= 1
        
        return True