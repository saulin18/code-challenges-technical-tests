# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

# 438. Find All Anagrams in a String
# Given two strings s and p, return an array of all the start indices of
# p's anagrams in s. You may return the answer in any order.
# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# Constraints:
# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.

from typing import List

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(s) < len(p):
            return []

        p_ocurrences = Counter(p)
        tmp = p_ocurrences.copy()
        res = []

        start = 0
        matches = 0

        for end in range(len(s)):
            if s[end] in p_ocurrences:
                p_ocurrences[s[end]] -= 1

                if p_ocurrences[s[end]] == 0:
                    matches += 1

                if p_ocurrences[s[end]] < 0:
                    matches -= 1

            else:
                matches = 0
                p_ocurrences = tmp.copy()
                start = end + 1

            while (
                end - start + 1 > len(p)
                or (count := p_ocurrences.get(s[end], None)) is not None
                and count < 0
            ):
                
                p_ocurrences[s[start]] += 1
                if p_ocurrences[s[start]] == 1:
                    matches -= 1
                if p_ocurrences[s[start]] == 0:
                    matches += 1
                start += 1

            if matches == len(p_ocurrences):
                res.append(start)

        return res
