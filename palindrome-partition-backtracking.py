#131. Palindrome Partitioning
#Medium
#Topics
#premium lock icon
#Companies
#Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
#
# 
#
#Example 1:
#
#Input: s = "aab"
#Output: [["a","a","b"],["aa","b"]]
#Example 2:
#
#Input: s = "a"
#Output: [["a"]]
# 
#
#Constraints:
#
#1 <= s.length <= 16
#s contains only lowercase English letters.

def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        
        def is_palindrome(subs: str) -> bool:
            return subs == subs[::-1]
        
        def backtrack(start: int, path: list[str]):
            if start >= len(s):
                res.append(path[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if is_palindrome(word):
                    path.append(word)
                    backtrack(end, path)
                    path.pop()
                    
        backtrack(0, [])
        
        return res            