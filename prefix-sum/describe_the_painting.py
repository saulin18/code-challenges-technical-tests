# 1943. Describe the Painting
# There is a long and thin painting that can be represented by a number line. The painting was
# painted with multiple overlapping segments where each segment was painted with a unique color. You are given a
# 2D integer array segments, where segments[i] = [starti, endi, colori] represents the half-closed segment [starti, endi
# ) with colori as the color.
# The colors in the overlapping segments of the painting were mixed when it was painted. When two or more
# colors mix, they form a new color that can be represented as a set of mixed colors.
#     For example, if colors 2, 4, and 6 are mixed, then the resulting mixed color is {2,4,6}.
# For the sake of simplicity, you should only output the sum of the elements in the set rather than the full set.
# You want to describe the painting with the minimum number of non-overlapping half-closed segments of these
# mixed colors. These segments can be represented by the 2D array painting
# where painting[j] = [leftj, rightj, mixj] describes a half-closed segment [leftj, rightj) with the mixed color sum of mixj.
#     For example, the painting created with segments = [[1,4,5],[1,7,7]] can be described
# by painting = [[1,4,12],[4,7,7]] because:
#         [1,4) is colored {5,7} (with a sum of 12) from both the first and second segments.
#         [4,7) is colored {7} from only the second segment.
# Return the 2D array painting describing the finished painting (excluding any parts that are not painted).
# You may return the segments in any order.
# A half-closed segment [a, b) is the section of the number line between
# points a and b including point a and not including point b.
# Example 1:
# Input: segments = [[1,4,5],[4,7,7],[1,7,9]]
# Output: [[1,4,14],[4,7,16]]
# Explanation: The painting can be described as follows:
# - [1,4) is colored {5,9} (with a sum of 14) from the first and third segments.
# - [4,7) is colored {7,9} (with a sum of 16) from the second and third segments.
# Example 2:
# Input: segments = [[1,7,9],[6,8,15],[8,10,7]]
# Output: [[1,6,9],[6,7,24],[7,8,15],[8,10,7]]
# Explanation: The painting can be described as follows:
# - [1,6) is colored 9 from the first segment.
# - [6,7) is colored {9,15} (with a sum of 24) from the first and second segments.
# - [7,8) is colored 15 from the second segment.
# - [8,10) is colored 7 from the third segment.
# Example 3:
# Input: segments = [[1,4,5],[1,4,7],[4,7,1],[4,7,11]]
# Output: [[1,4,12],[4,7,12]]
# Explanation: The painting can be described as follows:
# - [1,4) is colored {5,7} (with a sum of 12) from the first and second segments.
# - [4,7) is colored {1,11} (with a sum of 12) from the third and fourth segments.
# Note that returning a single segment [1,7) is incorrect because the mixed color sets are different.
# Constraints:
#     1 <= segments.length <= 2 * 104
#     segments[i].length == 3
#     1 <= starti < endi <= 105
#     1 <= colori <= 109
#     Each colori is distinct.

from typing import List


# class Solution:
#     def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
#         max_num = max(segments, key=lambda x: x[1])[1]
#         diff_arr = [0] * (max_num + 1)
#         points = set()
#         for start, end, _ in segments:
#             points.add(start)
#             points.add(end)
        
#         for start, end, color in segments:
#             diff_arr[start] += color
#             diff_arr[end] -= color
               
#         result = []
#         current_color = 0
#         prev_color = 0
#         prev_i = 0
#         for i, color in enumerate(diff_arr):
#             prev_color = current_color
#             current_color = prev_color + color
            
#             if i in points:
#                 result.append([prev_i, i, prev_color]) if prev_color > 0 else None
#                 prev_i = i
#         return result

from collections import defaultdict
from typing import List

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        # Map to store the net color change at each coordinate
        mix_map = defaultdict(int)
        
        # Populate the changes
        for start, end, color in segments:
            mix_map[start] += color
            mix_map[end] -= color
            
        # Sort the unique coordinates where a change occurs
        sorted_positions = sorted(mix_map.keys())
        
        result = []
        current_color_sum = 0
        
        # Iterate through adjacent coordinates
        for i in range(len(sorted_positions) - 1):
            left = sorted_positions[i]
            right = sorted_positions[i + 1]
            
            # Update the running sum at the 'left' boundary point
            current_color_sum += mix_map[left]
            
            # If the current interval has a color sum > 0, record it
            if current_color_sum > 0:
                result.append([left, right, current_color_sum])
                
        return result
        


# class Solution:
#     def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
#         diff = defaultdict(int)
#         for start, end, color in segments:
#             diff[start] += color
#             diff[end] -= color
            
#         res = []
#         prev = None
#         running = 0

#         for point in sorted(diff.keys()):
#             if prev is not None and running > 0:
#                 res.append([prev, point, running])
#             running += diff[point]
#             prev = point

#         return res
        
        
# class Solution:
#     def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:

#         events = {}

#         for start, end, color in segments:
#             events[start] = events.get(start, 0) + color
#             events[end] = events.get(end, 0) - color

#         points = sorted(events)

#         ans = []

#         current = 0
#         prev = None

#         for point in points:

#             # interval [prev, point)
#             if prev is not None and current > 0:
#                 ans.append([prev, point, current])

#             current += events[point]
#             prev = point

#         return ans
