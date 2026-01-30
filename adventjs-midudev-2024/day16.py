# ❄️ Cleaning the snow path
# The elves are working hard to clear paths filled with magical snow ❄️. This snow has a special property: 
# if two identical and adjacent snow piles are found, they disappear automatically.
# 
# Your task is to write a function to help the elves simulate this process. The path is represented by a 
# string and each snow pile by a character.
# 
# You need to remove all adjacent snow piles that are the same until no more moves are possible.
# 
# The result should be the final path after removing all duplicate piles:
# 
# removeSnow("zxxzoz"); // -> "oz"
# // 1. Remove "xx", resulting in "zzoz"
# // 2. Remove "zz", resulting in "oz"
# 
# removeSnow("abcdd"); // -> "abc"
# // 1. Remove "dd", resulting in "abc"
# 
# removeSnow("zzz"); // -> "z"
# // 1. Remove "zz", resulting in "z"
# 
# removeSnow("a"); // -> "a"
# // No duplicate piles

def remove_snow(string: str) -> str:
    
    if not string:
        return ""
    
    # The algorithm is very simple, we iterate through the string and compare the current character with the next one
    # if they are the same, we remove the next character
    i = 0
    r = len(string) - 1
    while i < r:
        if i + 1 < len(string) and (string[i] == string[i + 1]):
            string = string[:i] + string[i + 2:]
            i = 0
        else:
            i += 1
    return string
    
print(remove_snow("zxxzoz"))
print(remove_snow("abcdd"))
print(remove_snow("zzz"))
print(remove_snow("a"))