# 28. Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """

    if haystack == "" and needle == "":
        return 0

    if haystack.startswith(needle):
        return 0

    if len(haystack) < len(needle):
        return -1

    start = 0
    while start + len(needle) <= len(haystack):
        if haystack[start : start + len(needle)] == needle:
            return start
        start += 1

    print(start + len(needle) > len(haystack))

    return -1


print(strStr("abc", "c"))
