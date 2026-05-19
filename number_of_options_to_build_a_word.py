
# Number of options to build up a word
# You are given a target word and a collection of strings. Your task is to count in how
# many ways you can build up a target word from the strings in the collection.
# You can use any string in the collection as many times as needed, but you need
# to use that string as it is (meaning you can't remove characters from it). 
# Either use all of it or don't use it. If it doesn't fully match your needs,
# see if another string in the collection does.
# Examples
# For target word "example" and collection of words ["exa", "exam", "ple"]
# there is just 1 option of how you can use the strings in the collection to 
# create the word "example": taking strings "exam" and "ple".
# So you should return 1 for this case.
# For target word "example" and collection of words ["exa", "exam", "ple", "mple"] we now have 2 options:
# "exa" + "mple"
# "exam" + "ple"
# So you should return 2 for this case.
# For target word "example" and collection of words ["exa", "ple"] we cannot construct the target word.
# So you should return 0 for this case.
# Input
# For input, you will receive:
# target - target word as a string
# words - a tuple of unique strings
# All strings will be lowercase. All inputs are valid.
# Output
# You should return the number of ways you can build up a target word from the strings in
# the given collection.
# Return 0 if this is impossible.
# Return 1 if the target is an empty string.
# Tests
# Total number of tests is 300.
# You need to come up with an efficient approach so your solution doesn't time out.
# Good luck!
# Dynamic Programming

from typing import List

def get_options_count(target: str, words: List[str]) -> int:
    
    if target == "":
        return 1
    dp = [0 for _ in range(len(target) + 1)]
    dp[0] = 1
    for i in range(1, len(target) + 1):
        for word in words:
            if target[i - len(word):i] == word:
                dp[i] += dp[i - len(word)]
    return dp[len(target)] if dp[len(target)] > 0 else 0


print(get_options_count("example", ["exa", "exam", "ple", "mple"]))

# def get_options_count(target, arr):
#     options = [1]
#     for n in range(1, len(target)+1):
#         options.append(sum(options[-len(s)] for s in arr if target[-n:].startswith(s)))
#     return options[-1] 