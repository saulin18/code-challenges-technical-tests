# 2270. Number of Ways to Split Array
# You are given a 0-indexed integer array nums of length n.
# nums contains a valid split at index i if the following are true:
#     The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
#     There is at least one element to the right of i. That is, 0 <= i < n - 1.
# Return the number of valid splits in nums.
# Example 1:
# Input: nums = [10,4,-8,7]
# Output: 2
# Explanation:
# There are three ways of splitting nums into two non-empty parts:
# - Split nums at index 0. Then, the first part is [10], and its sum is 10. The second part is [4,-8,7], and its sum is 3. Since 10 >= 3, i = 0 is a valid split.
# - Split nums at index 1. Then, the first part is [10,4], and its sum is 14. The second part is [-8,7], and its sum is -1. Since 14 >= -1, i = 1 is a valid split.
# - Split nums at index 2. Then, the first part is [10,4,-8], and its sum is 6. The second part is [7], and its sum is 7. Since 6 < 7, i = 2 is not a valid split.
# Thus, the number of valid splits in nums is 2.
# Example 2:
# Input: nums = [2,3,1,0]
# Output: 2
# Explanation:
# There are two valid splits in nums:
# - Split nums at index 1. Then, the first part is [2,3], and its sum is 5. The second part is [1,0], and its sum is 1. Since 5 >= 1, i = 1 is a valid split.
# - Split nums at index 2. Then, the first part is [2,3,1], and its sum is 6. The second part is [0], and its sum is 0. Since 6 >= 0, i = 2 is a valid split.
# Constraints:
#     2 <= nums.length <= 105
#     -105 <= nums[i] <= 105


from typing import List
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = 0

        # Esentially it's just a prefix sum problem, the left prefix needs to be greater than or equal to the right prefix and the right prefix must
        # have at least one element
        # Though we don't need to calculate the suffix sum array explicitly, we can use the prefix sum array to calculate it on the fly
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        total_sum = prefix[n - 1]
        for i in range(n - 1):
            left_sum = prefix[i]
            right_sum = total_sum - left_sum
            if left_sum >= right_sum:
                ans += 1

        return ans


# class Solution:
#     def waysToSplitArray(self, nums: List[int]) -> int:

#         summ =0
#         for i in nums:
#             summ+=i

#         prefix_sum = 0

#         suffix_sum = summ

#         count =0


#         for i in range(0,len(nums)-1):

#             prefix_sum+= nums[i]


#             suffix_sum -= nums[i]

#             if(prefix_sum >= suffix_sum):

#                 count+=1


#         return count



        # rightPrefixSum = sum(nums)
        # leftPrefixSum = 0
        # ctr = 0

        # for i in range(len(nums)-1):
        #     leftPrefixSum += nums[i]
        #     if leftPrefixSum >= rightPrefixSum - leftPrefixSum:
        #         ctr += 1

        # return ctr


# class Solution:
#     def waysToSplitArray(self, nums: List[int]) -> int:
#         if len(nums) < 2:
#             return 0

#         total_sum = sum(nums)
#         valid = 0
#         left_sum = 0
#         for i in range(len(nums) - 1):
#             left_sum += nums[i]

#             if left_sum >= total_sum - left_sum:
#                 valid += 1
#         return valid
