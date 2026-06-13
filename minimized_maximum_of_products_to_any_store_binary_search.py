# 2064. Minimized Maximum of Products Distributed to Any Store
# You are given an integer n indicating there are n specialty
# retail stores. There are m product types of varying amounts,
# which are given as a 0-indexed integer array quantities,
# where quantities[i] represents the number of products of the ith product type.

# You need to distribute all products to the retail stores
# following these rules:

# A store can only be given at most one product type but can
# be given any amount of it.
# After distribution, each store will have been given some
# number of products (possibly 0). Let x represent the maximum
# number of products given to any store. You want x to be as small
# as possible, i.e., you want to minimize the maximum number of
# products that are given to any store.
# Return the minimum possible x.
# Example 1:
# Input: n = 6, quantities = [11,6]
# Output: 3
# Explanation: One optimal way is:
# - The 11 products of type 0 are distributed to the first four stores in these amounts: 2, 3, 3, 3
# - The 6 products of type 1 are distributed to the other two stores in these amounts: 3, 3
# The maximum number of products given to any store is max(2, 3, 3, 3, 3, 3) = 3.
# Example 2:

# Input: n = 7, quantities = [15,10,10]
# Output: 5
# Explanation: One optimal way is:
# - The 15 products of type 0 are distributed to the first three stores in these amounts: 5, 5, 5
# - The 10 products of type 1 are distributed to the next two stores in these amounts: 5, 5
# - The 10 products of type 2 are distributed to the last two stores in these amounts: 5, 5
# The maximum number of products given to any store is max(5, 5, 5, 5, 5, 5, 5) = 5.
# Example 3:
# Input: n = 1, quantities = [100000]
# Output: 100000
# Explanation: The only optimal way is:
# - The 100000 products of type 0 are distributed to the only store.
# The maximum number of products given to any store is max(100000) = 100000.
# Constraints:
# m == quantities.length
# 1 <= m <= n <= 105
# 1 <= quantities[i] <= 105

from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        left = 0
        right = max(quantities)
        ans = float("inf")
        
        def can(current_quantity: int):
            stores = n
            satisfied_stores = 0
            for quantity in quantities:
                satisfied_stores += quantity // current_quantity
                if quantity % current_quantity != 0:
                    satisfied_stores += 1
            return satisfied_stores <= stores
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if can(mid):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1

        return ans
    
# class Solution:
# def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
#     l, r = 1, max(quantities)
#     res = r
#     while l <= r:
#         m = l + (r - l) // 2
#         cur_sum = 0
#         for num in quantities:
#             cur_sum += math.ceil(num / m) 
#         if cur_sum <= n:
#             res = min(m, res)
#             r = m - 1
#         else:
#             l = m + 1
    
#     return res