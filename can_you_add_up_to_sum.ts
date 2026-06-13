
// Can you add up to the target sum?
// Given an array of numbers and a target number, return an array of numbers that
//  sums to the target number.

// You can only pick numbers from the given array, but you can pick them as many 
// times as you like.

// To not create different solutions you should always pick as big a number as possible.

// The array of numbers will be sorted in descending order (bigger numbers come 
// first, smaller numbers later).

// If it is impossible to get to the target number, return an empty array
//  (or, depending on language, an empty value).
// Input
// As arguments you will receive:
// numbers: an array of numbers, positive integers from 1 to 1 000,
//  sorted in descending order.
// target: a number, a positive integer from 1 to 100 000.
// All inputs will be valid.
// Your function should return an array of integers from the input array that, 
// when summed, equals the target number.
// Return an empty array (Haskell: Nothing) when it is not possible.
// Your function should pass 10 fixed tests and 490 random tests.
// Total number of tests is 500.


export function getNumbers(numbers: number[], target: number): number[] {
    const memo: Record<number, boolean> = {}
    const result: number[] = []

    function backtrack(start: number, remainder: number): boolean {
        if (remainder === 0) {
            return true
        }
        if (remainder < 0) {
            memo[remainder] = false
            return false
        }

        if(start >= numbers.length){
            memo[remainder] = false
            return false
        }

        if (memo[remainder]) {
            return memo[remainder]
        }
        for (let i = start; i < numbers.length; i++) {
            const num = numbers[i]
            result.push(num)
            if(backtrack(i, remainder - num)) return true
            result.pop()
        }
        memo[remainder] = false
        return false
    }
    return backtrack(0, target) ? result : []
    }


