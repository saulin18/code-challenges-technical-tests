# 383. Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
# Constraints:
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.
from collections import defaultdict
def canConstruct(self, ransomNote, magazine):


    dict = defaultdict(int)
    
    for char in ransomNote:
        dict[char] +=1
    
    for letter in magazine:
        if dict[letter] != 0:
            dict[letter] -=1
        
    
    for val in dict.values():
        if val != 0:
            return False
        
    return True            
        