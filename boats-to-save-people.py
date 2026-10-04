# 881. Boats to Save People
# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where
#  each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, 
# provided the sum of the weight of those people is at most limit.
# Return the minimum number of boats to carry every given person.
# Example 1:
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# Example 2:
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# Example 3:
# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
# Constraints:
#     1 <= people.length <= 5 * 104
#     1 <= people[i] <= limit <= 3 * 104


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        
        num_of_boats = 0
        people.sort() 
        left = 0
        right = len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                num_of_boats += 1
            else:
                right -= 1
                num_of_boats += 1
        return num_of_boats
    
    
# class Solution:
#     def numRescueBoats(self, people: list[int], limit: int) -> int:
#         people.sort()
#         l=0
#         b=0
#         r=len(people)-1
#         while l<=r:
#             if people[l]+people[r]<=limit:
#                 l+=1
#             r-=1
#             b+=1
#         return b
            