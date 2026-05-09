# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations
# that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. 
# Note that 1 does not map to any letters.
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
# Input: digits = "2"
# Output: ["a","b","c"]
# Constraints:
# 1 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].


class Solution(object):
    def letterCombinations(self, digits):
    
        phone_board = {
                1: [],                2: ['a', 'b','c'],    3: ['d','e','f'],
                4: ['g','h','i'],     5: ['j','k','l'],     6: ['m','n','o'], 
                7: ['p','q','r','s'], 8: ['t','u','v'],     9: ['w','x','y','z']
            }
        
        res = []
        
        def backtrack(actual_combination, next_digits):
            
            if len(next_digits) == 0:
                res.append("".join(actual_combination))
            else:
                for letter in phone_board[int(next_digits[0])]:
                    actual_combination.append(letter)
                    backtrack(actual_combination, next_digits[1:])
                    actual_combination.pop()

        backtrack([], digits)            
        return res            
            