# 1870. Minimum Speed to Arrive on Time
# You are given a floating-point number hour, representing
# the amount of time you have to reach the office. To commute 
# to the office, you must take n trains in sequential order. 
# You are also given an integer array dist of length n, 
# where dist[i] describes the distance (in kilometers) of the ith train ride.

# Each train can only depart at an integer hour, so you may 
# need to wait in between each train ride.

# For example, if the 1st train ride takes 1.5 hours, you must wait 
# for an additional 0.5 hours before you can depart on the 2nd train
# ride at the 2 hour mark.
# Return the minimum positive integer speed (in kilometers per hour)
# that all the trains must travel at for you to reach the office on time,
# or -1 if it is impossible to be on time.

# Tests are generated such that the answer will not exceed 107 
# and hour will have at most two digits after the decimal point.
# Example 1:
# Input: dist = [1,3,2], hour = 6
# Output: 1
# Explanation: At speed 1:
# - The first train ride takes 1/1 = 1 hour.
# - Since we are already at an integer hour, we depart 
# immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
# - Since we are already at an integer hour, we depart 
# immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
# - You will arrive at exactly the 6 hour mark.
# Example 2:

# Input: dist = [1,3,2], hour = 2.7
# Output: 3
# Explanation: At speed 3:
# - The first train ride takes 1/3 = 0.33333 hours.
# - Since we are not at an integer hour, we wait until the 1 hour mark
# to depart. The second train ride takes 3/3 = 1 hour.
# - Since we are already at an integer hour, we depart immediately at
# the 2 hour mark. The third train takes 2/3 = 0.66667 hours.
# - You will arrive at the 2.66667 hour mark.
# Example 3:

# Input: dist = [1,3,2], hour = 1.9
# Output: -1
# Explanation: It is impossible because the earliest the third train
# can depart is at the 2 hour mark.
 

# Constraints:

# n == dist.length
# 1 <= n <= 105
# 1 <= dist[i] <= 105
# 1 <= hour <= 109
# There will be at most two digits after the decimal point in hour.
 
# Discover more
# Online training programs
# programming

import math
from typing import List
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left = 0
        n = len(dist)
        right = 10**7

        def can(x: int) -> bool:

            if x == 0:
                return False

            total_number_of_hours = 0 

            for i, distance in enumerate(dist):

                if i == n - 1:
                    total_number_of_hours += float(distance / x)
                    continue

                total_number_of_hours += math.ceil(distance / x)
            
            return total_number_of_hours <= hour

        while left < right:
            mid = left + (right - left) // 2

            if can(mid):
                right = mid
            else:
                left = mid + 1
        
        return left if can(left) else -1
        
        
# import math

# class Solution:
#     def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
#         # Base Case: It takes at least 1 hour per train for all but the last train.
#         # If the total hours given is less than or equal to the number of wait periods, it's impossible.
#         if len(dist) - 1 >= hour:
#             return -1
        
#         # Binary search range for speed (1 to 10^7 as per problem constraints)
#         left, right = 1, 10**7
#         ans = -1
        
#         while left <= right:
#             mid = (left + right) // 2  # Our "guessed" speed
            
#             # Calculate total time at this 'mid' speed
#             total_time = 0
#             for i in range(len(dist) - 1):
#                 # All trains except the last one round UP to the next integer hour
#                 total_time += math.ceil(dist[i] / mid)
                
#             # The last train doesn't need to round up (no waiting afterwards)
#             total_time += dist[-1] / mid
            
#             # Did we make it on time?
#             if total_time <= hour:
#                 ans = mid          # Save this valid speed!
#                 right = mid - 1    # Try to find an even slower speed that still works
#             else:
#                 left = mid + 1     # We were late! We must go faster.
                
#         return ans