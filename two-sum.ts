
// Two Sum
// Write a function that takes an array of numbers (integers for the tests) 
// and a target number. It should find two different items in the array that,
//  when added together, give the target value. The indexes of these items shoul
// d then be returned in a tuple / list (depending on your language) like so: (index1, index2).

// For the purposes of this kata, some tests may have multiple answers; 
// any valid solutions will be accepted.

// The input will always be valid (numbers will be an array of length 2 or greater,
//  and all of the items will be numbers; target will always be the sum of two different 
// items from that array).

// Based on: https://leetcode.com/problems/two-sum/

// twoSum([1, 2, 3], 4) // returns [0, 2] or [2, 0]
// twoSum([3, 2, 4], 6) // returns [1, 2] or [2, 1]

// function twoSum(nums: number[], target: number): [number, number] {

//     const memo: Record<number, number> = {}

//     for (let index = 0; index < nums.length; index++) {
//         const num = nums[index]
//         const remainder = target - num

//         if (remainder in memo) {
//             return [memo[remainder], index]
//         }

//         memo[num] = index
//     }
//     return [0, 0]
// }

//N logn approach with lower bound binary search
function twoSum(nums: number[], target: number): [number, number] {
    const sorted = nums.map((num, index) => ({ num, index })).sort((a, b) => a.num - b.num)

    for (let index = 0; index < sorted.length; index++) {
        const num = sorted[index].num
        const remainder = target - num

        let left = index + 1
        let right = sorted.length - 1

        while (left <= right) {
            const middle = Math.floor((left + right) / 2)
            const middleNum = sorted[middle].num

            if (middleNum === remainder) {
                return [sorted[index].index, sorted[middle].index]
            } else if (middleNum < remainder) {
                left = middle + 1
            } else {
                right = middle - 1
            }
        }
    }

    return [0, 0]
}

console.log(twoSum([1, 2, 3], 4))
console.log(twoSum([3, 2, 4], 6))