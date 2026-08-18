# 801. Minimum Swaps To Make Sequences Increasing
# You are given two integer arrays of the same length nums1 and nums2. In one operation, you are allowed to
# swap nums1[i] with nums2[i].

# For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], you can swap the element at i = 3 to obtain
# nums1 = [1,2,3,4] and nums2 = [5,6,7,8].
# Return the minimum number of needed operations to make nums1 and nums2 strictly increasing. The
# test cases are generated so that the given input always makes it possible.

# An array arr is strictly increasing if and only if arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1].

# Example 1:

# Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
# Output: 1
# Explanation:
# Swap nums1[3] and nums2[3]. Then the sequences are:
# nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4]
# which are both strictly increasing.
# Example 2:
# Input: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
# Output: 1
# Constraints:
# 2 <= nums1.length <= 105
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 2 * 105

from typing import List


# class Solution:
#     def minSwap(self, nums1: List[int], nums2: List[int]) -> int:

#         INF = 10**18

#         def recursive(
#             index: int,
#             previous_swapped: bool,
#             list1: List[int],
#             list2: List[int],
#             memo: dict,
#         ) -> int:

#             if index >= len(list1):
#                 return 0

#             if (index, previous_swapped) in memo:
#                 return memo[(index, previous_swapped)]

#             if index == 0:
#                 without_swap = recursive(index + 1, False, list1, list2, memo)
#                 with_swap = recursive(index + 1, True, list1, list2, memo) + 1
#                 res = min(without_swap, with_swap)
#                 memo[(index, previous_swapped)] = res
#                 return res

#             # index >= 1: effective values at index-1 depend on whether we swapped there
#             if previous_swapped:
#                 prev_top, prev_bottom = list2[index - 1], list1[index - 1]
#             else:
#                 prev_top, prev_bottom = list1[index - 1], list2[index - 1]

#             a, b = list1[index], list2[index]

#             # No swap at index: rows stay (a, b)
#             without_swap = INF
#             if prev_top < a and prev_bottom < b:
#                 without_swap = recursive(index + 1, False, list1, list2, memo)

#             # Swap at index: rows become (b, a); cost +1
#             with_swap = INF
#             if prev_top < b and prev_bottom < a:
#                 with_swap = recursive(index + 1, True, list1, list2, memo) + 1

#             res = min(without_swap, with_swap)
#             memo[(index, previous_swapped)] = res
#             return res

#         memo = {}
#         return recursive(0, False, nums1, nums2, memo)

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:

        INF = 10**18
        dp = [[INF, INF] for _ in range(len(nums1))]
        dp[0][0] = 0
        dp[0][1] = 1
        for i in range(1, len(nums1)):
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                dp[i][0] = min(dp[i][0], dp[i-1][0])
                dp[i][1] = min(dp[i][1], dp[i-1][1] + 1)
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                dp[i][0] = min(dp[i][0], dp[i-1][1])
                dp[i][1] = min(dp[i][1], dp[i-1][0] + 1)
                
               
               
        return min(dp[len(nums1)-1][0], dp[len(nums1)-1][1])

solution = Solution()
print(solution.minSwap([1,3,5,4], [1,2,3,7]))
print(solution.minSwap([0,3,5,8,9], [2,1,4,6,9]))

# // problem: https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
# // solver:  https://leetcode.com/u/lambdacreature/

# function minSwap(nums1: number[], nums2: number[]): number {
#   const dive = (index: number, swaps: number, best: number): number => {
#     if (best <= swaps) {
#       return best;
#     }

#     if (index == nums1.length) {
#       return swaps;
#     }

#     if (index == 0) {
#       const results = [ best ];
#       results.push(dive(index+1, swaps, best));

#       const backup1 = nums1[index];
#       nums1[index] = nums2[index];
#       nums2[index] = backup1;

#       results.push(dive(index+1, swaps+1, best));

#       const backup2 = nums1[index];
#       nums1[index] = nums2[index];
#       nums2[index] = backup2;

#       return Math.min(...results);
#     }

#     const results = [ best ];

#     if (nums1[index-1] < nums1[index] && nums2[index-1] < nums2[index]) {
#       // nums1 and nums2 are strictly increasing without swap
#       results.push(dive(index+1, swaps, best));
#     }


#     if (nums1[index-1] < nums2[index] && nums2[index-1] < nums1[index]) { 
#       // nums1 and nums2 are strictly increasing after swap
#       const backup1 = nums1[index];
#       nums1[index] = nums2[index];
#       nums2[index] = backup1;

#       results.push(dive(index+1, swaps+1, best));

#       const backup2 = nums1[index];
#       nums1[index] = nums2[index];
#       nums2[index] = backup2;
#     }

#     return Math.min(...results);
#   };

#   const initialIndex = 0;
#   const initialSwaps = 0;
#   const initialBest  = nums1.length;

#   return dive(initialIndex, initialSwaps, initialBest);
# };


# // problem: https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
# // solver:  https://leetcode.com/u/lambdacreature/

# function minSwap(nums1: number[], nums2: number[]): number {
#   const INF = 200001;
#   const dp1 = [];
#   const dp2 = [];
#   for (const _ of nums1) {
#     dp1.push(INF);
#     dp2.push(INF);
#   }

#   // invariant: dp1[i] stores the minimum number of swaps
#   // needed to make nums1[0..i] and nums2[0..i] strictly increasing
#   // without swapping nums1[i] and nums2[i]
#   // dp2[i] is the same but having swapped nums1[i] and nums2[i]
#   //
#   // dp1[i] = INF if this is not possible
#   // dp2[i] = INF if this is not possible
#   // note: at least one of the two has to be true

#   // la cantidad minima de swaps para hacer ambos arrays
#   // estrictamente creciente se puede determinar de la forma siguente
#   //
#   // sea k1 la cantidad minima de swaps para hacer la secuencia entera estrictamente
#   // creciente sin contar el ultimo elemento, sin hacer swap a los penultimos
#   //
#   // y tambien sea k2 la cantidad minima de swaps para hacer el array entero estrictamente
#   // creciente sin tener en cuenta el ultimo elemento pero habiendo hecho swap a los penultimos
#   //
#   // IM HAVING A MELTDOWN QUE DP MAS TRICKY
#   // 

#   dp1[0] = 0;
#   dp2[0] = 1;

#   for (let i = 1; i < nums1.length; i++) {
#     if (dp1[i-1] != INF) {
#       if(nums1[i-1] < nums1[i] && nums2[i-1] < nums2[i]) {
#         dp1[i] = Math.min(dp1[i-1], dp1[i]);
#       }

#       if(nums1[i-1] < nums2[i] && nums2[i-1] < nums1[i]) {
#         dp2[i] = Math.min(dp1[i-1]+1, dp2[i]);
#       }
#     }

#     if (dp2[i-1] != INF) {
#       if(nums2[i-1] < nums1[i] && nums1[i-1] < nums2[i]) {
#         dp1[i] = Math.min(dp2[i-1], dp1[i]);
#       }

#       if(nums2[i-1] < nums2[i] && nums1[i-1] < nums1[i]) {
#         dp2[i] = Math.min(dp2[i-1]+1, dp2[i]);
#       }
#     }
#   }

#   const lastIndex = nums1.length-1;
#   const solution = Math.min(dp1[lastIndex], dp2[lastIndex]);

#   return solution;
# };