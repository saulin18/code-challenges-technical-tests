# 1854. Maximum Population Year
# You are given a 2D integer array logs where each
# logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.
# The population of some year x is the number of people alive during
# that year. The ith person is counted in year x's population if
# x is in the inclusive range [birthi, deathi - 1]. Note that the person
# is not counted in the year that they die.
# Return the earliest year with the maximum population.
# Example 1:
# Input: logs = [[1993,1999],[2000,2010]]
# Output: 1993
# Explanation: The maximum population is 1, and 1993 is the
# earliest year with this population.
# Example 2:
# Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
# Output: 1960
# Explanation:
# The maximum population is 2, and it had happened in years 1960 and 1970.
# The earlier year between them is 1960.
# Constraints:
#     1 <= logs.length <= 100
#     1950 <= birthi < deathi <= 2050

from typing_extensions import List
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        min_year = min(log[0] for log in logs)
        max_year = max(log[1] for log in logs)
        diff = [0] * (max_year + 1)

        for start_year, end_year in logs:
            diff[start_year] +=1

            diff[end_year] -=1

        max_population = float('-inf')
        min_year_by_pop = float('inf')
        for i in range(min_year, max_year + 1):
            diff[i] += diff[i - 1]
            if diff[i] > max_population:
                min_year_by_pop = i
            max_population = max(max_population, diff[i])        
        

        return int(min_year_by_pop)



# class Solution:
#     def maximumPopulation(self, logs: List[List[int]]) -> int:
        
#         mn = float("inf")
#         mx = float("-inf")
#         for s, e in logs:
#             mn = min(mn, s)
#             mx = max(mx, e)

#         count = [0] * (mx + 1)
#         for s, e in logs:
#             count[s] += 1
#             count[e] -= 1
        
#         guests = 0
#         result = 0
#         for i in range(mn, mx + 1):
#             count[i] += count[i - 1]
#             if count[i] > guests:
#                 guests = count[i]
#                 result = i
        
#         return result