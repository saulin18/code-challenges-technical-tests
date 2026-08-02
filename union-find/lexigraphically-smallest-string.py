# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/?envType=problem-list-v2&envId=union-find

# 1061. Lexicographically Smallest Equivalent String
# You are given two strings of the same length s1 and s2 and a string baseStr.
# We say s1[i] and s2[i] are equivalent characters.
#     For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
# Equivalent characters follow the usual rules of any equivalence relation:
#     Reflexivity: 'a' == 'a'.
#     Symmetry: 'a' == 'b' implies 'b' == 'a'.
#     Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.

# For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent 
# strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.
# Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.
# Example 1:
# Input: s1 = "parker", s2 = "morris", baseStr = "parser"
# Output: "makkek"
# Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
# The characters in each group are equivalent and sorted in lexicographical order.
# So the answer is "makkek".
# Example 2:
# Input: s1 = "hello", s2 = "world", baseStr = "hold"
# Output: "hdld"
# Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
# So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".
# Example 3:
# Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
# Output: "aauaaaaada"
# Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr 
# except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".
# Constraints:
#     1 <= s1.length, s2.length, baseStr <= 1000
#     s1.length == s2.length
#     s1, s2, and baseStr consist of lowercase English letters.


class UnionFind:
    def __init__(self):
        self.parent = [i for i in range(26)]
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int):
        rootX = self.find((x))
        rootY = self.find(y)
        if rootX == rootY:
            return
        if rootX < rootY:
            self.parent[rootY] = rootX
        else:
            self.parent[rootX] = rootY
    
    
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        for i in range(len(s1)):
            uf.union(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))
            
            
        result = []
        
        for char in baseStr:
            result.append(chr(uf.find(ord(char) - ord('a')) + ord('a')))
            
        return ''.join(result)
        
        
# class UF:
#     def __init__(self, n):
#         self.parent = [i for i in range(n)]
    
#     def find(self, u):
#         if self.parent[u] == u:
#             return u
#         self.parent[u] = self.find(self.parent[u])
#         return self.parent[u]
    
#     def union(self, u, v):
#         pu = self.find(u)
#         pv = self.find(v)
        
#         if pu == pv:
#             return

#         if pu < pv:
#             self.parent[pv] = pu
#         else:
#             self.parent[pu] = pv

# class Solution:
#     def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
#         uf = UF(26)

#         for i in range(len(s1)):
#             uf.union(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))
        
#         res = []

#         for ch in baseStr:
#             minCh = uf.find(ord(ch) - ord('a'))
#             res.append(chr(minCh + ord('a')))
        
#         return ''.join(res)

 