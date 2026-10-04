# 912. Sort an Array
# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity
# and with the smallest space complexity possible.
# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed
# (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessarily unique.
# Constraints:
#     1 <= nums.length <= 5 * 104
#     -5 * 104 <= nums[i] <= 5 * 104

import random


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # return self.merge_sort(0, n - 1, nums)
        return self.quick_sort(0, n - 1, nums)

    # # Hoare's Partitioning Scheme
    # def quick_sort(self, left: int, right: int, array: list[int]):
    #     if left > right:
    #         return array

    #     if left == right:
    #         return array

    #     pivot = random.randint(left, right)
    #     array[left], array[pivot] = array[pivot], array[left]
    #     pivot_value = array[left]
    #     left_pointer = left - 1
    #     right_pointer = right + 1
    #     while True:
    #         left_pointer += 1
    #         while array[left_pointer] < pivot_value:
    #             left_pointer += 1

    #         right_pointer -= 1
    #         while array[right_pointer] > pivot_value:
    #             right_pointer -= 1

    #         if left_pointer >= right_pointer:
    #             break
    #         array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]

    #     self.quick_sort(left, right_pointer, array)
    #     self.quick_sort(right_pointer + 1, right, array)

    #     return array
    
    # Lomuto's Partitioning Scheme
    def quick_sort(self, left: int, right: int, array: list[int]):
        if left >= right:
            return array

        pivot = random.randint(left, right)
        left_pointer: int = left - 1
        i: int = left
        right_pointer: int = right
        pivot_value: int = array[pivot]
        
        while i <= right_pointer:
            if array[i] < pivot_value:
                left_pointer += 1
                array[left_pointer], array[i] = array[i], array[left_pointer]
                i += 1
            elif array[i] > pivot_value:
               
                array[right_pointer], array[i] = array[i], array[right_pointer]
                i +=1
                right_pointer -= 1
            else:
                i += 1
                
        self.quick_sort(left, left_pointer, array)
        self.quick_sort(right_pointer + 1, right, array)
        
        return array
    # def merge_sort(self, left: int, right: int, array: list[int]):

    #     if left > right:
    #         return array

    #     if left == right:
    #         return array

    #     pivot = random.randint(left, right)
    #     less_than_pivot = []
    #     greater_than_pivot = []

    #     for i in range(pivot):
    #         if array[i] < array[pivot]:
    #             less_than_pivot.append(array[i])
    #         else:
    #             greater_than_pivot.append(array[i])

    #     for i in range(pivot + 1, len(array)):
    #         if array[i] > array[pivot]:
    #             greater_than_pivot.append(array[i])
    #         else:
    #             less_than_pivot.append(array[i])

    #     return (
    #         self.merge_sort(0, len(less_than_pivot) - 1, less_than_pivot)
    #         + [array[pivot]]
    #         + self.merge_sort(0, len(greater_than_pivot) - 1, greater_than_pivot)
    #     )
