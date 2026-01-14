#Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral 
# values will be tested for each function.
#
#Modern Roman numerals are written by expressing each digit separately starting with the left most digit and
# skipping any digit with a value of zero. In Roman numerals:
#
#1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
#2008 is written as 2000=MM, 8=VIII; or MMVIII
#1666 uses each Roman symbol in descending order: MDCLXVI.
#Input range : 1 <= n < 4000
#
#In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
#
#Examples
#to roman:
#2000 -> "MM"
#1666 -> "MDCLXVI"
#  86 -> "LXXXVI"
#   1 -> "I"
#
#from roman:
#"MM"      -> 2000
#"MDCLXVI" -> 1666
#"LXXXVI"  ->   86
#"I"       ->    1
#Help
#+--------+-------+
#| Symbol | Value |
#+--------+-------+
#|    M   |  1000 |
#|   CM   |   900 |
#|    D   |   500 |
#|   CD   |   400 |
#|    C   |   100 |
#|   XC   |    90 |
#|    L   |    50 |
#|   XL   |    40 |
#|    X   |    10 |
#|   IX   |     9 |
#|    V   |     5 |
#|   IV   |     4 |
#|    I   |     1 |
#+--------+-------+

class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
    
                
        values = [
            (1000, "M"),
            (900, "CM"),   
            (500, "D"),
            (400, "CD"),   
            (100, "C"),
            (90, "XC"),  
            (50, "L"),
            (40, "XL"),   
            (10, "X"),
            (9, "IX"),     
            (5, "V"),
            (4, "IV"),    
            (1, "I")
        ]
        
        result = ""
    
        for value, symbol in values:
            if val >= value:
                count = val // value
                
                if count:
                    # Append the symbol 'count' times
                    result += symbol * count
                    
                    # Decrease num
                    val -= value * count
                
                if val == 0:
                    return result    
            
            continue        
        return result  
            
        

    @staticmethod
    def from_roman(roman_num : str) -> int:
        
        map_of_roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        
        total = 0
        
        for i in range(len(roman_num) - 1, -1, -1):
            
            # If the current numeral is less than the previous numeral we subtract
            if i < len(roman_num) - 1 and map_of_roman_numerals[roman_num[i]] < map_of_roman_numerals[roman_num[i + 1]]:
                total -= map_of_roman_numerals[roman_num[i]]
            else:
                total += map_of_roman_numerals[roman_num[i]]
        
        return total            