from collections import defaultdict


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        nums.sort()

        n = len(nums)
        for i in range(n):
            j = i + 1
            k = n - 1
            actual = nums[i]
            needed = -actual

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while j < n and k > 0 and j < k:
                sum = nums[j] + nums[k]

                if sum == needed:
                    res.append([nums[i], nums[j], nums[k]])

                    while j < n and j + 1 < n and nums[j] == nums[j + 1]:
                        j += 1
                    while k > 0 and k - 1 > 0 and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif sum < needed:
                    j += 1
                else:
                    k -= 1
        return res
