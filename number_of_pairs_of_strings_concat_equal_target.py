# 2023. Number of Pairs of Strings With Concatenation Equal to Target
# Given an array of digit strings nums and a digit
# string target, return the number of pairs of indices
# (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.
# Example 1:
# Input: nums = ["777","7","77","77"], target = "7777"
# Output: 4
# Explanation: Valid pairs are:
# - (0, 1): "777" + "7"
# - (1, 0): "7" + "777"
# - (2, 3): "77" + "77"
# - (3, 2): "77" + "77"
# Example 2:
# Input: nums = ["123","4","12","34"], target = "1234"
# Output: 2
# Explanation: Valid pairs are:
# - (0, 1): "123" + "4"
# - (2, 3): "12" + "34"
# Example 3:

# Input: nums = ["1","1","1"], target = "11"
# Output: 6
# Explanation: Valid pairs are:
# - (0, 1): "1" + "1"
# - (1, 0): "1" + "1"
# - (0, 2): "1" + "1"
# - (2, 0): "1" + "1"
# - (1, 2): "1" + "1"
# - (2, 1): "1" + "1"

# Constraints:

# 2 <= nums.length <= 100
# 1 <= nums[i].length <= 100
# 2 <= target.length <= 100
# nums[i] and target consist of digits.
# nums[i] and target do not have leading zeros.

# class Solution:
#     def numOfPairs(self, nums: List[str], target: str) -> int:
#         # two sum
#         freq = defaultdict(int)
#         for s in nums:
#             freq[s] += 1
#         # print(freq)
#         res = 0
#         for s in nums:
#             if target.startswith(s):
#                 compliment = target[len(s):]
#                 # print(compliment)
#                 if compliment in freq:
#                     res += freq[compliment]
#                     if s == compliment:
#                         res -= 1
#         return res




from typing import List


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:

        frequency = {}
        count = 0

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        for i in range(len(target) -1 ):
            left = target[:i + 1]
            right = target[i + 1:]
            
            if left == right:
                count += frequency.get(left, 0) * (frequency.get(left, 0) - 1)

            if left in frequency and right in frequency:
                count += frequency[left] * frequency[right]
        
        return count        

nums = ["1", "1", "1"]
target = "11"
print(Solution.numOfPairs(Solution, nums, target))
