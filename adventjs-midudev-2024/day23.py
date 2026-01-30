# The elves are working on a system to verify children's gift lists 👧👦. However, some lists are incomplete 
# and numbers are missing!
# 
# Your task is to write a function that, given an array of numbers, finds all the numbers that are missing between 1 and n (where n is the size of the array or the highest number in the array).
# 
# Keep in mind that:
# 
# Numbers may appear more than once and others may be missing
# The array always contains positive integers
# Counting always starts from 1
# findMissingNumbers([1, 2, 4, 6]);
# // [3, 5]
# 
# findMissingNumbers([4, 8, 7, 2]);
# // [1, 3, 5, 6]
# 
# findMissingNumbers([3, 2, 1, 1]);
# // []
# 
# findDisappearedNumbers([5, 5, 5, 3, 3, 2, 1]);
# // [4]

def find_missing_numbers(numbers: list[int]) -> list[int]:
    
    if not numbers:
        return []
    
    res = []
    
    for i in range(1, len(numbers) + 1):
        if i not in numbers:
            res.append(i)
            
    return res

print(find_missing_numbers([1, 2, 4, 6]))
print(find_missing_numbers([4, 8, 7, 2]))
print(find_missing_numbers([3, 2, 1, 1]))
print(find_missing_numbers([5, 5, 5, 3, 3, 2, 1]))