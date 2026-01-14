#784. Letter Case Permutation
#Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
#
#Return a list of all possible strings we could create. Return the output in any order.
#
#Example 1:
#
#Input: s = "a1b2"
#Output: ["a1b2","a1B2","A1b2","A1B2"]
#Example 2:
#
#Input: s = "3z4"
#Output: ["3z4","3Z4"]
#Constraints:
#
#1 <= s.length <= 12
#s consists of lowercase English letters, uppercase English letters, and digits.

def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        res = []
        set_seen = set()
        
        
        def backtrack(start,  remaining):
            if start >= len(remaining) and tuple(remaining) not in set_seen:
                
                res.append(remaining)
                set_seen.add(tuple(remaining))
                return
            
            if not remaining[start].isdigit():
                char = remaining[start]
                char = char.swapcase()
                new_remaining = remaining[:start] + char + remaining[start+1:]
                backtrack(start + 1, new_remaining)
                backtrack(start + 1, remaining)
            else:    
                backtrack(start + 1, remaining)    
                    
        backtrack(0, s)
        
        return res            