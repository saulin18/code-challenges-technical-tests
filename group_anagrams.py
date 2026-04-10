
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap: dict[str, list] = {}

        for st in strs:
            key = "".join(sorted([char for char in st]))
            if hashmap.get(key, None) is not None:
                hashmap[key].append(st)
                continue
            hashmap[key] = []
            hashmap[key].append(st)

        return hashmap.values()
