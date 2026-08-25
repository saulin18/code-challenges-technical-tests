# https://leetcode.com/problems/range-frequency-queries/description/?envType=problem-list-v2&envId=segment-tree

# 2080. Range Frequency Queries
# Design a data structure to find the frequency of a given value in a given subarray.
# The frequency of a value in a subarray is the number of occurrences of that value in the subarray.
# Implement the RangeFreqQuery class:
# RangeFreqQuery(int[] arr) Constructs an instance of the class with the given 0-indexed integer array arr.
# int query(int left, int right, int value) Returns the frequency of value in the subarray arr[left...right].
# A subarray is a contiguous sequence of elements within an array. arr[left...right] denotes the subarray that contains
# the elements of nums between indices left and right (inclusive).
# Example 1:
# Input
# ["RangeFreqQuery", "query", "query"]
# [[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
# Output
# [null, 1, 2]
# Explanation
# RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
# rangeFreqQuery.query(1, 2, 4); // return 1. The value 4 occurs 1 time in the subarray [33, 4]
# rangeFreqQuery.query(0, 11, 33); // return 2. The value 33 occurs 2 times in the whole array.
# Constraints:

#     1 <= arr.length <= 105
#     1 <= arr[i], value <= 104
#     0 <= left <= right < arr.length
#     At most 105 calls will be made to query


from bisect import bisect_right
from bisect import bisect_left
class SegmentTree:
    def __init__(self, arr: list[int]):
        self.arr = arr
        self.tree: list[list[int]] = [[] for _ in range(4 * len(arr))]
        self.build(0, 0, len(arr) - 1)

    def build(self, node: int, start: int, end: int):
        if start == end:

            self.tree[node].append(self.arr[start])
            return
        mid = (start + end) // 2
        self.build(2 * node + 1, start, mid)
        self.build(2 * node + 2, mid + 1, end)
        self.tree[node] = sorted(self.tree[2 * node + 1] + self.tree[2 * node + 2])
        

    def query(self, node: int, start: int, end: int, left: int, right: int, value: int):
        if left > end or right < start:
            return 0
        if left <= start and right >= end:
            start_index = bisect_left(self.tree[node], value)
            end_index = bisect_right(self.tree[node], value)
            return end_index - start_index
        mid = (start + end) // 2
        return (
            self.query(2 * node + 1, start, mid, left, right, value)
            + self.query(2 * node + 2, mid + 1, end, left, right, value)
        )

class RangeFreqQuery:

    def __init__(self, arr: list[int]):
        self.segment_tree = SegmentTree(arr)

    def query(self, left: int, right: int, value: int) -> int:
        return self.segment_tree.query(0, 0, len(self.segment_tree.arr) - 1, left, right, value)
    
    
# from collections import defaultdict
# from bisect import bisect_left, bisect_right
# from typing import List

# class RangeFreqQuery:

#     def __init__(self, arr: List[int]):
#         self.pos = defaultdict(list)

#         for i, num in enumerate(arr):
#             self.pos[num].append(i)

#     def query(self, left: int, right: int, value: int) -> int:
#         if value not in self.pos:
#             return 0

#         indices = self.pos[value]

#         # first index >= left
#         l = bisect_left(indices, left)

#         # first index > right
#         r = bisect_right(indices, right)

#         return r - l
    
    
# class RangeFreqQuery:
#     def __init__(self, arr: list[int]):
#         self.l = [[] for _ in range(10001)]
#         for i, v in enumerate(arr):
#             self.l[v].append(i)
#     def query(self, left: int, right: int, v: int) -> int:
#         return bisect_right(self.l[v], right) - bisect_left(self.l[v], left)



# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
