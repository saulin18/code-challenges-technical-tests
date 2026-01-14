#Description:
#Given a string that includes alphanumeric characters ("3a4B2d") return the expansion of that string: 
# The numeric values represent the occurrence of each letter preceding that numeric value. T
# here should be no numeric characters in the final string.
#
#Notes
#The first occurrence of a numeric value should be the number of times each character behind it is
# repeated, until the next numeric value appears
#If there are multiple consecutive numeric characters, only 
# the last one should be used (ignore the previous ones)
#Empty strings should return an empty string.
#Your code should be able to work for both lower and capital case letters.
#
#"3D2a5d2f"  -->  "DDDaadddddff"    # basic example: 3 * "D" + 2 * "a" + 5 * "d" + 2 * "f"
#"3abc"      -->  "aaabbbccc"       # not "aaabc", nor "abcabcabc"; 3 * "a" + 3 * "b" + 3 * "c"
#"3d332f2a"  -->  "dddffaa"         # multiple consecutive digits: 3 * "d" + 2 * "f" + 2 * "a"
#"abcde"     -->  "abcde"           # no digits
#"1111"      -->  ""                # no characters to repeat
#""          -->  ""                # empty string


def string_expansion(s: str):

    if s == "":
        return ""

    result = []
    found_digit = False
    last_digit = 0
    last_digit_index = 0
    chars = []
    for i, char in enumerate(s):
        if char.isdigit():
            found_digit = True
            last_digit = int(char)
            last_digit_index = i

            # We search for the next chars after the digit for selecting the correct digit
            # ex: if 332 we want to select the 2
            while last_digit_index + 1 < len(s) and not s[last_digit_index + 1].isalpha():
                last_digit_index += 1
                last_digit = int(s[last_digit_index])


        if last_digit == 0:
            result.append(char)
        if char.isalpha():
            chars.append(char)
        if (s[i + 1] is not None and s[i + 1].isdigit() and i < len(s) - 1) or (i == len(s) - 1) and s[i].isalpha():
            for char in chars:
                result.append(char * last_digit)
            chars.clear()

    return "".join(result)
