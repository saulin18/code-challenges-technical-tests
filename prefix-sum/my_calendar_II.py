# 731. My Calendar II
# You are implementing a program to use as your calendar. We can add a new event if
# adding the event will not cause a triple booking.
# A triple booking happens when three events have some non-empty intersection
#  (i.e., some moment is common to all the three events.).
# The event can be represented as a pair of integers startTime and endTime that represents a booking
# on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.
# Implement the MyCalendarTwo class:
# MyCalendarTwo() Initializes the calendar object.
# boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar
# successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
# Example 1:
# Input
# ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
# [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
# Output
# [null, true, true, true, false, true, true]
# Explanation
# MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
# myCalendarTwo.book(10, 20); // return True, The event can be booked.
# myCalendarTwo.book(50, 60); // return True, The event can be booked.
# myCalendarTwo.book(10, 40); // return True, The event can be double booked.
# myCalendarTwo.book(5, 15);  // return False, The event cannot be booked, because it would result in a triple booking.
# myCalendarTwo.book(5, 10); // return True, The event can be booked, as it does not use time 10 which is already double booked.
# myCalendarTwo.book(25, 55); // return True, The event can be booked, as the time in [25, 40) will be double booked with the
# third event, the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
# Constraints:
# 0 <= start < end <= 109
# At most 1000 calls will be made to book.


from collections import defaultdict


class MyCalendarTwo:
    def __init__(self):
        self.tree_map = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> bool:
        self.tree_map[startTime] += 1
        self.tree_map[endTime] -= 1

        running_sum = 0
        for time in sorted(self.tree_map.keys()):
            running_sum += self.tree_map[time]
            if running_sum > 2:
                self.tree_map[startTime] -= 1
                self.tree_map[endTime] += 1
                return False
        return True


# class MyCalendarTwo:
#     def __init__(self):
#         self.overlaps = []
#         self.calendar = []

#     def book(self, start, end):
#         for i, j in self.overlaps:
#             if start < j and end > i:
#                 return False
#         for i, j in self.calendar:
#             if start < j and end > i:
#                 self.overlaps.append((max(start, i), min(end, j)))
#         self.calendar.append((start, end))
#         return True


# class MyCalendarTwo:

#     def __init__(self):
#         self.bookings = []
#         self.overlap_bookings = []

#     def book(self, start: int, end: int) -> bool:
#         # Check if the new booking overlaps with any double-booked booking.
#         for booking in self.overlap_bookings:
#             if self.does_overlap(booking[0], booking[1], start, end):
#                 return False

#         # Add any new double overlaps that the current booking creates.
#         for booking in self.bookings:
#             if self.does_overlap(booking[0], booking[1], start, end):
#                 self.overlap_bookings.append(
#                     self.get_overlapped(booking[0], booking[1], start, end)
#                 )

#         # Add the new booking to the list of bookings.
#         self.bookings.append((start, end))
#         return True

#     # Return True if the booking [start1, end1) & [start2, end2) overlaps.
#     def does_overlap(
#         self, start1: int, end1: int, start2: int, end2: int
#     ) -> bool:
#         return max(start1, start2) < min(end1, end2)

#     # Return the overlapping booking between [start1, end1) & [start2, end2).
#     def get_overlapped(
#         self, start1: int, end1: int, start2: int, end2: int
#     ) -> tuple:
#         return max(start1, start2), min(end1, end2)
