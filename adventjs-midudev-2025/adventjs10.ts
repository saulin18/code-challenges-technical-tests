//🎄 Profundidad de Magia Navideña
//En el Polo Norte, Santa Claus está revisando las cartas mágicas 📩✨ que recibe de los niños de todo el mundo. Estas cartas usan un antiguo
// lenguaje navideño en el que los corchetes [ y ] representan la intensidad del deseo.
//
//Cuanto más profunda sea la anidación de los corchetes, más fuerte es el deseo. Tu misión es averiguar la máxima profundidad en
// la que se anidan los [].
//
//Pero ¡cuidado! Algunas cartas pueden estar mal escritas. Si los corchetes no están correctamente balanceados
// (si se cierra antes de abrir, sobran cierres o faltan cierres), la carta es inválida y debes devolver -1.
//
//maxDepth('[]') // -> 1
//maxDepth('[[]]') // -> 2
//maxDepth('[][]') // -> 1
//maxDepth('[[][]]') // -> 2
//maxDepth('[[[]]]') // -> 3
//maxDepth('[][[]][]') // -> 2
//
//maxDepth('][') // -> -1 (cierra antes de abrir)
//maxDepth('[[[') // -> -1 (faltan cierres)
//maxDepth('[]]]') // -> -1 (sobran cierres)
//maxDepth('[][][') // -> -1 (queda uno sin cerrar)

/**
 * @param {string} s - The string to check
 * @returns {number} The maximum depth of the magic
 */
function maxDepth(s: string): number {

    if (s === '') {
        return -1
    }

  //It is closed before even open one bracket
  if (s[0] === "]") {
    return -1;
  }

  //Counter of the max of continous open brackets []
  let counter: number = 0;
  let maxDepthCounter: number = 0;
  //Stack for verifying the validity
  const stack: string[] = [];

  for (let index = 0; index < s.length; index++) {
    const element = s[index];

    if (element === "[") {
      stack.push(element);
      counter += 1;
      maxDepthCounter = Math.max(maxDepthCounter, counter);
      continue;
    }

    if (element === "]") {
     if (stack.length === 0) return -1;

      stack.pop();
      counter -= 1;
    }
  }

  if (stack.length > 0) {
    return -1;
  }

  return maxDepthCounter;
}

console.log(maxDepth("[[[]]]"));

//function maxDepth(s: string): number {
//  let depth = 0;
//  let maxDepth = 0;
//
//  for (const char of s) {
//    if (char === '[') {
//      depth++;
//      maxDepth = Math.max(maxDepth, depth);
//    } else if (char === ']') {
//      depth--;
//     
//      if (depth < 0) {
//        return -1;
//      }
//    }
//  }
//
// 
//  return depth === 0 ? maxDepth : -1;
//}