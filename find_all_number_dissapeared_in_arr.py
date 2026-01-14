
#448. Find All Numbers Disappeared in an Array
#Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n]
#that do not appear in nums.
#Example 1:
#Input: nums = [4,3,2,7,8,2,3,1]
#Output: [5,6]
#Example 2:
#Input: nums = [1,1]
#Output: [2]
#Constraints:
#n == nums.length
#1 <= n <= 105
#1 <= nums[i] <= n
#Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space

#def findDisappearedNumbers(nums):
#
#    res = set(nums)
#    
#    for index in range(1, len(nums) + 1):
#           res.add(index)
#    
#    return res - set(nums)           
#    
#          
#print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # Output: [5,6]
#print(findDisappearedNumbers([1,1]))  # Output: [2]      

def findDissapearedNumbers(nums):
    
    
    for num in nums:
       correct_index = abs(num) - 1
       
       nums[correct_index] = - abs(nums[correct_index])
       print(nums)
    
    res = []
    
    
    for index in range(len(nums)):
        
        if nums[index] > 0:
            res.append(index + 1) 
            
        print(nums, "nums")
        print(res, " res")
        
    return res


print(findDissapearedNumbers([4,3,2,7,8,2,3,1])) # Output: [5,6]
print(findDissapearedNumbers([1,1])) # Output: [2]       

        