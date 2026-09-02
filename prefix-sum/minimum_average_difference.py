# 2256. Minimum Average Difference
# You are given a 0-indexed integer array nums of length n.

# The average difference of the index i is the absolute difference between the
# average of the first i + 1 elements of nums and the average of the last n - i - 1 elements.
# Both averages should be rounded down to the nearest integer.
# Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.
# Note:
# The absolute difference of two numbers is the absolute value of their difference.
# The average of n elements is the sum of the n elements divided (integer division) by n.
# The average of 0 elements is considered to be 0.
# Example 1:
# Input: nums = [2,5,3,9,5,3]
# Output: 3
# Explanation:
# - The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
# - The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
# - The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
# - The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
# - The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
# - The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
# The average difference of index 3 is the minimum average difference so return 3.
# Example 2:
# Input: nums = [0]
# Output: 0
# Explanation:
# The only index is 0 so return 0.
# The average difference of index 0 is: |0 / 1 - 0| = |0 - 0| = 0.
# Constraints:
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105

class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        res = float("inf")
        n = len(nums)
        prefix_sum = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        index = 0
        for i in range(n):
            left_count = i + 1
            right_count = n - i - 1

            left_sum = prefix_sum[i + 1]
            right_sum = prefix_sum[n] - left_sum
            average_of_left = left_sum // left_count
            average_of_right = right_sum // right_count if right_count > 0 else 0
            
            if abs(average_of_left - average_of_right) < res:
                res = abs(average_of_left - average_of_right)
                index = i
            

        return index
        
# class Solution:
#     def minimumAverageDifference(self, nums: List[int]) -> int:
#         n = len(nums); sm = sum(nums); pref = list(accumulate(nums))
#         mn = float('inf'); ans = None
#         for i in range(n):
#             a1 = pref[i]//(i + 1)
#             a2 = ( (sm - pref[i])//(n - i - 1) ) if i < n - 1 else 0
#             if abs(a1 - a2) < mn: mn = abs(a1 - a2); ans = i
#         return ans



# class Solution:
#     def minimumAverageDifference(self, nums: List[int]) -> int:
#         n = len(nums)
#         tot = sum(nums)
#         res = float('inf')
#         ans = - 1
#         left = 0
#         right = tot
#         for i in range(n - 1) :
#             left += nums[i]
#             right -= nums[i]
#             diff = abs((left//(i + 1)) - right//(n - i - 1))
#             if diff < res :
#                 res = diff
#                 ans = i
#         if tot//n < res :
#             return n - 1
#         return ans