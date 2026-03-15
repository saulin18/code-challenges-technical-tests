// In this Kata, you will be given a string and two indexes (a and b). Your task is to reverse the
//  portion of that string between those two indices inclusive.
// str = "codewars", a = 1, b = 5 --> "cawedors"
// str = "cODEWArs", a = 1, b = 5 --> "cAWEDOrs"
// Input will be lowercase and uppercase letters only.
// The first index a will always be smaller than the string length; the second index b can be greater than
// the string length.
// More examples in the test cases. Good luck!

function solve(st: string, a: number, b: number) {
  const arr = st.split("");
  const maxIndex = Math.min(arr.length - 1, b);
  let end = maxIndex;
  for (let index = a; index < end; index++, end--) {
    let char = arr[index];

    const temp = char;
    let endChar = arr[end];

    char = endChar;
    endChar = temp;
    arr[index] = char;
    arr[end] = endChar;
  }

  return arr.join("");
}

let str = "codewars";
const a = 1,
  b = 5;
console.log(solve(str, a, b));
