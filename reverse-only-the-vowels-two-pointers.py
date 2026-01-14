#345. Reverse Vowels of a String
#Given a string s, reverse only all the vowels in the string and return it.
#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#Example 1:
#Input: s = "IceCreAm"
#Output: "AceCreIm"
#Explanation:
#The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
#Example 2:
#
#Input: s = "leetcode"
#
#Output: "leotcede"
#Constraints:
#1 <= s.length <= 3 * 105
#s consist of printable ASCII characters.

def reverseVowels(s: str):
        """
        :type s: str
        :rtype: str
        """
        
        start = 0
        end = len(s) - 1
        s = [*s]
        
        while start < end:
                
                while start < end and s[start] not in 'aeiouAEIOU':
                        start += 1
                
                while start < end and s[end] not in 'aeiouAEIOU':
                        end -= 1
                        

                if start < end:            
                    s[start], s[end] = s[end], s[start]
                  
                    start += 1
                    
                    end -= 1     
        
        return "".join(s)
        


# Test cases
print(reverseVowels("IceCreAm") ) # Expected output: "AceCreIm"
print(reverseVowels("leetcode") ) # Expected output: "leotcede"              