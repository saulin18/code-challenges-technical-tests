#40. Combination Sum II
#Medium
#Topics
#premium lock icon
#Companies
#Given a collection of candidate numbers (candidates) and a target number (target), f
# ind all unique combinations in candidates where the candidate numbers sum to target.
#Each number in candidates may only be used once in the combination.
#Note: The solution set must not contain duplicate combinations.
#Example 1:
#Input: candidates = [10,1,2,7,6,1,5], target = 8
#Output: 
#[
#[1,1,6],
#[1,2,5],
#[1,7],
#[2,6]
#]
#Example 2:
#
#Input: candidates = [2,5,2,1,2], target = 5
#Output: 
#[
#[1,2,2],
#[5]
#]
 
def combinationSum2(self, candidates: list[int], target: int):
    
    sorted_candidates = sorted(candidates)
    res = []
 
    def backtrack(target: int, start: int, path: list[int]):
        if sum(path) == target:
            res.append(path[:])
            return
        
        if sum(path) > target:
            return
        
        for index in range(start, len(sorted_candidates)):
                if sorted_candidates[index] != sorted_candidates[index - 1] and index < start: 
                    path.append(sorted_candidates[index])
                    backtrack(target - sorted_candidates[index], index + 1, path)
                    path.remove(sorted_candidates[index])
                
    backtrack(target, 0, [])        
    
    return res