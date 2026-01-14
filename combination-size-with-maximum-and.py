#275. Largest Combination With Bitwise AND Greater Than Zero
#The bitwise AND of an array nums is the bitwise AND of all integers in nums.
#
#For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
#Also, for nums = [7], the bitwise AND is 7.
#You are given an array of positive integers candidates. Compute the bitwise AND for all
# possible combinations of elements in the candidates array.
#Return the size of the largest combination of candidates with a bitwise AND greater than 0
#Input: candidates = [16,17,71,62,12,24,14]
#Output: 4
#Explanation: The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0.
#The size of the combination is 4.
#It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0.
#Note that more than one combination may have the largest size.
#For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.

#Input: candidates = [8,8]
#Output: 2
#Explanation: The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0.
#The size of the combination is 2, so we return 2.

#1 <= candidates.length <= 105
#1 <= candidates[i] <= 107
from functools import reduce
def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        # Save the maximum size of the combinations with the bitwise AND > 0
        maximum_size = [0]
        
        def calculate_bitwise_and(path: list[int], maximum_size: list[int]):
            
            if len(path) == 0:
                return
            
            path_and_sum = reduce(lambda a, b: a & b, path)
            if not path_and_sum >  0:
                return
            maximum_size[0] = max(maximum_size[0], len(path))
            
        def backtrack(start: int, path: list[int], maximum_size: list[int]):
            
            calculate_bitwise_and(path, maximum_size)
            
            for end in range(start, len(candidates)):
                actual = candidates[end]
                path.append(actual)
                backtrack(end + 1, path, maximum_size)
                path.pop()
        
        backtrack(0, [], maximum_size)   
        return maximum_size[0]     
            
            