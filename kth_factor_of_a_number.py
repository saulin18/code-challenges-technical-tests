# 1492. The kth Factor of n
# You are given two positive integers n and k.
# A factor of an integer n is defined as an integer i where n % i == 0.

# Consider a list of all factors of n sorted 
# in ascending order, return the kth factor in this
# list or return -1 if n has less than k factors.
# Example 1:
# Input: n = 12, k = 3
# Output: 3
# Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
# Example 2:

# Input: n = 7, k = 2
# Output: 7
# Explanation: Factors list is [1, 7], the 2nd factor is 7.
# Example 3:

# Input: n = 4, k = 4
# Output: -1
# Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
# Constraints:
# 1 <= k <= n <= 1000
# Follow up:
# Could you solve this problem in less than O(n) complexity?

import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        uniques = set()
        uniques.add(1)
        sqrt_of_n = math.sqrt(n)
        i = 2
        while i <= sqrt_of_n:
            if n % i == 0:
                uniques.add(i)
                uniques.add(n//i)
            i +=1
        uniques.add(n)    
        

        i = 0
        for div in sorted(uniques):
            if i == k - 1:
                return div
            i +=1    


        return -1
        