# 567. Permutation in String
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.
# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# Constraints:
# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.


def checkInclusion(s1, s2):


    if len(s2) < len(s1):
        return False

    map_s1 = {}

    for char in s1:
        map_s1[char] = map_s1.get(char, 0) + 1
          
    start = 0
    values_with_zero_or_less = 0

    for end in range(len(s2)):
        char_end = s2[end]

        # We found a ocurrence of a character in s1
        if char_end in map_s1:
            map_s1[char_end] -= 1
            if map_s1[char_end] == 0:
                values_with_zero_or_less += 1

        if end - start + 1 > len(s1):
            char_start = s2[start]
            if char_start in map_s1:
                map_s1[char_start] += 1
            if char_start in map_s1 and map_s1[char_start] == 1:
                values_with_zero_or_less -= 1
        
            start +=1        

            # Shrink the window start +=1
        if values_with_zero_or_less == len(map_s1):
            return True

    return False

s1 = "hello"
s2 = "ooolleoooleh"

print(checkInclusion(s1, s2))