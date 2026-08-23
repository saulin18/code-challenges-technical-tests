# 729. My Calendar I

# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.
# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).
# The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open
#  interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.
# Implement the MyCalendar class:
# MyCalendar() Initializes the calendar object.
# boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without 
# causing a double booking. Otherwise, return false and do not add the event to the calendar.
# Example 1:
# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]
# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time
#  less than 20, but not including 20.
# Constraints:
# 0 <= start < end <= 109
# At most 1000 calls will be made to book.

# class MyCalendar:

#     def __init__(self):
#         self.overlaps: list[tuple[int, int]] = []
        

#     def book(self, startTime: int, endTime: int) -> bool:
#         n = len(self.overlaps)
#         if n == 0:
#             self.overlaps.append((startTime, endTime))
#         # Check overlapping first
#         for i in range(n):
#             start, end = self.overlaps[i]

#             if self.does_overlap(start, end, startTime, endTime):
#                 return False
#         self.overlaps.append((startTime, endTime))
#         return True

#     def does_overlap(self, start, end, startTime, endTime) -> bool:
#         return max(start, startTime) < min(end, endTime)

#     def get_overlap_interval(self, start, end, startTime, endTime) -> tuple[int, int]:
#         return (max(start, startTime), min(end, endTime))

from bisect import bisect_left
from sortedcontainers import SortedDict
class MyCalendar:

    def __init__(self):
        self.overlaps: SortedDict[int, int] = SortedDict()
        

    def book(self, startTime: int, endTime: int) -> bool:
        if self.overlaps:
            insert_point = self.overlaps.bisect_left(startTime)
            if insert_point > 0 and self.overlaps.peekitem(insert_point - 1)[1] > startTime:
                return False
            if insert_point < len(self.overlaps) and self.overlaps.peekitem(insert_point)[0] < endTime:
                return False
            self.overlaps[startTime] = endTime
            return True
        self.overlaps[startTime] = endTime
        return True
    
    
# import bisect

# class MyCalendar:

#     #This with a set leads to a TLE at high numbers

#     def __init__(self):
#         #the event must be a pair of integers which is kind of interesting
#         self.intervals = []        

#     def book(self, startTime: int, endTime: int) -> bool:
        
#         idx_right = bisect.bisect_right(self.intervals, (startTime, endTime))

#         idx_left = idx_right - 1
        
#         if self.intervals:
#             if len(self.intervals) > idx_right:
#                 nxt = self.intervals[idx_right]
#                 if nxt[0] < endTime:
#                     return False
#             if idx_left >= 0:
#                 prev = self.intervals[idx_left]
#                 if prev[1] > startTime:
#                     return False
        
#         bisect.insort(self.intervals, (startTime, endTime))
#         return True
    

    #if you store everything in a sorted list based on the start, then you know if something overlaps because the
    # start is before the end or because your end is after the next start
    
    
# class MyCalendar:

#     def __init__(self):
#         self.books = []

#     def book(self, startTime: int, endTime: int) -> bool:
#         new_booking = [startTime, endTime]
        
#         index = bisect_left(self.books, new_booking)

#         if index > 0:
#             previous_end = self.books[index - 1][1]
#             if previous_end > startTime:
#                 return False
        
#         if index < len(self.books):
#             next_start = self.books[index][0]
#             if next_start < endTime:
#                 return False

#         self.books.insert(index, new_booking)
#         return True




# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
