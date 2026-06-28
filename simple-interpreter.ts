// interpreters: HQ9+
// 2006166% of 2,18914 of 12,533Voile3 Issues Reported
// You task is to implement an simple interpreter for the notorious esoteric
// language HQ9+ that will work for a single character input:

// If the input is 'H', return 'Hello World!'
// If the input is 'Q', return the input
// If the input is '9', return the full lyrics of 99 Bottles of Beer. It should
//  be formatted like this:
// 99 bottles of beer on the wall, 99 bottles of beer.
// Take one down and pass it around, 98 bottles of beer on the wall.
// 98 bottles of beer on the wall, 98 bottles of beer.
// Take one down and pass it around, 97 bottles of beer on the wall.
// 97 bottles of beer on the wall, 97 bottles of beer.
// Take one down and pass it around, 96 bottles of beer on the wall.
// ...
// ...
// ...
// 2 bottles of beer on the wall, 2 bottles of beer.
// Take one down and pass it around, 1 bottle of beer on the wall.
// 1 bottle of beer on the wall, 1 bottle of beer.
// Take one down and pass it around, no more bottles of beer on the wall.
// No more bottles of beer on the wall, no more bottles of beer.
// Go to the store and buy some more, 99 bottles of beer on the wall.
// For everything else, don't return anything (return null in C#, None in Rust, and "" in Haskell).
// (+ has no visible effects so we can safely ignore it.)

export function HQ9(code: string): string | undefined {
  function generateLyrics(): string {
    let startingNumberOfBeers = 99;
    const res: string[] = [];

    for (let index = startingNumberOfBeers; index >= 2; index--) {
      res.push(
        `${index} bottles of beer on the wall, ${index} bottles of beer.`,
      );

      if (index === 2) {
        res.push(
          "Take one down and pass it around, 1 bottle of beer on the wall.",
        );
      } else {
        res.push(
          `Take one down and pass it around, ${index - 1} bottles of beer on the wall.`,
        );
      }
    }

    res.push("1 bottle of beer on the wall, 1 bottle of beer.")
    res.push("Take one down and pass it around, no more bottles of beer on the wall.")
    res.push("No more bottles of beer on the wall, no more bottles of beer.")
    res.push("Go to the store and buy some more, 99 bottles of beer on the wall.")


    return res.join("\n");
  }

  const validChars = ["H", "Q", "9"];
  for (const char of code) {
    if (!validChars.includes(char)) return undefined;

    if (char === "Q") return char;
    if (char === "9") return generateLyrics();
    return "Hello World!";
  }
}

type HQ9Command = "H" | "Q" | "9";

const HQ9_HANDLERS: Record<HQ9Command, (input: string) => string> = {
  "H": () => "Hello World!",
  "Q": (input) => input,
  "9": () => generateLyricsForDictionary(),
};

function generateLyricsForDictionary(): string {
  const res: string[] = [];

  for (let index = 99; index >= 2; index--) {
    res.push(
      `${index} bottles of beer on the wall, ${index} bottles of beer.`,
    );

    if (index === 2) {
      res.push(
        "Take one down and pass it around, 1 bottle of beer on the wall.",
      );
    } else {
      res.push(
        `Take one down and pass it around, ${index - 1} bottles of beer on the wall.`,
      );
    }
  }

  res.push("1 bottle of beer on the wall, 1 bottle of beer.");
  res.push(
    "Take one down and pass it around, no more bottles of beer on the wall.",
  );
  res.push("No more bottles of beer on the wall, no more bottles of beer.");
  res.push(
    "Go to the store and buy some more, 99 bottles of beer on the wall.",
  );

  return res.join("\n");
}

function isHQ9Command(char: string): char is HQ9Command {
  return char === "H" || char === "Q" || char === "9";
}

export function HQ9Dictionary(code: string): string | undefined {
  for (const char of code) {
    if (!isHQ9Command(char)) {
      return undefined;
    }

    return HQ9_HANDLERS[char](code);
  }
}
