# 3. Tuple Sorting Lambda
#
# Write a Python program to sort a list of tuples using Lambda.
#
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


from decimal import Decimal


def sorting(list_of_tuples):
    sorted_list = sorted(list_of_tuples, key=lambda x: x[1])

    return sorted_list


print(
    sorting([("English", 88), ("Science", 90), ("Maths", 97), ("Social sciences", 82)])
)

# 5. Integer Filter Lambda
#
# Write a Python program to filter a list of integers using Lambda.
#
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]


def integer_filter(list_of_integers):
    even = filter(lambda x: x % 2 == 0, list_of_integers)
    odd = filter(lambda x: x % 2 != 0, list_of_integers)

    return list(even), list(odd)


print(
    integer_filter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
)  # Output: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9]) sorted

# 11. Array Intersection Lambda
#
# Write a Python program to find the intersection of two given arrays using Lambda.
#
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]
# Intersection of the said arrays: [1, 2, 8, 9]


def array_intersection(array1, array2):
    # return list(filter(lambda x: x in array1 and x in array2, array1))
    return set(array1).intersection(set(array2))


print(array_intersection([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]))

# Define a list 'array_nums' containing both positive and negative integers
array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]

# Display a message indicating that the following output will show the original array
print("Original arrays:")
print(array_nums)  # Print the contents of 'array_nums'

# Use the 'sorted()' function to rearrange the elements in 'array_nums' based on a custom key
# The 'key' parameter uses a lambda function to sort the elements:
#   - It places positive numbers before negative numbers and zeros, maintaining their original order
#   - Zeros are placed at the front (index 0) of the sorted list
result = sorted(array_nums, key=lambda i: 0 if i == 0 else 1 if i < 0 else -1)

# Display the rearranged array where positive numbers come before negative numbers and zeros
print("\nRearrange positive and negative numbers of the said array:")
print(result)


# Write a Python program to rearrange an array by alternating positive and negative numbers using lambda.


def rearrange_positives_and_negatives(arr: list[int]) -> list[int]:
    positives = list(filter(lambda x: x > 0, arr))
    negatives = list(filter(lambda x: x < 0, arr))

    res = []
    for index in range(len(positives)):
        res.append(positives[index])
        if index < len(negatives):
            res.append(negatives[index])

    return res


print(rearrange_positives_and_negatives([-1, 2, -3, 5, 7, 8, 9, -10]))

# 15. Add Lists with Lambda
#
# Write a Python program to add two given lists using map and lambda.
#
# Original list:
# [1, 2, 3]
# [4, 5, 6]
# Result: after adding two list
# [5, 7, 9]


def add_lists(list1: list[int], list2: list[int]) -> list[int]:
    return list(map(lambda x, y: x + y, list1, list2))


# 18. Palindrome Filter Lambda
#
# Write a Python program to find palindromes in a given list of strings using Lambda.
#
# Orginal list of strings:
# ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
# List of palindromes:
# ['php', 'aaa']


def palindrome_filter(list_of_strings: list[str]) -> list[str]:
    return list(filter(lambda x: x == x[::-1], list_of_strings))


print(palindrome_filter(["php", "w3r", "Python", "abcd", "Java", "aaa"]))


def anagram_finder(list_strings: list[str], word: str) -> list[str]:
    def is_anagram(s1: str, s2: str) -> bool:
        for char in s1:
            if char not in s2:
                return False
        return True

    return list(filter(lambda x: is_anagram(x, word), list_strings))


print(anagram_finder(["listen", "silent", "enlist", "google", "gooegl"], "google"))

# 20. Number Extraction & Filter Lambda
# Write a Python program to find the numbers in a given string and store them in a list.
# Afterward, display the numbers that are longer than the length of the list in sorted form.
# Use the lambda function to solve the problem.

# Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
# Numbers in sorted form:
# 20 23 56


def number_extraction_and_filter(string: str) -> list[int]:
    numbers = list(
        filter(lambda x: x.isdigit() and int(x) > len(string.split()), string.split())
    )
    return sorted(numbers)


print(number_extraction_and_filter("sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"))

# 27. Sort Sublists Lambda
#
# Write a Python program to sort each sublist of strings in a given list of lists using lambda.
#
#
# Original list:
# [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
# After sorting each sublist of the said list of lists:
# [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]


def sort_sublists(list_of_lists: list[list[str]]) -> list[list[str]]:
    return list(map(lambda x: sorted(x), list_of_lists))


print(
    sort_sublists(
        [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]
    )
)
# 30. Matrix Row Sum Sort Lambda
#
# Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.
#
# Original Matrix:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
# Original Matrix:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]


def sort_matrix_by_row_sum(matrix: list[list[int]]) -> list[list[int]]:
    lambda_row_sum = lambda row: sum(row)
    return sorted(matrix, key=lambda_row_sum)


print(sort_matrix_by_row_sum([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))
print(sort_matrix_by_row_sum([[1, 2, 3], [-2, 4, -5], [1, -1, 1]]))


# 32. Count Floats Lambda
#
# Write a Python program to count float values in a mixed list using lambda.
#
# Original list:
# [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# Number of floats in the said mixed list:
# 3


def count_floats(mixed_list: list) -> int:
    return len(list(filter(lambda x: isinstance(x, float), mixed_list)))


print(count_floats([1, "abcd", 3.12, 1.2, 4, "xyz", 5, "pqr", 7, -5, -12.22]))

# 40. Nested List Intersection Lambda
#
# Write a Python program to find the nested list elements, which are present in another list using lambda.
#
# Original lists: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# Intersection of said nested lists:
# [[12], [7, 11], [1, 5, 8]]


def nested_list_intersection(
    list1: list[int], list2: list[list[int]]
) -> list[list[int]]:
    visited: set = set()
    res = []

    for element in list1:
        if element not in visited:
            visited.add(element)

    for list_el in list2:
        res.append(list(filter(lambda x: x in visited, list_el)))

    return res


print(
    nested_list_intersection(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]],
    )
)


# Define a function 'average_tuple' that calculates the average of elements in a tuple of tuples
def average_tuple(nums):
    # Use 'zip(*nums)' to unpack the tuples in 'nums' and then apply 'map' with a lambda to calculate the averages
    # For each position (index) in the unpacked tuples, calculate the average of elements at that position across tuples
    # Convert the averages into a tuple
    print(list(zip(*nums)), "tuples")
    result = tuple(map(lambda x: sum(x) / float(len(x)), zip(*nums)))

    # Return the tuple of average values
    return result


# Create a tuple of tuples 'nums' containing integer values
nums = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))

# Print the original tuple 'nums' and the average value of numbers in the tuple of tuples using 'average_tuple' function
print("Original Tuple:")
print(nums)
print(
    "\nAverage value of the numbers of the said tuple of tuples:\n", average_tuple(nums)
)

# Create another tuple of tuples 'nums' containing integer values including negative numbers
nums = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))

# Print the original tuple 'nums' and the average value of numbers in the tuple of tuples using 'average_tuple' function
print("\nOriginal Tuple:")
print(nums)
print(
    "\nAverage value of the numbers of the said tuple of tuples:\n", average_tuple(nums)
)
