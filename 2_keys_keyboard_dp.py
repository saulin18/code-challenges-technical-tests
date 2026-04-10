# 650. 2 Keys Keyboard
# There is only one character 'A' on the screen of a notepad. You can perform one
# of two operations on this notepad for each step:
# Copy All: You can copy all the characters present on the screen (a partial
# copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# Given an integer n, return the minimum number of operations to get the character
# 'A' exactly n times on the screen.
# Example 1:
# Input: n = 3
# Output: 3
# Explanation: Initially, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
# Example 2:
# Input: n = 1
# Output: 0
# Constraints:
# 1 <= n <= 1000


class Solution:
    def minSteps(self, n: int) -> int:

        # By defaults
        actual_quantity_of_a = 1

        def recursive(
            quantity_of_a: int, quantity_of_copied_a: int, step: int, memo: dict
        ) -> int:
            if quantity_of_a == n:
                return step

            if quantity_of_a > n:
                return float("inf")

            if (quantity_of_a, quantity_of_copied_a) in memo:
                return memo[(quantity_of_a, quantity_of_copied_a)]

            copy = (
                recursive(quantity_of_a, quantity_of_a, step + 1, memo)
                if quantity_of_a != quantity_of_copied_a
                else float("inf")
            )
            paste = (
                recursive(
                    quantity_of_a + quantity_of_copied_a,
                    quantity_of_copied_a,
                    step + 1,
                    memo,
                )
                if quantity_of_copied_a > 0
                else float("inf")
            )
            memo[(quantity_of_a, quantity_of_copied_a)] = min(copy, paste)
            return memo[(quantity_of_a, quantity_of_copied_a)]

        return recursive(actual_quantity_of_a, 0, 0, {})


# You can do it also with prime factorization since the number of operations is the sum of the prime factors
# Example:
# 12 = 2 * 2 * 3
# 12 = 4 * 3
# So the number of operations is 4 + 3 = 7

# class Solution:
#     def minSteps(self, n: int) -> int:
#         if n == 1:
#             return 0
        
#         operations = 0
#         factor = 2
        
#         # Prime factorization
#         while n > 1:
#             while n % factor == 0:
#                 operations += factor
#                 n //= factor
#             factor += 1
            
#         return operations