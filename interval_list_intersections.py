# 986. Interval List Intersections
# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj].
# Each list of intervals is
# pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example,
# the intersection of [1, 3] and [2, 4] is [2, 3].
# Example 1:
# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Example 2:
# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []
# Constraints:
# 0 <= firstList.length, secondList.length <= 1000
# firstList.length + secondList.length >= 1
# 0 <= starti < endi <= 109
# endi < starti+1
# 0 <= startj < endj <= 109
# endj < startj+1

from typing import List


def intervalIntersection(
    firstList: List[List[int]], secondList: List[List[int]]
) -> List[List[int]]:

    if firstList == [] or secondList == []:
        return []

    left = 0
    first_length = len(firstList)
    second_length = len(secondList)
    right = 0
    
    res = []

    while left <= first_length - 1 and right <= second_length - 1:
        a_start, a_end = firstList[left]
        b_start, b_end = secondList[right]

        low = max(a_start, b_start)
        high = min(a_end, b_end)

        intersection = None
        if low <= high:
            intersection = [low, high]

        if intersection is not None:
            res.append(intersection)

        if a_end < b_end:
            left += 1
        else:
            right += 1

    return res


firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
print(intervalIntersection(firstList, secondList))

