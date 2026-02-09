# 1189. Maximum Number of Balloons
# Given a string text, you want to use the characters of text to form as
# many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.
# Example 1:
# Input: text = "nlaebolko"
# Output: 1
# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:
# Input: text = "leetcode"
# Output: 0
# Constraints:
# 1 <= text.length <= 104
# text consists of lower case English letters only.
# Note: This question is the same as 2287: Rearrange Characters to Make Target String.
from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        target = "balloon"
        if text is None or target is None:
            return 0

        counter_of_iter_string = Counter(filter(lambda x: x in target, text))

        if len(counter_of_iter_string) < len(set(target)):
            return 0

        if any(char not in counter_of_iter_string for char in target):
            return 0

        counter_of_target = Counter(target)

        for char, repetitions in counter_of_iter_string.items():
            counter_of_iter_string[char] = repetitions // counter_of_target[char]

        return min(counter_of_iter_string.values())