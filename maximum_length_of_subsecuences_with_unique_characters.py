# 1239. Maximum Length of a Concatenated String with Unique Characters
# You are given an array of strings arr. A string s is formed by the concatenation
# of a subsequence of arr that has unique characters.
# Return the maximum possible length of s.
# A subsequence is an array that can be derived from another array by deleting some
# or no elements without changing the order of the remaining elements.
# Example 1:
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All the valid concatenations are:
# - ""
# - "un"
# - "iq"
# - "ue"
# - "uniq" ("un" + "iq")
# - "ique" ("iq" + "ue")
# Maximum length is 4.
# Example 2:
# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
# Example 3:
# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
# Explanation: The only string in arr has all 26 characters.
# Constraints:
# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lowercase English letters.

from typing import List



class Solution:
    def maxLength(self, arr: List[str]) -> int:

        N = len(arr)

        def have_duplicates(s: str) -> bool:
            seen = set()
            for char in s:
                if char in seen:
                    return True
                seen.add(char)
            return False

        res = 0

        def recursive(index: int, memo: dict, string: str) -> int:

            if index >= N:
                return 0

            if (index, string) in memo:
                return memo[(index, string)]

            if have_duplicates(string):
                memo[(index, string)] = -1000
                return recursive(index + 1, memo, string)

            actual_string = arr[index]
            actual_length = len(actual_string)

            new_string = string + actual_string
            
            if have_duplicates(new_string):
                memo[(index, string)] = -1000
                return recursive(index + 1, memo, string)
                

            with_actual = recursive(index + 1, memo, new_string)

            without_actual = recursive(index + 1, memo, string)

            memo[(index, string)] = max(
                with_actual + actual_length, without_actual
            )
            return memo[(index, string)]

        res += recursive(0, {}, "")
        return res

