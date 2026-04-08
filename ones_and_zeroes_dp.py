# You are given an array of binary strings strs
# and two integers m and n.
# Return the size of the largest subset of strs such that there are at
# most m 0's and n 1's in the subset.
# A set x is a subset of a set y if all elements of x are also
# elements of y.
# Example 1:
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's
# is {"10", "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
# Example 2:
# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: The largest subset is {"0", "1"}, so the answer is 2.
# Constraints:
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] consists only of digits '0' and '1'.
# 1 <= m, n <= 100

# class Solution:
#     def findMaxForm(self, strs, m, n):
#         # dp[i][j] = max subset size with i zeros and j ones
#         dp = [[0] * (n + 1) for _ in range(m + 1)]
        
#         for s in strs:
#             zeros = s.count('0')
#             ones = s.count('1')
            
#             # Traverse backwards (0/1 knapsack)
#             for i in range(m, zeros - 1, -1):
#                 for j in range(n, ones - 1, -1):
#                     dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        
#         return dp[m][n]


from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        def recursive(
            index: int,
            actual_count_of_0s: int,
            actual_count_of_1s: int,
            memo: dict = {},
            actual_res: List[str] = [],
        ) -> int:
            """
            We will recursively try to add the current string to the result and check if it is valid or
            not. If it is valid, we will add it to the result and move to the next string.
            If it is not valid, we will move to the next string without adding it to the result.

            :param index: current index of the string we are trying to add to the result
            :type index: int
            :param actual_count_of_0s: actual count of 0s in the current result
            :type actual_count_of_0s: int
            :param actual_count_of_1s: actual count of 1s in the current result
            :type actual_count_of_1s: int
            :param memo: memoization dictionary to store already computed results
            :type memo: dict
            :param actual_res: actual result we are trying to build
            :type actual_res: List[str]
            :return: Description
            :rtype: int
            """
            if index >= len(strs):
                return 0

            if (index, actual_count_of_0s, actual_count_of_1s) in memo:
                return memo[(index, actual_count_of_0s, actual_count_of_1s)]

            current_string = strs[index]
            count_of_0s = current_string.count("0")

            if actual_count_of_0s + count_of_0s > m:
                # We cannot add the current string to the result because it will exceed the maximum count
                # of 0s
                return recursive(
                    index + 1, actual_count_of_0s, actual_count_of_1s, memo, actual_res
                )

            count_of_1s = current_string.count("1")
            if actual_count_of_1s + count_of_1s > n:
                # We cannot add the current string to the result because it will exceed the maximum count
                # of 1s
                return recursive(
                    index + 1, actual_count_of_0s, actual_count_of_1s, memo, actual_res
                )
            
            # We can add the current string to the result
            result_with_current = recursive(
                index + 1,
                actual_count_of_0s + count_of_0s,
                actual_count_of_1s + count_of_1s,
                memo,
                actual_res + [current_string]
            ) + 1
            # The one is because this is the favorable branch, 1 string is added to the result, 
            # so we add 1 to the result of the recursive call
            # We can also skip the current string
            result_without_current = recursive(
                index + 1,
                actual_count_of_0s,
                actual_count_of_1s,
                memo,
                actual_res
            )
            memo[(index, actual_count_of_0s, actual_count_of_1s)] = max(result_with_current, result_without_current) 
            return memo[(index, actual_count_of_0s, actual_count_of_1s)]
        
        return recursive(0, 0, 0, {}, [])
        
        
 
print(
    Solution.findMaxForm(
        Solution(),
        ["10", "0001", "111001", "1", "0"],
        5,
        3,
    )
)    
print(
    Solution.findMaxForm(
        Solution(),
        ["10", "0", "1"],
        1,
        1
    )
)    