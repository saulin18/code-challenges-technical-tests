# 1802. Maximum Value at a Given Index in a Bounded Array
# You are given three positive integers: n, index, and maxSum. You want to construct an array 
# nums (0-indexed) that satisfies the following conditions:
#     nums.length == n
#     nums[i] is a positive integer where 0 <= i < n.
#     abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
#     The sum of all the elements of nums does not exceed maxSum.
#     nums[index] is maximized.
# Return nums[index] of the constructed array.
# Note that abs(x) equals x if x >= 0, and -x otherwise.
# Example 1:
# Input: n = 4, index = 2,  maxSum = 6
# Output: 2
# Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
# There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
# Example 2:
# Input: n = 6, index = 1,  maxSum = 10
# Output: 3
# Constraints:

#     1 <= n <= maxSum <= 109
#     0 <= index < n

class Solution:
   def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        left = 1
        right = maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if self._is_valid(n, index, maxSum, mid):
                left = mid
            else:
                right = mid - 1
        return left 
    
   def _side_sum(self, peak: int, count: int) -> int:
        """Min sum of `count` elements descending from peak by at most 1 per step (floor 1)."""
        if count == 0:
            return 0
        if peak > count:
            # mid-1, mid-2, ..., mid-count — arithmetic series, never hits 1
            return (2 * peak - count - 1) * count // 2
        # Hits floor 1: (mid-1)+...+1, then the rest are 1s
        return peak * (peak - 1) // 2 + (count - peak + 1)

   def _is_valid(self, n: int, index: int, maxSum: int, mid: int) -> bool:
        total = mid + self._side_sum(mid, index) + self._side_sum(mid, n - index - 1)
        return total <= maxSum
        
    
    
    
# class Solution:
#     def maxValue(self, n: int, index: int, maxSum: int) -> int:
#         def calc_sum(index, value):
#             sum_val = 0
#             if value > index:
#                 sum_val = (value) * (value + 1) // 2 - (value - index - 1) * (value - index) // 2
#             else:
#                 sum_val = ((value) * (value + 1) // 2) + (index - value + 1)
#             return sum_val

#         l, r = 0, maxSum + 1
#         while r - l > 1:
#             mid = l + (r - l) // 2

#             curr_sum = calc_sum(index, mid)
#             curr_sum += calc_sum(n - index - 2, mid - 1)
            
#             if curr_sum <= maxSum:
#                 l = mid
#             else:
#                 r = mid
#         return l