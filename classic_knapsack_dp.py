# Packing your backpack
# You're about to go on a trip around the world! On this trip you're bringing your trusted
# backpack, that anything fits into. The bad news is that the airline has informed you that
# your luggage cannot exceed a certain amount of weight.
# To make sure you're bringing your most valuable items on this journey you've decided to 
# give all your items a score that represents how valuable this item is to you. It's your 
# job to pack your bag so that you get the most value out of the items that you decide to bring.
# Your input will consist of two arrays, one for the scores and one for the weights. 
# Your input will always be valid lists of equal length, so you don't have to worry 
# about verifying your input.
# You'll also be given a maximum weight. This is the weight that your backpack cannot exceed.
# For instance, given these inputs:
# scores = [15, 10, 9, 5]
# weights = [1, 5, 3, 4]
# capacity = 8
# The maximum score will be 29. This number comes from bringing items 1, 3 and 4.
# Note: Your solution will have to be efficient as the running time of your algorithm will be put to a test.

def pack_backpack(scores, weights, capacity):
    n = len(scores)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + scores[i-1])
            else:
                dp[i][j] = dp[i-1][j]
            
    return dp[n][capacity]

def recursive_pack_backpack(scores, weights, capacity, n):
    memo = {}
    if n == 0 or capacity == 0:
        return 0
    
    def recurse(index: int, remaining_capacity: int, memo: dict) -> int:
        if (index, remaining_capacity) in memo:
            return memo[(index, remaining_capacity)]
        
        if weights[index] > remaining_capacity:
            memo[(index, remaining_capacity)] = recurse(index - 1, remaining_capacity, memo)
            return memo[(index, remaining_capacity)]
        
        memo[(index, remaining_capacity)] = max(
            recurse(index - 1, remaining_capacity, memo),
            recurse(index - 1, remaining_capacity - weights[index], memo) + scores[index]
        )
        return memo[(index, remaining_capacity)]
    return recurse(n - 1, capacity, memo)