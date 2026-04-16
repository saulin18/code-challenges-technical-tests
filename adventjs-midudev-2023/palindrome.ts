// En el taller de Santa, los elfos aman los acertijos 🧠. Este año, han creado uno especial: un desafío para formar un palíndromo navideño.

// Un palíndromo es una palabra que se lee igual hacia adelante y hacia atrás. Los elfos quieren saber si es posible formar un palíndromo haciendo, como mucho, un intercambio de letras.

// Crea una función getIndexsForPalindrome que reciba una cadena de caracteres y devolverá:

// Si ya es un palíndromo, un array vacío.
// Si no es posible, null.
// Si se puede formar un palíndromo con un cambio, un array con las dos posiciones (índices) que se deben intercambiar para poder crearlo.
// Por ejemplo:

// getIndexsForPalindrome('anna') // []
// getIndexsForPalindrome('abab') // [0, 1]
// getIndexsForPalindrome('abac') // null
// getIndexsForPalindrome('aaaaaaaa') // []
// getIndexsForPalindrome('aaababa') // [1, 3]
// getIndexsForPalindrome('caababa') // null
// Si se puede formar el palíndromo con diferentes intercambios, siempre se debe devolver el primero que se encuentre.

function isPalindrome(s: string): boolean {
  for (let l = 0, r = s.length - 1; l < r; l++, r--) {
    if (s[l] !== s[r]) return false;
  }
  return true;
}

function getIndexsForPalindrome(word: string): number[] | null {
  if (isPalindrome(word)) {
    return [];
  }

  for (let i = 0; i < word.length; i++) {
    for (let j = i + 1; j < word.length; j++) {
      const chars = word.split("");
      const t = chars[i];
      chars[i] = chars[j];
      chars[j] = t;
      if (isPalindrome(chars.join(""))) {
        return [i, j];
      }
    }
  }

  return null;
}
