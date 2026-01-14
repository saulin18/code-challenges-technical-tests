str1 = "saul"
str2 = "abe"

print(str1 + str2)

s3 = str1 + str2
print(id(s3), id(str1))

str1 += str2
s4 = str1

print(id(s4), id(str1))
print(s4, str1)
str1 += str2
print(str1, str2)


# 12. Rearrange Pos/Neg Lambda
#
# Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
#
# Original arrays:
# [-1, 2, -3, 5, 7, 8, 9, -10]
# Rearrange positive and negative numbers of the said array:
# [2, 5, 7, 8, 9, -10, -3, -1]


def rearrange(arr: list[int]) -> list[int]:
    negatives = list(filter(lambda num: num < 0, arr))
    positives = list(filter(lambda num: num > 0, arr))

    return positives + negatives


print(rearrange([-1, 2, -3, 5, 7, 8, 9, -10]))
