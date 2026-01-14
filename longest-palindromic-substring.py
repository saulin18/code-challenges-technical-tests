def longestPalindrome(s):
    max_substr = ""

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    for center in range(len(s)):
        palindrome_odd = expand(center, center)
        palindrome_even = expand(center, center + 1)

        if len(palindrome_even) >= len(max_substr):
            max_substr = palindrome_even

        if len(palindrome_odd) >= len(max_substr):
            max_substr = palindrome_odd

    return max_substr


print(longestPalindrome("babad"))
# aba or bab
