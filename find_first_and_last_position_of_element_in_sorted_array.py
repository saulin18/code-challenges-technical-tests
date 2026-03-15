# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109


def searchRange(
    nums: list[int],
    target: int,
) -> list[int]:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    l = 0
    r = len(nums) - 1
    coincedence = [-1, -1]
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1

        if nums[mid] == target:
            # Equal to the index, we need to find the left and right bounds of the target value
            coincedence[0] = mid
            coincedence[1] = mid
            # Search left indexes
            while coincedence[0] - 1 >= 0 and nums[coincedence[0] - 1] == target:
                coincedence[0] -= 1
            # Search right indexes
            while coincedence[1] + 1 < len(nums) and nums[coincedence[1] + 1] == target:
                coincedence[1] += 1
            break

    return coincedence

print(searchRange([5, 7, 7, 8, 8, 10], 8))
