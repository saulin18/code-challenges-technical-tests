# 2389. Longest Subsequence With Limited Sum

# You are given an integer array nums of length n, and 
# an integer array queries of length m.

# Return an array answer of length m where answer[i] is the
# maximum size of a subsequence that you can take from nums
# such that the sum of its elements is less than or equal to queries[i].

# A subsequence is an array that can be derived from another 
# array by deleting some or no elements without changing the order 
# of the remaining elements.

# Example 1:
# Input: nums = [4,5,2,1], queries = [3,10,21]
# Output: [2,3,4]
# Explanation: We answer the queries as follows:
# - The subsequence [2,1] has a sum less than or equal to 3. It can 
# be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
# - The subsequence [4,5,1] has a sum less than or equal to 10. It
# can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
# - The subsequence [4,5,2,1] has a sum less than or equal to 21.
# It can be proven that 4 is the maximum size of such a subsequence, 
# so answer[2] = 4.

# Example 2:
# Input: nums = [2,3,4,5], queries = [1]
# Output: [0]
# Explanation: The empty subsequence is the only subsequence that has
# a sum less than or equal to 1, so answer[0] = 0.
# Constraints:

# n == nums.length
# m == queries.length
# 1 <= n, m <= 1000
# 1 <= nums[i], queries[i] <= 106
from typing import List
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans: List[int] = [0] * len(queries)
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        for i in range(len(queries)):
            ans[i] = Solution.binary_search_with_prefix_sum(Solution, i, queries, prefix_sum)
            
        return ans
            
    def binary_search_with_prefix_sum(self, query_index: int, queries: List[int], prefix_sum: List[int]):
       
        index = Solution.binarySearchForMaxVal(Solution, 0, len(prefix_sum) - 1, lambda x: prefix_sum[x] <= queries[query_index])
        return index
    
    
    # bisect right
    def binarySearchForMaxVal(self, lower_bound: int, upper_bound: int, feasible: callable) -> int:
         left, right = lower_bound, upper_bound
         while left <= right:
             mid = (left + right) //2 #round down
             if feasible(mid):
                 left = mid + 1 #check for possible greater values that work
             else:
                 right = mid - 1 #values greater than or equal to mid do not work. Reduce search space to values smaller than mid.
         return left 
     
    # bisect left 
    # def binarySearchForMinVal(self, lower_bound: int, upper_bound: int, feasible: callable) -> int:
    #     left, right = lower_bound, upper_bound
    #     while left < right:
    #         mid = (left + right)//2 #round down
    #         if feasible(mid):
    #             right = mid #check for possible smaller values that work
    #         else:
    #             left = mid + 1 #values smaller than or equal to mid do not work. Reduce search space to values greater than mid.
    #     return left
            
            