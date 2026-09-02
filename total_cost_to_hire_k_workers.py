# 2462. Total Cost to Hire K Workers
# You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.
# You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:
#     You will run k sessions and hire exactly one worker in each session.
#     In each hiring session, choose the worker with the lowest cost from either the first candidates
# workers or the last candidates workers. Break the tie by the smallest index.
#         For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we
#  choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
#         In the second hiring session, we will choose 1st worker because they have the same lowest cost
# as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed
# in the process.
#     If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them.
#  Break the tie by the smallest index.
#     A worker can only be chosen once.
# Return the total cost to hire exactly k workers.
# Example 1:
# Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
# Output: 11
# Explanation: We hire 3 workers in total. The total cost is initially 0.
# - In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by
# the smallest index, which is 3. The total cost = 0 + 2 = 2.
# - In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4).
#  The total cost = 2 + 2 = 4.
# - In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3).
#  The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
# The total hiring cost is 11.
# Example 2:
# Input: costs = [1,2,4,1], k = 3, candidates = 3
# Output: 4
# Explanation: We hire 3 workers in total. The total cost is initially 0.
# - In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost is 1, and we break the tie by the
#  smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the
# first and last 3 workers.
# - In the second hiring round we choose the worker from [2,4,1]. The lowest cost is 1 (index 2).
#  The total cost = 1 + 1 = 2.
# - In the third hiring round there are less than three candidates. We choose the worker from the
# remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
# The total hiring cost is 4.
# Constraints:
#     1 <= costs.length <= 105
#     1 <= costs[i] <= 105
#     1 <= k, candidates <= costs.length


import heapq


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)
        total_cost = 0
        left_min_heap: list[tuple[int, int]] = [
            (costs[i], i) for i in range(candidates)
        ]
        right_min_heap: list[tuple[int, int]] = [
            (costs[i], i) for i in range(n - candidates, n)
        ]
        heapq.heapify(left_min_heap)
        heapq.heapify(right_min_heap)
        hired = set()

        left = candidates
        right = n - candidates - 1
        for i in range(k):

            while left_min_heap and left_min_heap[0][1] in hired:
                heapq.heappop(left_min_heap)
            while right_min_heap and right_min_heap[0][1] in hired:
                heapq.heappop(right_min_heap)

            should_pop_left = (
                left_min_heap and left_min_heap[0] <= right_min_heap[0]
                if right_min_heap
                else True
            )

            if should_pop_left:
                element_going_out = heapq.heappop(left_min_heap)
                hired.add(element_going_out[1])
                total_cost += element_going_out[0]
                if left <= right and left not in hired:
                    heapq.heappush(left_min_heap, (costs[left], left))
                    left += 1
            else:
                element_going_out = heapq.heappop(right_min_heap)
                hired.add(element_going_out[1])
                total_cost += element_going_out[0]
                if right >= left and right not in hired:
                    heapq.heappush(right_min_heap, (costs[right], right))
                    right -= 1
        return total_cost

# class Solution:
#     def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
#         n=len(costs)
#         heap=[]
#         left = 0
#         right = n - 1
#         ans=0
#         for _ in range(candidates):
#             heapq.heappush(heap,(costs[left],left))
#             left+=1
#         for _ in range(candidates):
#             if left<=right:
#                 heapq.heappush(heap,(costs[right],right))
#                 right-=1
#         for _ in range(k):
#             cost, index = heapq.heappop(heap)
#             ans += cost
#             if index < left:
#                 if left <= right:
#                     heapq.heappush(heap, (costs[left], left))
#                     left += 1
#             else:
#                 if left <= right:
#                     heapq.heappush(heap, (costs[right], right))
#                     right -= 1

#         return ans

# class Solution:
#     def totalCost(self, costs: list[int], k: int, candidates: int) -> int:


#         heap = []
#         n = len(costs)
#         for i in range(candidates):
#             heap.append((costs[i], 0))

#         for i in range(max(candidates, n - candidates), n):
#             heap.append((costs[i], 1))

#         heapify(heap)

#         res = 0
#         next_left , next_right = candidates, n - candidates -1
#         while k > 0:
#             cur_cost, cur_id = heappop(heap)
#             res += cur_cost
#             k -=1

#             if next_left <= next_right:
#                 if cur_id == 0:
#                     heappush(heap, (costs[next_left], 0))
#                     next_left += 1
#                 else:
#                     heappush(heap, (costs[next_right], 1))
#                     next_right -=1
#         return res
