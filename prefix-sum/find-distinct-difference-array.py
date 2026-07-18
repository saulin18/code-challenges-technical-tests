# 2670. Find the Distinct Difference Array
# You are given a 0-indexed array nums of length n.

# The distinct difference array of nums is an array diff of length n such that diff[i] is equal to the number of distinct ele
# ments in the suffix nums[i + 1, ..., n - 1] subtracted from the number of distinct elements in the prefix nums[0, ..., i].
# Return the distinct difference array of nums.
# Note that nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j inclusive.
# Particularly, if i > j then nums[i, ..., j] denotes an empty subarray.
# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: [-3,-1,1,3,5]
# Explanation: For index i = 0, there is 1 element in the prefix and 4 distinct elements in the suffix. Thus, diff[0] = 1 - 4 = -3.
# For index i = 1, there are 2 distinct elements in the prefix and 3 distinct elements in the suffix. Thus, diff[1] = 2 - 3 = -1.
# For index i = 2, there are 3 distinct elements in the prefix and 2 distinct elements in the suffix. Thus, diff[2] = 3 - 2 = 1.
# For index i = 3, there are 4 distinct elements in the prefix and 1 distinct element in the suffix. Thus, diff[3] = 4 - 1 = 3.
# For index i = 4, there are 5 distinct elements in the prefix and no elements in the suffix. Thus, diff[4] = 5 - 0 = 5.
# Example 2:
# Input: nums = [3,2,3,4,2]
# Output: [-2,-1,0,2,3]
# Explanation: For index i = 0, there is 1 element in the prefix and 3 distinct elements in the suffix. Thus, diff[0] = 1 - 3 = -2.
# For index i = 1, there are 2 distinct elements in the prefix and 3 distinct elements in the suffix. Thus, diff[1] = 2 - 3 = -1.
# For index i = 2, there are 2 distinct elements in the prefix and 2 distinct elements in the suffix. Thus, diff[2] = 2 - 2 = 0.
# For index i = 3, there are 3 distinct elements in the prefix and 1 distinct element in the suffix. Thus, diff[3] = 3 - 1 = 2.
# For index i = 4, there are 3 distinct elements in the prefix and no elements in the suffix. Thus, diff[4] = 3 - 0 = 3.
# Constraints:
#     1 <= n == nums.length <= 50
#     1 <= nums[i] <= 50


# from typing import List


# class Solution:
#     def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         ans = [0] * n
#         prefix_distinct = [0] * n
#         suffix_distinct = [0] * n

#         prefix_distinct[0] = nums[0]

#         prefix_set = set()
#         suffix_set = set()

#         unique_prefix_count = 0
#         unique_suffix_count = 0
#         for i in range(n):
#             if nums[i] not in prefix_set:
#                 unique_prefix_count += 1
#                 prefix_set.add(nums[i])
#             prefix_distinct[i] = unique_prefix_count

#         for i in range(n - 2, -1, -1):
#             if nums[i + 1] not in suffix_set:
#                 unique_suffix_count += 1
#                 suffix_set.add(nums[i + 1])
#             suffix_distinct[i] = unique_suffix_count

#         for i in range(n):
#             ans[i] = prefix_distinct[i] - suffix_distinct[i]

#         return ans




from typing import List
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        prefix_distinct = [0] * n
        suffix_distinct = [0] * n

        prefix_distinct[0] = nums[0]
        suffix_distinct[-1] = 0

        prefix_set = set()
        suffix_set = set()

        # We'll use one pass to calculate the prefix distinct count and the suffix count n - i - 1, we'll use the length of the sets
        for i in range(n):
            if nums[i] not in prefix_set:
                prefix_set.add(nums[i])
            prefix_distinct[i] = len(prefix_set)

            # Here the order matters because we don't want to include the actual element and we can't fix it changing the indexes or
            # initializing, the suffix set represents the previous state
            suffix_distinct[n - i - 1] = len(suffix_set)
            suffix_set.add(nums[n - i - 1])

        for i in range(n):
            ans[i] = prefix_distinct[i] - suffix_distinct[i]

        return ans
