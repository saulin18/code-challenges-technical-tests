# 218. The Skyline ProblemW
# A city's skyline is the outer contour of the silhouette formed by all
# the buildings in that city when viewed from a distance. Given the locations
# and heights of all the buildings, return the skyline formed by these buildings collectively.
# The geometric information of each building is given in the array buildings
# where buildings[i] = [lefti, righti, heighti]:
#     lefti is the x coordinate of the left edge of the ith building.
#     righti is the x coordinate of the right edge of the ith building.
#     heighti is the height of the ith building.
# You may assume all buildings are perfect rectangles grounded on
# an absolutely flat surface at height 0.
# The skyline should be represented as a list of "key points"
# sorted by their x-coordinate in the form
# [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of
# some horizontal segment in the skyline except the last point
# in the list, which always has a y-coordinate 0 and is used to mark
# the skyline's termination where the rightmost building ends.
# Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.
# Note: There must be no consecutive horizontal
# lines of equal height in the output skyline.
# For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable;
# the three lines of height 5 should be merged into one in the final output
# as such: [...,[2 3],[4 5],[12 7],...]
# Example 1:
# Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
# Explanation:
# Figure A shows the buildings of the input.
# Figure B shows the skyline formed by those buildings.
# WThe red points in figure B represent the key points in the output list.
# Example 2:W
# Input: buildings = [[0,2,3],[2,5,3]]
# Output: [[0,3],[5,0]]

from typing import List
from collections import defaultdict
import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        events = defaultdict(list)
        active_heights = []
        result = []
        for left, right, height in buildings:
            events[left].append(height)
            events[right].append(-height)
        prev_max = 0
        deleted_counter = defaultdict(int)
        for x in sorted(events.keys()):
            for height in events[x]:
                if height > 0:
                    heapq.heappush(active_heights, -height)
                else:   
                   deleted_counter[height] += 1
                   
            if active_heights:
                
                while active_heights and deleted_counter[active_heights[0]] > 0:
                    deleted_counter[active_heights[0]] -= 1
                    heapq.heappop(active_heights)
                    
                max_height = -active_heights[0] if active_heights else 0
                    
                if max_height != prev_max:
                    prev_max = max_height
                    result.append([x, max_height])
        return result
        
        
# class Solution:
#     def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
#         skyline = []
#         heap = []  # (height, end)
#         buildings.append([inf, inf, inf])  # flusher building

#         for start, end, height in buildings:
#             # process buildings that have already ended
#             while heap and start > heap[0][1]:
#                 prev_height, prev_end = heappop_max(heap)
#                 # discard smaller buildings that ended even earlier
#                 while heap and heap[0][1] <= prev_end:
#                     heappop_max(heap)
#                 # draw right skyline point until the next tallest building or the floor
#                 skyline.append([prev_end, heap[0][0] if heap else 0])

#             # for new buildings draw left skyline if it's above current highest
#             if not heap or height > heap[0][0]:
#                 # same start different height case
#                 if skyline and skyline[-1][0] == start:
#                     skyline[-1][1] = height
#                 else:
#                     skyline.append([start, height])
            
#             heappush_max(heap, (height, end))

#         skyline.pop()  # pop the flusher

#         return skyline

            

        


# Constraints:

#     1 <= buildings.length <= 104
#     0 <= lefti < righti <= 231 - 1
#     1 <= heighti <= 231 - 1
#     buildings is sorted by lefti in non-decreasing order.
