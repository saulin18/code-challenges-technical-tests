#3211. Generate Binary Strings Without Adjacent Zeros
#You are given a positive integer n.
#A binary string x is valid if all substrings of x of length 2 contain at least one "1".
#Return all valid strings with length n, in any order.
#Example 1:
#Input: n = 3
#Output: ["010","011","101","110","111"]
#Explanation:
#The valid strings of length 3 are: "010", "011", "101", "110", and "111".
#Example 2:
#Input: n = 1
#Output: ["0","1"]
#Explanation:
#The valid strings of length 1 are: "0" and "1".
#Constraints:
#1 <= n <= 18

def validStrings(self, n):

    result = []
    
    # string with length n without adjacent zeroes
    
    def backtrack(current_string: str):
        if len(current_string) == n:
            result.append(current_string)
            return
        
        if len(current_string) == 0:
            # Because we can start with 1 or with 0
            current_string += "1"
            backtrack(current_string)
            current_string = current_string[:-1]
            
            current_string += "0"
            backtrack(current_string)
            current_string = current_string[:-1]
    
        if current_string[-1] == "0":
            # AFTER a 0 can only follow a 1
            current_string += "1"
            backtrack(current_string)
            if current_string != "": current_string = current_string[:-1]

             
        if current_string[-1] == "1":
            # Follow with a 0 or with a 1
            current_string += "0"
            backtrack(current_string)
            if current_string != "": current_string = current_string[:-1]
            
            current_string += "1"
            backtrack(current_string)
            if current_string != "": current_string = current_string[:-1]
            
            
    
    backtrack("")
    
    return result
            
            
        