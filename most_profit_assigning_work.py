# 826. Most Profit Assigning Work
# You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:
#     difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
#     worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
# Every worker can be assigned at most one job, but one job can be completed multiple times.
#     For example, if three workers attempt the same job that pays $1, then the total profit will be $3. 
# If a worker cannot complete any job, their profit is $0.
# Return the maximum profit we can achieve after assigning the workers to the jobs.
# Example 1:
# Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
# Output: 100
# Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
# Example 2:
# Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
# Output: 0
# Constraints:
#     n == difficulty.length
#     n == profit.length
#     m == worker.length
#     1 <= n, m <= 104
#     1 <= difficulty[i], profit[i], worker[i] <= 105

# from typing import List
# class Solution:
#     def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
#         jobs = sorted(zip(difficulty, profit))
#         worker.sort()
#         max_profit = 0
#         current_profit = 0
#         i = 0
#         for w in worker:
#             while i < len(jobs) and jobs[i][0] <= w:
#                 current_profit = max(current_profit, jobs[i][1])
#                 i += 1
#             max_profit += current_profit
#         return max_profit


from bisect import bisect_right
from bisect import bisect
from typing import List
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        jobs = sorted(zip(difficulty, profit))
        diff, prof = zip(*jobs)
        max_prefix_sum = [0] * len(jobs)
        max_prefix_sum[0] = jobs[0][1]
        for i in range(1, len(jobs)):
            max_prefix_sum[i] = max(max_prefix_sum[i-1], jobs[i][1])
        ans = 0
        for w in worker:
            index = bisect_right(diff, w)
            if index > 0:
                ans += max_prefix_sum[index-1]
            else:
                ans += 0
        return ans
    
    
# class Solution:
#     def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

#         result = list(map(lambda x, y: (-x, y), profit, difficulty))
#         worker.sort(reverse=True)
#         heapify(result)
#         seen=set()

#         n=len(worker)
#         ans=0
#         for i in range(n):

#             while result :
#                 val,diff=heappop(result)
#                 if diff<=worker[i]:
#                     ans+=(-val)
#                     heappush(result,(val,diff))
#                     break
#         return ans