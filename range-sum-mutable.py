# 307. Range Sum Query - Mutable
# Given an integer array nums, handle multiple queries of the following types:
# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int val) Updates the value of nums[index] to be val.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
# Example 1:
# Input
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# Output
# [null, 9, null, 8]
# Explanation
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1, 2, 5]
# numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
# Constraints:
# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# At most 3 * 104 calls will be made to update and sumRange.

from typing import Callable, List


class SegmentTree:
    def __init__(self, n: int, identity: int, combine: Callable = lambda x, y: x + y) -> None:
        self.n = n
        self.tree: list[int] = [0] * (4 * n)
        self.combine: Callable = combine

    def build(self, node: int, start: int, end: int, nums: list[int]) -> None:

        if start == end:
            self.tree[node] = nums[start]
            return

        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2

        self.build(left_node, start, mid, nums)
        self.build(right_node, mid + 1, end, nums)

        self.tree[node] = self.combine(self.tree[left_node], self.tree[right_node])


    def query(self, node:int, start: int, end: int, left: int, right: int):

            # Invalid range
            if end < left or start > right:
                return 0

            if all((start >= left, end <= right)):

                return self.tree[node]


            mid = (start + end) // 2
            left_tree = 2 * node + 1
            right_tree = 2 * node + 2
            left_result = self.query(left_tree, start, mid, left, right)
            right_result = self.query(right_tree, mid + 1, end, left, right)
            return self.combine(left_result, right_result)



    def update(self, index: int, start: int, end: int, value: int, node: int) -> None:

        if index < start or index > end:
            raise Exception("Index out of bounds")

        if start == end:
            self.tree[node] = value
            return

        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2

        if index <= mid:
            self.update(index, start, mid, value, left_node)
        else:
            self.update(index, mid + 1, end, value, right_node)

        self.tree[node] = self.combine(self.tree[left_node], self.tree[right_node])




class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.seg_tree  = SegmentTree(self.n, 0)
        self.seg_tree.build(0, 0, self.n - 1, nums )

    def update(self, index: int, val: int) -> None:
        return self.seg_tree.update(index, 0, self.n - 1, val, 0)


    def sumRange(self, left: int, right: int) -> int:
        return self.seg_tree.query(0, 0, self.n - 1, left, right)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums
#         self.sum = sum(nums)
#         self.d = {}

#     def update(self, index: int, val: int) -> None:
#         self.sum += val-self.nums[index]
#         self.nums[index] = val
#         self.d = {}

#     def sumRange(self, left: int, right: int) -> int:
#         if (left, right) in self.d:
#             return self.d[(left, right)]
#         elif (right - left) >= (len(self.nums))//2:
#             res = self.sum - sum(self.nums[:left]) - sum(self.nums[right+1:])
#         else:
#             res = sum(self.nums[left:right+1])
#         self.d[(left, right)] = res
#         return res