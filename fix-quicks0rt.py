def quicksort(arr):
    if len(arr) <= 1:
        return arr
    p = arr[len(arr) // 2]
    return (
        quicksort(list(filter(lambda x: x < p, arr)))
        + list(filter(lambda x: x == p, arr))
        + quicksort(list(filter(lambda x: x > p, arr)))
    )
