# 494. Target Sum
# You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.
# Example 1:
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# Example 2:
#
# Input: nums = [1], target = 1
# Output: 1
# Constraints
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000


def findTargetSumWays(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    # We will use a subsets approach, we will add the number positive to the subset, and we will add it negative, and later we will look for the sum
    # if its equal to our target, we increase our counter in 1
    # return counter

    memo = {}

    def backtrack(start, sum, memo):
        if (start, sum) in memo:
            return memo[(start, sum)]
        if start == len(nums):
            if sum == target:
                return 1
            return 0

        num = nums[start]
        # Add the number
        current_sum = backtrack(start + 1, sum + num)

        # Dont add the number (substract)
        substract = backtrack(start + 1, sum - num)

        total = current_sum + substract
        memo[(start, sum)] = total
        return total

    res = backtrack(0, 0, memo)

    return res
