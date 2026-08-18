# 699. Falling Squares

# There are several squares being dropped onto the X-axis of a 2D plane.

# You are given a 2D integer array positions where
#  positions[i] = [lefti, sideLengthi] represents the ith square with a side length of
#  sideLengthi that is dropped with its left edge aligned with X-coordinate lefti.

# Each square is dropped one at a time from a
# height above any landed squares.
# It then falls downward (negative Y direction) until it either lands on the top side of
# another square or on the X-axis.
# A square brushing the left/right side of another square does not count as landing on it.
#  Once it lands, it freezes in place and cannot be moved.

# After each square is dropped, you must record the height of the current tallest stack of squares.

# Return an integer array ans where ans[i] represents the height described above after dropping the ith square.

# Example 1:

# Input: positions = [[1,2],[2,3],[6,1]]
# Output: [2,5,5]
# Explanation:
# After the first drop, the tallest stack is square 1 with a height of 2.
# After the second drop, the tallest stack is squares 1 and 2 with a height of 5.
# After the third drop, the tallest stack is still squares 1 and 2 with a height of 5.
# Thus, we return an answer of [2, 5, 5].

# Example 2:

# Input: positions = [[100,100],[200,100]]
# Output: [100,100]
# Explanation:
# After the first drop, the tallest stack is square 1 with a height of 100.
# After the second drop, the tallest stack is either square 1 or square 2, both with heights of 100.
# Thus, we return an answer of [100, 100].
# Note that square 2 only brushes the right side of square 1, which does not count as landing on it.
# Constraints:

#     1 <= positions.length <= 1000
#     1 <= lefti <= 108
#     1 <= sideLengthi <= 106


from collections.abc import Callable


class SegTree:
    def __init__(
        self, n: int, identity: int = 0, function: Callable = lambda x, y: max(x, y)
    ):
        self.lazy: list[int | None] = [None] * (4 * n)
        self.arr: list[int] = [0] * (4 * n)
        self.n: int = n
        self.identity: int = identity
        self.function: Callable = function

    def query(
        self, left: int, right: int, start: int = 0, end: int = -1, node: int = 0
    ) -> int:
        if end == -1:
            end = self.n - 1
        if start > right or end < left:
            return self.identity
        if start >= left and end <= right:
            return self.arr[node]
        self.push(node)
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        mid = (start + end) // 2
        return self.function(
            self.query(left, right, start, mid, left_child),
            self.query(left, right, mid + 1, end, right_child),
        )

    def update(
        self,
        value: int,
        left: int,
        right: int,
        start: int = 0,
        end: int = -1,
        node: int = 0,
    ) -> None:
        if end == -1:
            end = self.n - 1
        if start > right or end < left:
            return None
        if start >= left and end <= right:
            self.arr[node] = value
            self.lazy[node] = value
            return None
        self.push(node) if start != end else None
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        mid = (start + end) // 2
        self.update(value, left, right, start, mid, left_child)
        self.update(value, left, right, mid + 1, end, right_child)
        self.arr[node] = self.function(self.arr[left_child], self.arr[right_child])
        return None

    def push(self, node: int) -> None:
        if self.lazy[node] is None:
            return
        h = self.lazy[node]
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        assert h is not None, "Height is not None"
        self.arr[left_child] = h
        self.arr[right_child] = h
        self.lazy[left_child] = h
        self.lazy[right_child] = h
        self.lazy[node] = None
        return None


class Solution:
    def fallingSquares(self, positions: list[list[int]]) -> list[int]:

        def coordinate_compression(positions: list[list[int]]) -> list[int]:
            coordinates: set[int] = set()
            for left, side in positions:
                coordinates.add(left)
                coordinates.add(left + side)
            return sorted(coordinates)

        coordinates: list[int] = coordinate_compression(positions)
        coordinate_to_index: dict[int, int] = {
            coordinate: index for index, coordinate in enumerate(coordinates)
        }
        n: int = len(coordinates) - 1
        res: list[int] = []
        seg_tree: SegTree = SegTree(n, 0, max)

        max_height: int = 0
        for left, side in positions:
            left_index: int = coordinate_to_index[left]
            right_index: int = coordinate_to_index[left + side] - 1
            height: int = seg_tree.query(left_index, right_index) + side
            seg_tree.update(height, left_index, right_index)
            max_height = max(max_height, height)
            res.append(max_height)

        return res
    
    
# O(N log N) Time
# - each square performs one range query + one range update,
# - each taking O(log N) on the Segment Tree.
# - (Coordinate compression and tree building are O(N log N) and O(N), respectively.)
# O(N) Space
# - O(N) compressed coordinates + O(N) Segment Tree nodes.
# where, N = number of squares

# class SegmentTree:
#     def __init__(self, L, R):
#         self.L = L
#         self.R = R
#         self.maxHeight = 0          # Maximum height in this interval
#         self.lazy = 0               # Lazy propagation value
#         self.left = None
#         self.right = None

#     @staticmethod
#     def build(L, R):
#         node = SegmentTree(L, R)

#         if L == R:
#             return node

#         M = (L + R) // 2
#         node.left = SegmentTree.build(L, M)
#         node.right = SegmentTree.build(M + 1, R)
#         return node

