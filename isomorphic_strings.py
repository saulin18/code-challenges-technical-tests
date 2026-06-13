# 205. Isomorphic Strings
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map_s_t = {}
        map_t_s = {}    
        
        for i in range(len(s)):
            if map_s_t.get(s[i], None) is not None:
                if map_s_t[s[i]] != t[i]:
                    return False
            else:
                map_s_t[s[i]] = t[i]

            if map_t_s.get(t[i], None) is not None:
                if map_t_s[t[i]] != s[i]:
                    return False
            else:
                map_t_s[t[i]] = s[i]

        return True

# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         map_s_to_t = {}
#         map_t_to_s = {}

#         for cs, ct in zip(s, t):
# 
#             if cs in map_s_to_t:
#                 if map_s_to_t[cs] != ct:
#                     return False
#             else:
#                 if ct in map_t_to_s:
#                     return False
#                 map_s_to_t[cs] = ct
#                 map_t_to_s[ct] = cs
#         return True


# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "f11", t = "b23"

# Output: false

# Explanation:

# The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true


# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.
