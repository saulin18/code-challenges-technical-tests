
# A staircase is given with a non-negative cost per each step.
# Once you pay the cost, you can either climb one or two steps.
# Create a solution to find the minimum sum of costs to reach the top.
# You can start at either of the first two steps.
# Examples
# Stairs: [0, 2, 2, 1]
# Step 0: Start on first step
# Step 1: Pay 0 and climb two steps to reach the third step
# Step 2: Pay 2 and climb two steps to reach the top
# Total spent: 2
# Stairs: [0, 2, 3, 2]
# Step 0: Start on first step
# Step 1: Pay 0 and climb two steps to reach the third step
# Step 2: Pay 3 and climb two steps to reach the top
# Total spent: 3
# Stairs: [10, 15, 20]
# Step 0: Start on the second step
# Step 1: Pay 15 and climb two steps to reach the top
# Total spent: 15
# Stairs [0, 0, 0, 0, 0, 0]
# Take any path, because every step is free!
# Stairs [0, 1, 2, 0, 1, 2]
# Step 0: Start on the second step
# Step 1: Pay 1 and climb two steps to reach the fourth step
# Step 2: Pay 0 and climb one step to reach the fifth step
# Step 3: Pay 1 and climb two steps to reach the top
# Total spent: 2
# Notes
# 2 <= number of steps <= 1000

def climbing_stairs(cost):
    n = len(cost)
    dp = [float('inf')] * n 
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
            
    return min(dp[n - 1], dp[n - 2])


# def climbing_stairs(cost):
#     a = b = 0
#     for c in cost:
#         a, b = b, min(a, b) + c
#     return min(a, b)
        