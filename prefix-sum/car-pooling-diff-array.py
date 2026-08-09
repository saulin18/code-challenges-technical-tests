# 1094. Car Pooling
# There is a car with capacity empty seats. The vehicle only drives
# east (i.e., it cannot turn around and drive west).
# You are given the integer capacity and an array trips where trips[i]
# = [numPassengersi, fromi, toi] indicates that the ith trip has
# numPassengersi passengers and the locations to pick them up and drop
# them off are fromi and toi respectively. The locations are given as the number
# of kilometers due east from the car's initial location.
# Return true if it is possible to pick up and drop off all passengers for
# all the given trips, or false otherwise.
# Example 1:
# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false
# Example 2:
# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true
# Constraints:
#     1 <= trips.length <= 1000
#     trips[i].length == 3
#     1 <= numPassengersi <= 100
#     0 <= fromi < toi <= 1000
#     1 <= capacity <= 105

from typing_extensions import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001
        for num_passengers, from_location, to_location in trips:
            diff[from_location] += num_passengers
            diff[to_location] -= num_passengers
        for i in range(1001):
           
            diff[i] += diff[i - 1]
            if diff[i] > capacity:
                return False
        return True
    
    
# best approach:

# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool
#         maxDist = max(trips, key = lambda x: x[2])[2]
#         minDist = min(trips, key = lambda x: x[1])[1]

#         # print(maxDist)
#         # print(minDist)
#         diff = [0] * (maxDist + 1)
#         for pasng, l, r in trips:
#             diff[l] += pasng
#             if r + 1 < maxDist + 1:
#                 diff[r] -= pasng
#         # print(diff)
#         for i in range(minDist, maxDist + 1):
#             diff[i] += diff[i - 1]
#             if diff[i] > capacity:
#                 return False
#         return True

# The only difference is that it's using the max and min of the trips to
# create the diff array. This is a more efficient approach because it's not
# creating a diff array for every possible location.