# 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a
# single space separating the words. Do not include any extra spaces.
# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
# Constraints:
# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?


#def reverseWords(s):
#   WRONG  -> X

#        start = len(s)
#        
#        word = ""
#        res = ""
#        
#        for end in range(len(s) - 1, -1, -1):
#            if s[end] == " ":
#                word = s[end:start]
#                res += word
#                start = end
#            if end == 0:
#                word = s[end:start]
#                if res != "":
#                    res_with_start = res + " " + word
#                else:    
#                    res_with_start = res + word    
#                res = res_with_start
#                start -= len(word)
#                    
#        
#        return res.strip()  

def reverseWords(s):

        start = len(s)
        
        word = ""
        res = ""
        
        for end in range(len(s) - 1, -1, -1):
            if s[end] == " ":
               start -=1 
               continue

            if s[end] != " " and s[end - 1] == " " or end == 0:
                word = s[end:start]
                new_res = res + " " + word
                res = new_res
                start = end
                    
        
        return res 
        

print(reverseWords("the sky is blue"))
            