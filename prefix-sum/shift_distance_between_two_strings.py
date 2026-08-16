# 3361. Shift Distance Between Two Strings
# Medium
# You are given two strings s and t of the same length, and
# two integer arrays nextCost and previousCost.
# In one operation, you can pick any index i of s, and perform either one of the following actions:
#     Shift s[i] to the next letter in the alphabet. If s[i] == 'z', you
# should replace it with 'a'. This operation costs nextCost[j] where j is the index
# of s[i] in the alphabet.
#     Shift s[i] to the previous letter in the alphabet. If s[i] == 'a', you should
# replace it with 'z'. This operation costs previousCost[j] where j is the index of
# s[i] in the alphabet.
# The shift distance is the minimum total cost of operations required to transform s into t.
# Return the shift distance from s to t.
# Example 1:
# Input: s = "abab", t = "baba",
# nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Output: 2
# Explanation:
#     We choose index i = 0 and shift s[0] 25 times to the previous character for a total cost of 1.
#     We choose index i = 1 and shift s[1] 25 times to the next character for a total cost of 0.
#     We choose index i = 2 and shift s[2] 25 times to the previous character for a total cost of 1.
#     We choose index i = 3 and shift s[3] 25 times to the next character for a total cost of 0.
# Example 2:
# Input: s = "leet", t = "code",
# nextCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
# previousCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# Output: 31
# Explanation:

#     We choose index i = 0 and shift s[0] 9 times to the previous character for a total cost of 9.
#     We choose index i = 1 and shift s[1] 10 times to the next character for a total cost of 10.
#     We choose index i = 2 and shift s[2] 1 time to the previous character for a total cost of 1.
#     We choose index i = 3 and shift s[3] 11 times to the next character for a total cost of 11.
# Constraints:
#     1 <= s.length == t.length <= 105
#     s and t consist only of lowercase English letters.
#     nextCost.length == previousCost.length == 26
#     0 <= nextCost[i], previousCost[i] <= 109


from typing import List


class Solution:
    def shiftDistance(
        self, s: str, t: str, nextCost: List[int], previousCost: List[int]
    ) -> int:

        min_costs = [[float("inf") if i != j else 0 for i in range(26)] for j in range(26)]

        # for i in range(26):
        #     current = i
        #     previous = i
        #     forward_cost = 0
        #     backward_cost = 0
        #     for _ in range(25):
        #         forward_cost += nextCost[current]
        #         backward_cost += previousCost[previous]
        #         current = (current + 1) % 26 # next
        #         previous = (previous - 1) % 26 # previous

        #         min_costs[i][current] = min(min_costs[i][current], forward_cost)
        #         min_costs[i][previous] = min(min_costs[i][previous], backward_cost)
        
        for i in range(26):
            for j in range(26):
                if i == j:
                    continue
                
                forward_cost = 0
                backward_cost = 0
                
                # Calculate forward cost
                current = i
                while current != j:
                    forward_cost += nextCost[current]
                    current = (current + 1) % 26 # next

                previous = i
                while previous != j:
                    backward_cost += previousCost[previous]
                    previous = (previous - 1) % 26 # previous

                min_costs[i][j] = min(forward_cost, backward_cost)

        res = 0
        for i in range(len(s)):
            res += min_costs[ord(s[i]) - ord("a")][ord(t[i]) - ord("a")]

        return int(res)


# class Solution:
#     def shiftDistance(
#         self, s: str, t: str, nextCost: List[int], previousCost: List[int]
#     ) -> int:
#         next_costs_prefix_sum = [0] * 27
#         previous_costs_prefix = [0] * 27

#         for i in range(26):
#             next_costs_prefix_sum[i + 1] = next_costs_prefix_sum[i] + nextCost[i]
#             previous_costs_prefix[i + 1] = previous_costs_prefix[i] + previousCost[i]

#         n = len(s)
#         res = 0
#         for i in range(n):
#             if s[i] == t[i]:
#                 continue

#             index_of_s_in_alph = (ord(s[i]) - ord("a")) % 26
#             index_of_t_in_alph = (ord(t[i]) - ord("a")) % 26

#             next_cost = (
#                 (
#                     next_costs_prefix_sum[index_of_t_in_alph]
#                     - next_costs_prefix_sum[index_of_s_in_alph]
#                 )
#                 if index_of_s_in_alph < index_of_t_in_alph
#                 else (
#                     # with wrap
#                     next_costs_prefix_sum[26]
#                     - next_costs_prefix_sum[index_of_s_in_alph]
#                     + next_costs_prefix_sum[index_of_t_in_alph]
#                 )
#             )
#             previous_cost = (
#                 (
#                     previous_costs_prefix[index_of_s_in_alph + 1]
#                     - previous_costs_prefix[index_of_t_in_alph + 1]
#                 )
#                 if index_of_s_in_alph > index_of_t_in_alph
#                 else (
#                     # with wrap
#                     previous_costs_prefix[index_of_s_in_alph + 1]
#                     + (
#                         previous_costs_prefix[26]
#                         - previous_costs_prefix[index_of_t_in_alph + 1]
#                     )
#                 )
#             )

#             res += min(next_cost, previous_cost)

#         return res


# class Solution:
#     def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
#         nxt_sum = list(accumulate(nextCost + nextCost, initial=0))
#         pre_sum = list(accumulate(previousCost + previousCost, initial=0))
#         res = 0

#         for a, b in zip(s, t):
#             x = ord(a) - ord('a')
#             y = ord(b) - ord('a')

#             nxt = nxt_sum[y + 26 if y < x else y] - nxt_sum[x]
#             pre = pre_sum[(x + 26 if x < y else x) + 1] - pre_sum[y + 1]

#             res += min(nxt, pre)

#         return res


# class Solution:
#     def shiftDistance(
#         self,
#         s: str,
#         t: str,
#         nextCost: List[int],
#         previousCost: List[int]
#     ) -> int:
#         forward = [[0] * 26 for _ in range(26)]
#         backward = [[0] * 26 for _ in range(26)]
#         for start in range(26):
#             current = start
#             cost = 0
#             for _ in range(25):
#                 cost += nextCost[current]
#                 current = (current + 1) % 26
#                 forward[start][current] = cost
#             current = start
#             cost = 0
#             for _ in range(25):
#                 cost += previousCost[current]
#                 current = (current - 1) % 26
#                 backward[start][current] = cost
#         ans = 0
#         for first, second in zip(s, t):
#             start = ord(first) - 97
#             end = ord(second) - 97
#             ans += min(
#                 forward[start][end],
#                 backward[start][end]
#             )
#         # LC3361_FIX
#         return ans
