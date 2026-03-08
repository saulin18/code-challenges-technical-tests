#
# Complete the 'getRemovableIndices' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING str1
#  2. STRING str2
#

# Problem Statement
# This message will be auto-pinned
# Given two strings, str1, and str2, where str1 contains exactly one character more than str2, find the indices of
# the characters in str1 that can be removed to make str1 equal to str2. Return the array of indices in increasing order.
# If it is not possible, return the array [-1].
#
# Note: Use 0-based indexing.
#
# Example
#
# str1 = "abdgggda"
#
# str2 = "abdggda"
#
# Any "g" character at positions 3, 4, or 5 can be deleted to obtain str2. Return [3, 4, 5].

from collections import defaultdict
from typing import Dict, Tuple, List


# More efficient approach using sliding window
def getRemovableIndices(str1: str, str2: str):
    if len(str1) != len(str2) + 1:
        return [-1]

    valid_indexes = []
    for i in range(len(str1)):
        if str1[:i] == str2[:i] and str1[i + 1:] == str2[i:]:
            valid_indexes.append(i)

    return valid_indexes if valid_indexes else [-1]


# First approach
# def getRemovableIndices(str1: str, str2: str):
# 
#     if len(str1) != len(str2) + 1:
#         return [-1]
# 
#     dict_str_1: Dict[str, Tuple[int, List]] = defaultdict(lambda: (0, []))
#     dict_str_2: Dict[str, int] = defaultdict(int)
# 
#     for i in range(len(str1)):
#         char = str1[i]
#         occurences, list_of_indexes = dict_str_1[char]
#         occurences += 1
#         list_of_indexes.append(i)
#         dict_str_1[char] = (occurences, list_of_indexes)
# 
#     for i in range(len(str2)):
#         dict_str_2[str2[i]] += 1
# 
#     valid_indexes = []
#     valid_char = None
# 
#     for char, value in dict_str_1.items():
#         occurences, list_of_indexes = value
# 
#         occurences_on_other_dict = dict_str_2[char]
# 
#         if (occurences > occurences_on_other_dict + 1) or (
#             occurences < occurences_on_other_dict
#         ):
#             return [-1]
# 
#         if occurences == occurences_on_other_dict:
#             continue
# 
#         if valid_char is None:
#             valid_char = char
#         else:
#             if valid_char != char:
#                 return [-1]    
#         
#         for i in list_of_indexes:
#             if str1[0:i] == str2[0:i] and str1[i + 1 :] == str2[i:]:
#                 valid_indexes.append(i)
# 
#     return [-1] if len(valid_indexes) == 0 else valid_indexes


if __name__ == "__main__":
    str1 = input()

    str2 = input()

    result = getRemovableIndices(str1, str2)

    print("\n".join(map(str, result)))
