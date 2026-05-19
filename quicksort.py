

def quicksort(arr: list[int]) -> list[int]:
    
    if len(arr) <= 1:
        return arr
    
    n = len(arr) 
    pivot_index = n //2
    
    lower_than_pivot = []
    greater_than_pivot = []
    
    pivot = arr[pivot_index] 
    
    for i, num in enumerate(arr):
        if num < pivot:
            lower_than_pivot.append(num)
        elif num > pivot:
            greater_than_pivot.append(num)
    
    return quicksort(lower_than_pivot) + [pivot] + quicksort(greater_than_pivot)

arr = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(arr))