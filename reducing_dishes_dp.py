# 1402. Reducing Dishes
# A chef has collected data on the satisfaction level of his n
# dishes. Chef can cook any dish in 1 unit of time.

# Like-time coefficient of a dish is defined as the time taken to cook that dish including previous
# dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

# Return the maximum sum of like-time coefficient that the chef can obtain
# after preparing some amount of dishes.

# Dishes can be prepared in any order and the chef can discard some
# dishes to get this maximum value.
# Example 1:
# Input: satisfaction = [-1,-8,0,5,-9]
# Output: 14
# Explanation: After Removing the second and last dish, the maximum total like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
# Each dish is prepared in one unit of time.
# Example 2:
# Input: satisfaction = [4,3,2]
# Output: 20
# Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
# Example 3:
# Input: satisfaction = [-1,-4,-5]
# Output: 0
# Explanation: People do not like the dishes. No dish is prepared.
# Constraints:
# n == satisfaction.length
# 1 <= n <= 500
# -1000 <= satisfaction[i] <= 1000


from typing import List


# class Solution:
#     def maxSatisfaction(self, satisfaction: List[int]) -> int:
#         satisfaction.sort()
#         n = len(satisfaction)

#         def recursive(index: int, quantity: int, memo: dict) -> int:
#             if index == n:
#                 return 0

#             if (index, quantity) in memo:
#                 return memo[(index, quantity)]

#             skip = recursive(index + 1, quantity, memo)
#             take = satisfaction[index] * (quantity + 1) + recursive(
#                 index + 1, quantity + 1, memo
#             )
#             memo[(index, quantity)] = max(skip, take)
#             return memo[(index, quantity)]

#         return recursive(0, 0, {})

# We can do it in a greedy approach

def maxSatisfaction(satisfaction: List[int]) -> int:
    satisfaction.sort()
    n = len(satisfaction)

    max_satisfaction = 0
    current_satisfation = 0
    for index in range(n - 1, -1, -1):
        current_satisfation += satisfaction[index]
        if current_satisfation > 0:
            max_satisfaction = max(
                max_satisfaction, max_satisfaction + current_satisfation
            )
        else:
            break

    return max_satisfaction


print(maxSatisfaction([-1, -8, 0, 5, -9]))
