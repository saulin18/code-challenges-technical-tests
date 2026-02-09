# You are given two 0-indexed strings s and target. You can take some letters from s and rearrange them
# to form new strings.
# Return the maximum number of copies of target that can be formed by taking letters from s and rearranging them.
# Example 1:
# Input: s = "ilovecodingonleetcode", target = "code"
# Output: 2
# Explanation:
# For the first copy of "code", take the letters at indices 4, 5, 6, and 7.
# For the second copy of "code", take the letters at indices 17, 18, 19, and 20.
# The strings that are formed are "ecod" and "code" which can both be rearranged into "code".
# We can make at most two copies of "code", so we return 2.
# Example 2:
# Input: s = "abcba", target = "abc"
# Output: 1
# Explanation:
# We can make one copy of "abc" by taking the letters at indices 0, 1, and 2.
# We can make at most one copy of "abc", so we return 1.
# Note that while there is an extra 'a' and 'b' at indices 3 and 4, we cannot reuse the letter 'c' at index 2, so we cannot make a second copy of "abc".
# Example 3:
# Input: s = "abbaccaddaeea", target = "aaaaa"
# Output: 1
# Explanation:
# We can make one copy of "aaaaa" by taking the letters at indices 0, 3, 6, 9, and 12.
# We can make at most one copy of "aaaaa", so we return 1.
# Constraints:
# 1 <= s.length <= 100
# 1 <= target.length <= 10
# s and target consist of lowercase English letters.

from collections import Counter
def rearrangeCharacters(s, target):
    """
    :type s: str
    :type target: str
    :rtype: int
    """

    if s is None or target is None:
        return 0

    counter_of_iter_string = Counter(filter(lambda x: x in target, s))

    if len(counter_of_iter_string) < len(set(target)):
        return 0

    if any(char not in counter_of_iter_string for char in target):
        return 0

    counter_of_target = Counter(target)

    for char, repetitions in counter_of_iter_string.items():
        counter_of_iter_string[char] = repetitions // counter_of_target[char]

    return min(counter_of_iter_string.values())


s = "ilovecodingonleetcode"
target = "code"
print(rearrangeCharacters(s, target))
