# 599. Minimum Index Sum of Two Lists
# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j
# should be the minimum value among all the other common strings.

# Return all the common strings with the least index sum. Return the answer in any order.
# Example 1:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only common string is "Shogun".
# Example 2:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.
# Example 3:
# Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
# Output: ["sad","happy"]
# Explanation: There are three common strings:
# "happy" with index sum = (0 + 1) = 1.
# "sad" with index sum = (1 + 0) = 1.
# "good" with index sum = (2 + 2) = 4.
# The strings with the least index sum are "sad" and "happy".
# Constraints:
# 1 <= list1.length, list2.length <= 1000
# 1 <= list1[i].length, list2[i].length <= 30
# list1[i] and list2[i] consist of spaces ' ' and English letters.
# All the strings of list1 are unique.
# All the strings of list2 are unique.
# There is at least a common string between list1 and list2.

from typing import List

from collections import defaultdict


def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

    # The keys will be the words and the value the sum of the indexes, the default is 0
    my_dict = defaultdict(int)
    minimum_elements = []
    minimum_count = -5

    for i, word in enumerate(list1):
        my_dict[word] += i

    for i, word2 in enumerate(list2):
        if word2 in my_dict:
            my_dict[word2] += i
            new_min = my_dict[word2]

            if new_min <= minimum_count or minimum_count == -5:
                minimum_elements.append((word2, new_min))
                minimum_count = new_min

    return [word for word, count in minimum_elements if count <= minimum_count]


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = [
    "Piatti",
    "The Grill at Torrey Pines",
    "Hungry Hunter Steakhouse",
    "Shogun",
]
print(findRestaurant(list1, list2))
