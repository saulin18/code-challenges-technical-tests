# 9. Palindrome Number
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer x, return true if x is a palindrome, and false otherwise.


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    original = x
    reversed_num = 0
    while x != 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    return original == reversed_num


print(isPalindrome(121))  # True
print(isPalindrome(-121))  # False
print(isPalindrome(10))  # False


# def isPalindrome(x):
#    str_number = str(x)
#    reversed_str_number = str_number[::-1]
#
#    return int(str_number) == int(reversed_str_number)
