# 5 kyu
# Moving Zeros To The End
# Write an algorithm that takes an array and moves all of the zeros to the end, 
# preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
from typing import List


def move_zeros(lst: List[int]) -> List[int]:
    number_of_zeros = 0
    
    res = []
    
    for num in lst:
        if num != 0:
            res.append(num)
            continue
        number_of_zeros +=1
        
    while number_of_zeros > 0:
        res.append(0)
        number_of_zeros -=1
        
    return res