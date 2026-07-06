# 2121. Intervals Between Identical Elements
# You are given a 0-indexed array of n integers arr.
# The interval between two elements in arr is defined as the absolute
# difference between their indices. More formally, the interval between arr[i]
# and arr[j] is |i - j|.
# Return an array intervals of length n where intervals[i] is the sum of
# intervals between arr[i] and each
# element in arr with the same value as arr[i].
# Note: |x| is the absolute value of x.
# Example 1:
# Input: arr = [2,1,3,1,2,3,3]
# Output: [4,2,7,2,4,4,5]
# Explanation:
# - Index 0: Another 2 is found at index 4. |0 - 4| = 4
# - Index 1: Another 1 is found at index 3. |1 - 3| = 2
# - Index 2: Two more 3s are found at indices 5 and 6. |2 - 5| + |2 - 6| = 7
# - Index 3: Another 1 is found at index 1. |3 - 1| = 2
# - Index 4: Another 2 is found at index 0. |4 - 0| = 4
# - Index 5: Two more 3s are found at indices 2 and 6. |5 - 2| + |5 - 6| = 4
# - Index 6: Two more 3s are found at indices 2 and 5. |6 - 2| + |6 - 5| = 5
# Example 2:
# Input: arr = [10,5,10,10]
# Output: [5,0,3,4]
# Explanation:
# - Index 0: Two more 10s are found at indices 2 and 3. |0 - 2| + |0 - 3| = 5
# - Index 1: There is only one 5 in the array, so its sum of intervals to
# identical elements is 0.
# - Index 2: Two more 10s are found at indices 0 and 3. |2 - 0| + |2 - 3| = 3
# - Index 3: Two more 10s are found at indices 0 and 2. |3 - 0| + |3 - 2| = 4

# Constraints:

#     n == arr.length
#     1 <= n <= 105
#     1 <= arr[i] <= 105


from typing import List


# We can use a hash map to store the indices of the elements in the array.
# Then we can iterate through the array and for each element, we can add the interval between
# every index we have put in the hash map.
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        # We can use a hash map to store the index and the count of 
        # the elements in the array.
        intervals: list[int] = [0] * len(arr)
        prefix_sum: list[int] = [0] * len(arr)
        suffix_sum: list[int] = [0] * len(arr)
        hash_map: dict[int, tuple[int, int]] = {}
        
        for i in range(len(arr)):
            if arr[i] not in hash_map:
                hash_map[arr[i]] = (i, 1)
                continue
            
            
            sum, count = hash_map[arr[i]]
            prefix_sum[i] = i * count  - sum
            hash_map[arr[i]] = (hash_map[arr[i]][0] + i, hash_map[arr[i]][1] + 1)
            
        prefix_hash_map: dict[int, tuple[int, int]] = {}
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] not in prefix_hash_map:
                prefix_hash_map[arr[i]] = (i, 1)
                continue
            
            sum, count = prefix_hash_map[arr[i]]
            suffix_sum[i] = sum  - i * count
            prefix_hash_map[arr[i]] = (sum + i, count + 1)
            
        for i in range(len(arr)):
            intervals[i] = prefix_sum[i] + suffix_sum[i]
        return intervals
