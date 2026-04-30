
# 56. Merge Intervals
# Given an array of intervals where 
# intervals[i] = [starti, endi], merge 
# all overlapping intervals, and 
# return an array of the non-overlapping intervals that cover all the intervals in the input.
# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# Example 3:

# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.


# from typing import List


# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
#         ans = []
#         interval = intervals[0]
        
#         intervals.sort(key=lambda x: x[0])
        
#         for index, next_interval in enumerate(intervals):
            
#             next_start, next_end = next_interval
            
#             if next_start <= interval[1]:
#                 interval[0] = min(interval[0], next_start)
#                 interval[1] = max(interval[1], next_end)
#             else:
#                 ans.append(interval)
#                 interval = next_interval
        
#         ans.append(interval)
#         return ans 
            
            
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         result = []
#         for (start, end) in sorted(intervals):
#             if len(result) != 0 and start <= result[-1][1]:
#                 result[-1][1] = max(result[-1][1], end)
#             else:
#                 result.append([start, end])
#         return result
            
        