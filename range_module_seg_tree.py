# 715. Range Module
# Hard
# Topics
# premium lock iconCompanies
# Hint

# A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

# A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

# Implement the RangeModule class:

#     RangeModule() Initializes the object of the data structure.
#     void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval.
# Adding an interval that partially overlaps with currently tracked numbers should add any numbers in
# the interval [left, right) that are not already tracked.
#     boolean queryRange(int left, int right) Returns true if every real number in the interval 
# [left, right) is currently being tracked, and false otherwise.
#     void removeRange(int left, int right) Stops tracking every real number currently being tracked in the
# half-open interval [left, right).
# Example 1:

# Input
# ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
# [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
# Output
# [null, null, null, true, false, true]

# Explanation
# RangeModule rangeModule = new RangeModule();
# rangeModule.addRange(10, 20);
# rangeModule.removeRange(14, 16);
# rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
# rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
# rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)

 

# Constraints:

#     1 <= left < right <= 109
#     At most 104 calls will be made to addRange, queryRange, and removeRange.

 
from typing import Any, cast

from sortedcontainers import SortedDict


class RangeModule:

    def __init__(self) -> None:
        # sortedcontainers stubs don't expose SortedDict[K, V]
        self.sorted_dict: Any = SortedDict()

    def _at(self, index: int) -> tuple[int, int] | None:
        """Return (start, end) at position index, or None if out of range."""
        if index < 0 or index >= len(self.sorted_dict):
            return None
        return cast(tuple[int, int], self.sorted_dict.peekitem(index))

    def addRange(self, left: int, right: int) -> None:
        # index = first key >= left (next slot)
        index = self.sorted_dict.bisect_left(left) 
        prev_interval = self._at(index - 1)
        next_interval = self._at(index)

        while prev_interval is not None and self.does_overlap(
            prev_interval, (left, right)
        ):
            left = min(prev_interval[0], left)
            right = max(prev_interval[1], right)
            self.sorted_dict.pop(prev_interval[0])
            prev_interval = self._at(index - 1)

        next_interval = self._at(index)
        while next_interval is not None and self.does_overlap(
            next_interval, (left, right)
        ):
            left = min(next_interval[0], left)
            right = max(next_interval[1], right)
            self.sorted_dict.pop(next_interval[0])
            next_interval = self._at(index)

        self.sorted_dict[left] = right

    def does_overlap(
        self,
        prev_interval: tuple[int, int] | None,
        next_interval: tuple[int, int] | None,
    ) -> bool:
        if prev_interval is None or next_interval is None:
            return False
        return (
            prev_interval[1] >= next_interval[0]
            and next_interval[1] >= prev_interval[0]
        )

    def queryRange(self, left: int, right: int) -> bool:
        index = self.sorted_dict.bisect_right(left) - 1
        prev_interval = self._at(index)
        
        if prev_interval is None:
            return False
        return prev_interval[1] >= right
        

    def removeRange(self, left: int, right: int) -> None:
        index = self.sorted_dict.bisect_left(left)
        prev_interval = self._at(index - 1)
        
        
        next_interval = self._at(index)
        
        while prev_interval is not None and self.does_overlap_strict(
            prev_interval, (left, right)
        ):
            self.sorted_dict.pop(prev_interval[0])
            if prev_interval[0] < left:
                self.sorted_dict[prev_interval[0]] = left
            if prev_interval[1] > right:
                self.sorted_dict[right] = prev_interval[1]
            prev_interval = self._at(index - 1)
            index -= 1
            
            
        index = self.sorted_dict.bisect_left(left)
        
        while next_interval is not None and self.does_overlap_strict(
            next_interval, (left, right)
        ):
            self.sorted_dict.pop(next_interval[0])
            if next_interval[0] < left:
                self.sorted_dict[next_interval[0]] = left
            if next_interval[1] > right:
                self.sorted_dict[right] = next_interval[1]
            next_interval = self._at(index)
        return
    
    def does_overlap_strict(self, prev_interval: tuple[int, int] | None, next_interval: tuple[int, int] | None) -> bool:
        
        if prev_interval is None or next_interval is None:
            return False
        return max(prev_interval[0], next_interval[0]) < min(prev_interval[1], next_interval[1])
    
    
# import bisect

# class RangeModule:
#     def __init__(self):
#         self.ranges = []

#     def modify(self, left, right, add=True):
#         l = bisect.bisect_left(self.ranges, left)
#         r = bisect.bisect_right(self.ranges, right)
#         self.ranges[l:r] = ([left] if add ^ (l % 2) else []) + ([right] if add ^ (r % 2) else [])

#     def addRange(self, left: int, right: int) -> None:
#         self.modify(left, right)

#     def removeRange(self, left: int, right: int) -> None:
#         self.modify(left, right, False)

#     def queryRange(self, left: int, right: int) -> bool:
#         l = bisect.bisect_right(self.ranges, left)
#         r = bisect.bisect_left(self.ranges, right)
#         return (l % 2) == 1 and l == r


# class RangeModule:

#     def __init__(self):
#         self.track = []

#     def addRange(self, left, right):
#         start = bisect.bisect_left(self.track, left)
#         end = bisect.bisect_right(self.track, right)
        
#         subtrack = []
#         if start % 2 == 0:
#             subtrack.append(left)
#         if end % 2 == 0:
#             subtrack.append(right)
			
#         self.track[start:end] = subtrack

#     def removeRange(self, left, right):
#         start = bisect.bisect_left(self.track, left)
#         end = bisect.bisect_right(self.track, right)
        
#         subtrack = []
#         if start % 2 == 1:
#             subtrack.append(left)
#         if end % 2 == 1:
#             subtrack.append(right)
			
#         self.track[start:end] = subtrack
		
#     def queryRange(self, left, right):
#         start = bisect.bisect_right(self.track, left)
#         end = bisect.bisect_left(self.track, right)
		
#         return start == end and start % 2 == 1



# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)