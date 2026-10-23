# Longest 2-character substring
# Find the longest substring within a string that contains at most 2 unique characters.

# "a" => "a"
# "aaa" => "aaa"
# "abacd" => "aba"
# "abacddcd" => "cddcd"
# "cefageaacceaccacca" => "accacca"

# This function will take alphanumeric characters as input.

# In cases where there could be more than one correct answer, the first string occurrence 
# should be used. For example, 'abc' should return 'ab' instead of 'bc'.

# Although there are O(N^2) solutions to this problem, you should try to 
# solve this problem in O(N) time. Tests may pass for O(N^2) solutions but, this is not guaranteed.

# This question is much harder than some of the other substring questions. 
# It's easy to think that you have a solution and then get hung up on the implementation.

from collections import defaultdict
def substring(strng: str) -> str:
    
    ocurrences = defaultdict(int)
    
    left = 0  
    right = 0
    max_length = 0
    
    better_left_and_right = (0, 0)
    
    while right < len(strng):
        if strng[right] in ocurrences:
            ocurrences[strng[right]] += 1
            
        else:
            ocurrences[strng[right]] = 1
        
        while len(ocurrences) > 2:
            
            ocurrences[strng[left]] -= 1
            if ocurrences[strng[left]] == 0:
                del ocurrences[strng[left]]
                
            left += 1
                
                    
        if right - left + 1 > max_length:
            max_length = right - left + 1
            better_left_and_right = (left, right)
            
        right += 1
    
    return strng[better_left_and_right[0]:better_left_and_right[1] + 1]