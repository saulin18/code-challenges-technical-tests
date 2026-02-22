# 152. Maximum Product Subarray
# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# Note that the product of an array with a single element is the value of that element.
# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# Constraints:
# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # The reasoning is the following: we need to keep track the maximum while we iterate through the array
        # initialize the value max_product to -Infinity and keep updating it, also, we only need to keep track
        # of two values, the maximum at the current index, and the minimum at the current index, we need to do
        # it this way because we could have negative numbers and if the next number is negative the previous product
        # could be less than the following product

        minimum_product, maximum_product = 1, 1

        max_product = float("-inf")

        for index in range(len(nums)):
            temp = maximum_product
            maximum_product = max(nums[index], nums[index] * maximum_product, minimum_product * nums[index])
            minimum_product = min(nums[index], nums[index] * temp, minimum_product * nums[index])
            max_product = max(max_product, maximum_product)
           

        return max_product