#     def pushDown(self):
#         # Propagate pending assignment to children.
#         if self.lazy != 0 and self.left:
#             self.left.maxHeight = self.lazy
#             self.right.maxHeight = self.lazy

#             self.left.lazy = self.lazy
#             self.right.lazy = self.lazy

#             self.lazy = 0

#     def rangeQuery(self, L, R):
#         # Exact match
#         if self.L == L and self.R == R:
#             return self.maxHeight

#         self.pushDown()

#         M = (self.L + self.R) // 2

#         if R <= M:
#             return self.left.rangeQuery(L, R)

#         elif L > M:
#             return self.right.rangeQuery(L, R)

#         else:
#             return max(
#                 self.left.rangeQuery(L, M),
#                 self.right.rangeQuery(M + 1, R)
#             )

#     def rangeUpdate(self, L, R, height):
#         # Entire segment becomes 'height'
#         if self.L == L and self.R == R:
#             self.maxHeight = height
#             self.lazy = height
#             return

#         self.pushDown()

#         M = (self.L + self.R) // 2

#         if R <= M:
#             self.left.rangeUpdate(L, R, height)

#         elif L > M:
#             self.right.rangeUpdate(L, R, height)

#         else:
#             self.left.rangeUpdate(L, M, height)
#             self.right.rangeUpdate(M + 1, R, height)

#         self.maxHeight = max(
#             self.left.maxHeight,
#             self.right.maxHeight
#         )

# class Solution:
#     def fallingSquares(self, positions: List[List[int]]) -> List[int]:

#         # -----------------------------
#         # Coordinate Compression
#         # -----------------------------
#         # Coordinates can be as large as 1e8, so we cannot build
#         # a Segment Tree over every x-coordinate.
#         #
#         # Instead, keep only the coordinates where intervals start
#         # and end, then map them to 0...N-1.
#         coords = set()

#         for left, size in positions:
#             coords.add(left)
#             coords.add(left + size - 1)

#         coords = sorted(coords)

#         # Map original coordinate -> compressed index.
#         index = {}
#         for i, x in enumerate(coords):
#             index[x] = i

#         # Build Segment Tree over compressed coordinates.
#         root = SegmentTree.build(0, len(coords) - 1)

#         ans = []
#         tallest = 0

#         for left, size in positions:

#             # Interval covered by the current square.
#             right = left + size - 1

#             # Convert original coordinates to compressed indices.
#             L = index[left]
#             R = index[right]

#             # Query the maximum height already present underneath
#             # this square. The new square will be stacked on top of it.
#             baseHeight = root.rangeQuery(L, R)

#             # Height after dropping this square.
#             newHeight = baseHeight + size

#             # Update the entire covered interval to the new height.
#             #
#             # Lazy propagation happens INSIDE rangeUpdate():
#             # - If an update completely covers a node's interval,
#             #   we store the height in that node and mark it as "lazy"
#             #   instead of immediately updating all descendants.
#             # - The pending update is pushed to children later only
#             #   when another query/update needs to visit them.
#             root.rangeUpdate(L, R, newHeight)

#             # Keep track of the tallest stack seen so far.
#             tallest = max(tallest, newHeight)
#             ans.append(tallest)

#         return ans


# class Solution:
#     def fallingSquares(self, positions: list[list[int]]) -> list[int]:

#         intervals = []
#         max_height = 0
#         res = []
#         for left, side in positions:
#             right = left + side

#             base_height = 0
#             for interval in intervals:
#                 if interval[1] > left and interval[0] < right:
#                     base_height = max(base_height, interval[2])
#             intervals.append((left, right, base_height + side))
#             max_height = max(max_height, base_height + side)
#             res.append(max_height)

#         return res


# class Solution:
#     def fallingSquares(self, positions: list[list[int]]) -> list[int]:
#         # Store dropped squares as: (left, right, height)
#         intervals = []
#         ans = []
#         global_max = 0

#         for left, size in positions:
#             right = left + size
#             base_height = 0

#             # Check for overlaps with every square already on the ground
#             for prev_left, prev_right, prev_height in intervals:
#                 # OVERLAP CONDITION:
#                 # Does the new left start strictly before the old right AND
#                 # Does the new right end strictly after the old left?
#                 if left < prev_right and right > prev_left:
#                     base_height = max(base_height, prev_height)

#             # The new square rests on the highest overlapping peak
#             new_height = base_height + size
#             intervals.append((left, right, new_height))

#             # Update the highest point seen on the entire board
#             global_max = max(global_max, new_height)
#             ans.append(global_max)

#         return ans


# from bisect import bisect_left, bisect_right

# class Solution:
#     def fallingSquares(self, positions: List[List[int]]) -> List[int]:
#         height = [0]
#         pos = [0]
#         res = []
#         max_h = 0
#         for left, side in positions:
#             i = bisect.bisect_right(pos, left)
#             j = bisect.bisect_left(pos, left + side)
#             high = max(height[i - 1:j] or [0]) + side
#             pos[i:j] = [left, left + side]
#             height[i:j] = [high, height[j - 1]]
#             max_h = max(max_h, high)
#             res.append(max_h)
#         return res
