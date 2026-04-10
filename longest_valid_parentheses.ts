// # 32. Longest Valid Parentheses
// # Given a string containing just the characters '(' and ')', return the
// length of the
// # longest valid (well-formed) parentheses substring.
// # Example 1:

// # Input: s = "(()"
// # Output: 2
// # Explanation: The longest valid parentheses substring is "()".
// # Example 2:

// # Input: s = ")()())"
// # Output: 4
// # Explanation: The longest valid parentheses substring is "()()".
// # Example 3:

// # Input: s = ""
// # Output: 0

// # Constraints:

// # 0 <= s.length <= 3 * 104
// # s[i] is '(', or ')'.

function longestValidParentheses(s: string): number {
  let maxLength = 0;
  const stackIndexes: number[] = [-1];

  for (let i = 0; i < s.length; i++) {
    let char = s[i];

    if (char === "(") {
      // stack.push(char);
      stackIndexes.push(i);
    } else if (char === ")") {
      if (stackIndexes.length === 0) {
        stackIndexes.push(i);
        continue;
      }

      stackIndexes.pop();

      if (stackIndexes.length === 0) {
        stackIndexes.push(i);
        continue;
      }

      const previousIndex = stackIndexes[stackIndexes.length - 1];
      maxLength = Math.max(maxLength, i - (previousIndex ?? 0));
      continue;
    }
  }
  return maxLength;
}
