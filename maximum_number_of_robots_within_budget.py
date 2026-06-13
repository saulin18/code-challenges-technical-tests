# 2398. Maximum Number of Robots Within Budget
# You have n robots. You are given two 0-indexed integer arrays,
# chargeTimes and runningCosts, both of length n. The ith robot
# costs chargeTimes[i] units to charge and costs runningCosts[i]
# units to run. You are also given an integer budget.

# The total cost of running k chosen robots is equal to
# max(chargeTimes) + k * sum(runningCosts), where max(chargeTimes)
# is the largest charge cost among the k robots and sum(runningCosts)
# is the sum of running costs among the k robots.

# Return the maximum number of consecutive robots you can run such
# that the total cost does not exceed budget.

# Example 1:

# Input: chargeTimes = [3,6,1,3,4], runningCosts =
# [2,1,3,4,5], budget = 25
# Output: 3
# Explanation:
# It is possible to run all individual and consecutive pairs of robots within budget.
# To obtain answer 3, consider the first 3 robots. The total cost will be
# max(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24 which is less than 25.
# It can be shown that it is not possible to run more than
# 3 consecutive robots within budget, so we return 3.
# Example 2:

# Input: chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19
# Output: 0
# Explanation: No robot can be run that does not exceed the budget, so we return 0.


# Constraints:

# chargeTimes.length == runningCosts.length == n
# 1 <= n <= 5 * 104
# 1 <= chargeTimes[i], runningCosts[i] <= 105
# 1 <= budget <= 1015


from typing import List
from collections import deque

class Solution:
    def maximumRobots(
        self, chargeTimes: List[int], runningCosts: List[int], budget: int
    ) -> int:

        left = 0
        N = len(chargeTimes)
        right = len(runningCosts)

        def can(k: int) -> bool:
            """
            The total cost of running k chosen robots is equal to
            max(chargeTimes) + k * sum(runningCosts), where max(chargeTimes)
            is the largest charge cost among the k robots and sum(runningCosts)
            is the sum of running costs among the k robots.
            """

            if k == 0:
                return True

            if k > N:
                return False

            # We will be using a sliding window approach
            start = 0
            wsum = 0
            max_charge_time = 0
            max_charge_time_deque = deque()

            for end in range(N):
                while max_charge_time_deque and chargeTimes[max_charge_time_deque[-1]] < chargeTimes[end]:
                    max_charge_time_deque.pop()
                max_charge_time_deque.append(end)
                max_charge_time = chargeTimes[max_charge_time_deque[0]]
                wsum += runningCosts[end]

                if end - start + 1 == k and wsum * k + max_charge_time <= budget:
                    return True

                while end - start + 1 > k:
                    index_going_out = start
                    start += 1
                    while max_charge_time_deque and max_charge_time_deque[0] < start:
                        max_charge_time_deque.popleft()
                    max_charge_time = chargeTimes[max_charge_time_deque[0]]
                    wsum -= runningCosts[index_going_out]
                   

                    if end - start + 1 == k and wsum * k + max_charge_time <= budget:
                        return True

            return False

        while left < right:
            mid = (left + right + 1) // 2

            if can(mid):
                left = mid
            else:
                right = mid - 1

        return left


# class Solution:
#     def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
#         from collections import deque
#         n = len(chargeTimes)
#         max_charge = deque()
#         total_running_cost = 0
#         left = 0
#         max_robots = 0
        
#         for right in range(n):
#             total_running_cost += runningCosts[right]
            
#             while max_charge and chargeTimes[max_charge[-1]] <= chargeTimes[right]:
#                 max_charge.pop()
#             max_charge.append(right)
            
#             while max_charge and (chargeTimes[max_charge[0]] + (right - left + 1) * total_running_cost) > budget:
#                 if max_charge[0] == left:
#                     max_charge.popleft()
#                 total_running_cost -= runningCosts[left]
#                 left += 1
            
#             if max_charge:
#                 max_robots = max(max_robots, right - left + 1)
        
#         return max_robots


# from collections import deque

# class Solution:
#     def maximumRobots(self, chargeTimes: list[int], runningCosts: list[int], budget: int) -> int:
#         left = 0
#         max_robots = 0
#         current_running_sum = 0
#         max_chg = deque()  # Stores indices, maintains decreasing order of chargeTimes
        
#         for right in range(len(chargeTimes)):
#             # 1. Add current robot's running cost to the window sum
#             current_running_sum += runningCosts[right]
            
#             # 2. Maintain the monotonic deque (decreasing order of charge times)
#             while max_chg and chargeTimes[max_chg[-1]] <= chargeTimes[right]:
#                 max_chg.pop()
#             max_chg.append(right)
            
#             # 3. Calculate current window size (k)
#             k = right - left + 1
            
#             # 4. If total cost exceeds budget, shrink window from the left
#             while max_chg and (chargeTimes[max_chg[0]] + k * current_running_sum) > budget:
#                 # Remove left robot's running cost
#                 current_running_sum -= runningCosts[left]
                
#                 # If the max charge time element is leaving the window, pop it
#                 if max_chg[0] == left:
#                     max_chg.popleft()
                
#                 left += 1
#                 k -= 1  # Window shrunk, so k decreases by 1
            
#             # 5. Update max consecutive robots found so far
#             max_robots = max(max_robots, right - left + 1)
            
#         return max_robots


# class Solution:
#     def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
#         n = len(chargeTimes)
#         q = deque()
#         left = curr_sum = 0
#         for right in range(n):
#             curr_sum += runningCosts[right]

#             while q and q[-1] < chargeTimes[right]:
#                 q.pop()
#             q.append(chargeTimes[right])
            
#             if q[0] + (right - left + 1) * curr_sum > budget:
#                 if q[0] == chargeTimes[left]:
#                     q.popleft()
#                 curr_sum -= runningCosts[left]
#                 left += 1
        
#         return n - left