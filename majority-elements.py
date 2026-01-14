#229. Majority Element II
#Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#Example 1:
#Input: nums = [3,2,3]
#Output: [3]
#Example 2:
#Input: nums = [1]
#Output: [1]
#Example 3:
#Input: nums = [1,2]
#Output: [1,2]
#Constraints:
#1 <= nums.length <= 5 * 104
#-109 <= nums[i] <= 109
#Follow up: Could you solve the problem in linear time and in O(1) space?

def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
     # We can only have at most two majority elements
        if not nums:
                return []
        
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for i, num in enumerate(nums):
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1   
               
        return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) // 3]       