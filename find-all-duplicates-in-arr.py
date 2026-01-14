#442. Find All Duplicates in an Array
#Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, 
# return an array of all the integers that appears twice.
#You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output
#Example 1:
#Input: nums = [4,3,2,7,8,2,3,1]
#Output: [2,3]
#Example 2:
#Input: nums = [1,1,2]
#Output: [1]
#Example 3:
#Input: nums = [1]
#Output: []
#Constraints:
#n == nums.length
#1 <= n <= 105
#1 <= nums[i] <= n
#Each element in nums appears once or twice.


        
        # We will use a "flip approach" we will mark the num index, we will flip the value at that index to negative and if
        # we find that the value at that index is already negative, it means we have seen that number before so we add the number
        # to our solution
        
       
def findDuplicates(nums):
        
        res = []

        for index in range(len(nums)):
            if nums[abs(nums[index]) - 1] < 0: 
                res.append(abs(nums[index]))

            nums[abs(nums[index]) - 1] = - abs(nums[abs(nums[index]) - 1])  

        return res    
        
        