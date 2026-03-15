//Sort Strings by Most Contiguous Vowel
// //The goal of this Kata is to write a function that will receive an array of strings as its single
// argument, then the strings are each processed and sorted (in desending order) based on the
// length of the single longest sub-string of contiguous vowels ( aeiouAEIOU ) that may be contained
// within the string. The strings may contain letters, numbers, special characters, uppercase, lowercase,
// whitespace, and there may be (often will be) multiple sub-strings of contiguous vowels. We are only interested
// in the single longest sub-string of vowels within each string, in the input array.
//
//Example:
//
//str1 = "what a beautiful day today"
//str2 = "it's okay, but very breezy"
//When the strings are sorted, str1 will be first as its longest sub-string of contiguous vowels "eau" is of length 3, while str2 has as its longest sub-string of contiguous vowels "ee", which is of length 2.
//
//If two or more strings in the array have maximum sub-strings of the same length, then the strings should
//remain in the order in which they were found in the orginal array.

/**
 *
 * @param {string[]} strings
 * @returns {string[]}
 */
function sortStringsByVowels(strings: string[]) {

  const details = strings.map((string, index) => {
    const matchs = string.match("/[aeiou]+/ig") || [];
    const max = Math.max(...matchs.map((g) => g.length), 0);

    return { string, index, max };
  });

  return details
    .sort((a, b) => b.max - a.max || a.index - b.index)
    .map((a) => a.string);
}

/**
 *
 * @param {string[]} strings
 * @returns {string[]}
 */
//function sortStringsByVowels(strings) {
//  const myMap = {};
//  const vowels = "aeiouAEIOU";
//
//  for (let index = 0; index < strings.length; index++) {
//    myMap[strings[index]] = [0, 0];
//    for (let j = 0; j < strings[index].length; j++) {
//      const char = strings[index][j];
//
//      const prevChar = j > 0 ? strings[index][j - 1] : "";
//
//      if (vowels.includes(char)) {
//        let [reps, maxReps] = myMap[strings[index]];
//
//        if (!vowels.includes(prevChar)) reps = 1;
//
//        if (vowels.includes(prevChar)) reps += 1;
//
//        myMap[strings[index]] = [reps, Math.max(maxReps, reps)];
//      }
//      myMap[strings[index]] = [(reps += 1), j];
//    }
//  }
//
//  strings.sort((a, b) => {
//    const [_, vowelsCount] = myMap[a];
//    const [latest, vowelsCountOther] = myMap[b];
//    return vowelsCountOther - vowelsCount;
//  });
//
//  return strings;
//}
//
let str1 = "what a beautiful day today";
let str2 = "it's okay, but very breezy";
console.log(sortStringsByVowels([str1, str2]));
