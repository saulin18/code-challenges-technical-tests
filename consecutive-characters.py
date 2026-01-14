#1446. Consecutive Characters
#The power of the string is the maximum length of a non-empty substring that contains only one unique character.
#
#Given a string s, return the power of s.
#Example 1:

#Input: s = "leetcode"
#Output: 2
#Explanation: The substring "ee" is of length 2 with the character 'e' only.
#Example 2:

#Input: s = "abbcccddddeeeeedcba"
#Output: 5
#Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

#Constraints:

#1 <= s.length <= 500
#s consists of only lowercase English letters.


def maxPower(s):

    count = 1
    max_count = 0
    
    for index, char in enumerate(s):
        
        
        
        if char == s[index - 1] and index != 0:
            count += 1
        
        max_count = max(max_count, count)
        count = 1 if char != s[index - 1] else count    
        
    return max_count    


s ="tourist"

print(maxPower(s))