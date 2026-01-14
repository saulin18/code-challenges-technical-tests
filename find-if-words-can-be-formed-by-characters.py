# 160. Find Words That Can Be Formed by Characters
# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).
# Return the sum of lengths of all good strings in words.
# Example 1:
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
# 1 <= words.length <= 1000
# Constraints:
# 1 <= words[i].length, chars.length <= 100
# words[i] and chars consist of lowercase English letters.
from collections import defaultdict
class Solution(object):

    def countCharacters(self, words, chars):

        res = 0
        
        # Dict for chars
        dict = defaultdict(int)
        
        for i in range(len(chars)):
            dict[chars[i]] +=1
            
        
        for end in range(len(words)):
            is_good = True
            for start in range(len(words[end])):
                char_count = words[end].count(words[end][start])
                if not dict[words[end][start]] >= char_count:
                    is_good = False

            if is_good:
                res += len(words[end])         
                
        return res        
        
        
            
    
    