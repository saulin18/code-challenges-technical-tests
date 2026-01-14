# 491. Non-decreasing Subsequences
# Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements.
# You may return the answer in any order.

# Example 1:

# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
# Example 2:

# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]
# Constraints:
# 1 <= nums.length <= 15
# -100 <= nums[i] <= 100


def findSubsequences(nums):
   
    without_duplicates = set()
    res = []
   
    def backtrack(index: int, actual_perm: list[int]):
       
        if len(actual_perm) >= 2 and tuple(actual_perm) not in without_duplicates:
           without_duplicates.add(tuple(actual_perm)) 
           res.append(actual_perm[:])
           
        
        for end in range(index, len(nums)):
            if len(actual_perm) == 0 or nums[end] >= actual_perm[-1]:
                actual_perm.append(nums[end])
                backtrack(end + 1, actual_perm)
                actual_perm.remove(nums[end])
            
    backtrack(0, [])
    
    return res
          
print(findSubsequences([4,4,3,2,1]))     
           