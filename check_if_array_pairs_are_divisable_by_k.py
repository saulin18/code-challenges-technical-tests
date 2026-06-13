# 1497. Check If Array Pairs Are Divisible by k
# Given an array of integers arr of even length n and an integer k.
# We want to divide the array into exactly n / 2 pairs such that
# the sum of each pair is divisible by k.
# Return true If you can find a way to do that or false otherwise.
# Example 1:
# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
# Example 2:
# Input: arr = [1,2,3,4,5,6], k = 7
# Output: true
# Explanation: Pairs are (1,6),(2,5) and(3,4).
# Example 3:
# Input: arr = [1,2,3,4,5,6], k = 10
# Output: false
# Explanation: You can try all possible pairs to see that there
# is no way to divide arr into 3 pairs each with sum divisible by 10.
# Constraints:
# arr.length == n
# 1 <= n <= 105
# n is even.
# -109 <= arr[i] <= 109
# 1 <= k <= 105

from collections import defaultdict


class Solution(object):
    def canArrange(self, arr, k):

        my_map = defaultdict(int)

        for x in arr:
            my_map[(x + k) % k] += 1

        if my_map[0] % 2 != 0:
            return False

        if k % 2 == 0:
            if my_map[k // 2] % 2 != 0:
                return False

        for remainder in range(1, (k + 1) // 2):
            if remainder < k - remainder and my_map[remainder] != my_map[k - remainder]:
                return False

        return True


# class Solution(object):
#     def canArrange(self, arr, k):
#         """
#         :type arr: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         rem_counts = [0] * k  # Frequency array to store the counts of each remainder
        
#         for num in arr:
#             rem_counts[num % k] += 1  # Python safely wraps negative remainders to positive (e.g., -1 % 5 == 4)
            
#         if rem_counts[0] % 2 != 0:
#             return False  # Elements perfectly divisible by k must pair with each other, requiring an even count
            
#         for i in range(1, k // 2 + 1):
#             if rem_counts[i] != rem_counts[k - i]:
#                 return False  # Remainder 'i' must perfectly pair with remainder 'k-i' to sum to a multiple of k
                
#         return True