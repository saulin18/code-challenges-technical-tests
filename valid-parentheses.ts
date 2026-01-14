function isValid(s: string) {
  const arr: string[] = [];

  for (let i = 0; i < s.length; i++) {
    let char = s[i];
    let lastChar = arr[arr.length - 1];

    if (char === "(" || char === "{" || char === "[") {
      arr.push(char);
    } else if (
      (char === ")" && lastChar === "(") ||
      (char === "}" && lastChar === "{") ||
      (char === "]" && lastChar === "[")
    ) {
      arr.pop();
      continue;
    }

    return false;
  }
  
  return arr.length === 0;
}

console.log(isValid("([)]"));
