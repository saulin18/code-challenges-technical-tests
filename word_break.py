# 139. Word Break
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into
# a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
# Constraints:

#     1 <= s.length <= 300
#     1 <= wordDict.length <= 1000
#     1 <= wordDict[i].length <= 20
#     s and wordDict[i] consist of only lowercase English letters.
#     All the strings of wordDict are unique.


from typing import List
# Top down
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:

#         wordDictSet = set(wordDict)
#         def backtrack(start: int, memo: dict) -> bool:
#             if start in memo:
#                 return memo[start]
#             if start == len(s):
#                 memo[start] = True
#                 return True
#             for end in range(start + 1, len(s) + 1):
#                 if s[start:end] in wordDictSet and backtrack(end, memo):
#                     memo[start] = True
#                     return True
#             memo[start] = False
#             return False
#         return backtrack(0, {})


# Bottom up
#


# class Solution:
#     def wordBreak(self, s: str, wordDict: list[str]) -> bool:
#         n = len(s)
#         dp = [False] * (n + 1)
#         dp[0] = True
#         wordDictSet = set(wordDict)
#         for i in range(1, n + 1):
#             for j in range(i - 1, -1, -1):
#                 if dp[j] and s[j:i] in wordDictSet:
#                     dp[i] = True
#                     break
#                 if i - j > 20:
#                     break
#         return dp[n]


class Trie:
    def __init__(self) -> None:
        self.children: dict[str, "Trie"] = {}
        self.is_end_of_word = False


    def insert(self, word: str) -> None:
        root = self

        for char in word:
            if char in root.children:
                root = root.children[char]
                continue
            root.children[char] = Trie()
            root = root.children[char]
        root.is_end_of_word = True

    def search(self, word: str) -> bool:
        root = self

        for char in word:
            if char not in root.children:
                return False
            root = root.children[char]
        return root.is_end_of_word
    
    

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
            
        def dfs(index: int, memo: dict) -> bool:
            node = trie
            if index in memo:
                return memo[index]
            if index == len(s):
                memo[index] = True
                return True
            for i in range(index, len(s)):
                    if s[i] not in node.children:
                        break
                    node = node.children[s[i]]
                    if node.is_end_of_word:
                        if dfs(i + 1, memo):
                            memo[index] = True
                            return True
            memo[index] = False
            return False
        
        # root = trie
        # def walk_trie(index: int, trie: Trie, memo: dict) -> bool:
        #     if index not in memo:
        #         memo[index] = {}
        #     if index in memo and trie in memo[index]:
        #         return memo[index][trie]
        #     if index == len(s) and trie.is_end_of_word:
        #         memo[index][trie] = True
        #         return True
        #     elif index == len(s) and not trie.is_end_of_word:
        #         memo[index][trie] = False
        #         return False
        #     if s[index] not in trie.children:
        #         memo[index][trie] = False
        #         return False
            
        #     if trie.children[s[index]].is_end_of_word:
        #         memo[index][trie] = walk_trie(index + 1, trie.children[s[index]], memo) or walk_trie(index + 1, root, memo)
        #         return memo[index][trie]
         
        #     memo[index][trie] = walk_trie(index + 1, trie.children[s[index]], memo)
        #     return memo[index][trie]
        
        return dfs(0, {})
    
   