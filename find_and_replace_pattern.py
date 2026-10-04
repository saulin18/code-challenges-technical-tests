# 890. Find and Replace Pattern
# Given a list of strings words and a string pattern, return a list of words[i] that match pattern. 
# You may return the answer in any order.
# A word matches the pattern if there exists a permutation of letters p so that after replacing every
# letter x in the pattern with p(x), we get the desired word.
# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, 
# Wand no two letters map to the same letter.
# Example 1:
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
# Example 2:
# Input: words = ["a","b","c"], pattern = "a"
# Output: ["a","b","c"]
# Constraints:
#     1 <= pattern.length <= 20
#     1 <= words.length <= 50
#     words[i]W.length == pattern.length
#     pattern and words[i] are lowercase English letters.

from collections import OrderedDict
class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        res = []
        for word in words:
            if len(word) != len(pattern):
                continue
            if self.is_match(word, pattern):
                res.append(word)
        return res
    
    def is_match(self, word: str, pattern: str) -> bool:
        pattern_ocurrences = {}
        word_ocurrences = {}
        for i in range(len(pattern)):
            if pattern[i] not in pattern_ocurrences:
                pattern_ocurrences[pattern[i]] = word[i]
            else:
                if pattern_ocurrences[pattern[i]] != word[i]:
                    return False
            
            if word[i] not in word_ocurrences:
                word_ocurrences[word[i]] = pattern[i]
            else:
                if word_ocurrences[word[i]] != pattern[i]:
                    return False
        return True
    
    
    
# class Solution:
#     def findAndReplacePattern(self, words, pattern):
#         answer = []

#         for word in words:
#             map1 = {}
#             map2 = {}
#             valid = True

#             for i in range(len(pattern)):
#                 w = word[i]
#                 p = pattern[i]

#                 if w in map1 and map1[w] != p:
#                     valid = False
#                     break

#                 if p in map2 and map2[p] != w:
#                     valid = False
#                     break

#                 map1[w] = p
#                 map2[p] = w

#             if valid:
#                 answer.append(word)

#         return answer

    