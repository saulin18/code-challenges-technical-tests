
#Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
#
#The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
#
#The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

#Input: candidates = [2,3,6,7], target = 7
#Output: [[2,2,3],[7]]
#Explanation:
#2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
#7 is a candidate, and 7 = 7.
#These are the only two combinations.
#Example 2:
#
#Input: candidates = [2,3,5], target = 8
#Output: [[2,2,2,2],[2,3,3],[3,5]]
#Example 3:
#
#Input: candidates = [2], target = 1
#Output: []
 
def combinationSum(candidates, target, memo = {}):

    if target == 0:
        return []
    
    if target in memo:
        return memo[target]
    
    if target < 0:
        return -1
    
    for i, number in enumerate(candidates):
        remainder = target - candidates
        result = combinationSum(candidates[1:], remainder, memo)
        memo[target] = result
            
    return memo[target]        

def combinationSum(candidates, target):
    
    res = []
    
    def backtrack(remaining, combination, start):
        if remaining == 0: 
            res.append(combination[:])
            return
        
        if remaining < 0:
            return
        
        for i in range(start, len(remaining)):
            combination.append(candidates[i])
            backtrack(remaining - candidates[i], combination, i)
            combination.pop()
    
    backtrack(target, [], 0)
    return res        


def combinationSum(candidates, target, memo={}):
    if target == 0:
        return [[]]  # One way to make 0: use nothing
    
    if target < 0:
        return []  # Can't make negative target
    
    if target in memo:
        return memo[target]
    
    result = []
    for i, number in enumerate(candidates):
        remainder = target - number
        sub_combinations = combinationSum(candidates, remainder, memo)  # Keep all candidates
        
        # For each sub-combination, prepend current number
        for comb in sub_combinations:
            result.append([number] + comb)
    
    memo[target] = result
    return result
