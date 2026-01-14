
#Description:
#Subsets in this kata refers to sublists with only unique elements.
#
#Given a list, return the combined total of the sum of all "subsets".
#
#Example:
#
#[1, 2, 1] can be decomposed into:
#
#[1, 2, 1], [1, 2], [2, 1], [1], [2], [1] ---> (1)
#
#but sublist [1, 2, 1] has to be converted into one of ([1, 2] or [2, 1]) in order to make it a "subset".
#
#Therefore the combined total is:
#
#3 + 3 + 3 + 1 + 2 + 1 = 13 (Note that I've added the sums in the same order as (1)).
#0 < Size of list <= 10 ^ 5
#function subset(array, target, memo = {}) {
#    if (target === 0) {
#        return [];
#    }
#
#    if (target < 0 || array.length === 0) {
#        return null;
#    }
#
#    // Usar índice para evitar problemas de memoización
#    const key = `${target}-${array.length}`;
#
#    if (key in memo) {
#        return memo[key];
#    }
#
#    for (let i = 0; i < array.length; i++) {
#        const currentNum = array[i];
#
#        // Crear array sin el elemento actual
#        const newArray = [...array];
#        newArray.splice(i, 1);
#
#        const result = subset(newArray, target - currentNum, memo);
#
#        if (result !== null) {
#            memo[key] = [...result, currentNum];
#            return memo[key];
#        }
#    }
#
#    memo[key] = null;
#    return null;
#}

# We will solve this using a backtracking with memoization approach, the memoization key will be unique
def solve(lst, memo = {}, index = 0):
    key = f"{tuple(lst)}-{index}"

    if not lst:
        memo[key] = 0

    if key in memo: return memo[key]

    total_sum = 0
    for i in range(len(lst)):
        number = lst[i]

        # Create a new list without the current element
        new_lst = lst[:i] + lst[i+1:]

        # For preventing duplicates, including the number
        if number not in new_lst:
            total_sum += number
            total_sum += solve(new_lst, memo, index + 1)

        # Dont including the number
        total_sum += solve(new_lst, memo, index + 1)

    memo[key] = total_sum
    return memo[key]



def is_valid_subset_with_no_duplicates(arr):
    return len(arr) == len(set(arr))
