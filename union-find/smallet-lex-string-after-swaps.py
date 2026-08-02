# https://leetcode.com/problems/smallest-string-with-swaps/description/?envType=problem-list-v2&envId=union-find

# 1202. Smallest String With Swaps
# You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
# You can swap the characters at any pair of indices in the given pairs any number of times.
# Return the lexicographically smallest string that s can be changed to after using the swaps.
# Example 1
# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination:
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
# Example 2:
# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination:
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"
# Example 3:
# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination:
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"
# Constraints:
#     1 <= s.length <= 10^5
#     0 <= pairs.length <= 10^5
#     0 <= pairs[i][0], pairs[i][1] < s.length
#     s only contains lower case English letters.

from collections import defaultdict
from typing import List
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return

        if rootX < rootY:
            self.parent[rootX] = rootY
        elif rootY < rootX:
            self.parent[rootY] = rootX

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)

        for a, b in pairs:
            uf.union(a, b)

        groups_chars = defaultdict(list)
        for i in range(n):
            groups_chars[uf.find(i)].append(s[i])

        for group in groups_chars.values():
            group.sort(reverse=True)

        res = []
        for i in range(n):
            res.append(groups_chars[uf.find(i)].pop())

        return "".join(res)
