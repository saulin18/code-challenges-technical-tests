// Los elfos están recibiendo mensajes binarios extraños desde Marte 🪐. ¿Los extraterrestres
//  están tratando de comunicarse con ellos? 👽

// El mensaje que llega es un array de 0s y 1s. Parece que han encontrado un patrón…
// Para asegurarse, quieren encontrar el segmento más largo de la cadena donde el número de 0s y 1s sea igual.

// findBalancedSegment([1, 1, 0, 1, 1, 0, 1, 1])
// //                         |________|
// // posición del segmento:    [2, 5]
// // más largo equilibrado
// // de 0s y 1s

// findBalancedSegment([1, 1, 0])
// //                      |__|
// //                     [1, 2]

// findBalancedSegment([1, 1, 1])
// // no hay segmentos equilibrados: []
// Ten en cuenta que si hay más de un patrón equilibrado, debes devolver el más
// largo y el primero que encuentres de izquierda a derecha.

// Dicen que si encuentran el patrón, podrán enviar un mensaje de vuelta a Marte
// 🚀. Parece ser que tienen que enviarlos a https://mars.codes.

function findBalancedSegment(message: number[]) {
  const prefix: number[] = [];
  prefix[0] = 0;
  let end = 0;
  //Map to store the prefix value and the index of the first occurrence
  const prefixMap = new Map<number, number>();
  prefixMap.set(0, 0);

  //Variable to store the balanced segment
  let balancedSegment: [number, number] = [0, 0];
  //Variable to store the maximum length of the balanced segment
  let maxLength = 0;
  //Variable to store the start index of the maximum length of the balanced segment
  let maxStart: number = 0;
  //Loop through the message
  while (end < message.length) {
    //The current prefix is the sum of the last one + 1 or -1, it doesn't matters as long it's balanced
    const prefixValue = prefix[end] + (message[end] === 0 ? 1 : -1);

    //If the prefix value is already in the map, we have a balanced segment
    if (prefixMap.has(prefixValue)) {
      //The length of the balanced segment is the difference between the current
      //  index and the index of the first occurrence of the prefix value + 1
      const length = end - prefixMap.get(prefixValue)! + 1;
      //The start index of the balanced segment is the index of the first occurrence of the prefix value
      const start = prefixMap.get(prefixValue)!;
      //If the length is greater than the maximum length, we update the maximum
      // length and the balanced segment
      if (length > maxLength || (length === maxLength && start < maxStart)) {
        maxLength = length;
        maxStart = start;
        balancedSegment = [start, end];
      }
    } else {
      //If the prefix value is not in the map, we add it to the map
      prefixMap.set(prefixValue, end + 1);
    }

    //Update the prefix
    prefix[end + 1] = prefixValue;
    end++;
  }

  //If there is no balanced segment, return an empty array
  if (maxLength === 0) {
    return [];
  }

  return balancedSegment;
}
