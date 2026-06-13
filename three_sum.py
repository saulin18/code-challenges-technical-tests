# 15. 3Sum
# Given an integer array nums, return all the triplets
#  [nums[i], nums[j], nums[k]] such that i != j, i != k,
#  and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
# Constraints:
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
             
            start = i + 1
            right = len(nums) - 1
            target = num
            while start < right:
                sum = nums[start] + nums[right]
                if sum == -target:
                    res.append([num, nums[start], nums[right]])
                    while start < right and nums[start + 1] == nums[start]:
                        start += 1
                        continue
                    while start < right and nums[right - 1] == nums[right]:
                        right -= 1
                        continue

                    start += 1
                    right -= 1

                if sum > -target:
                    right -= 1
                elif sum < -target:
                    start += 1

        return res
