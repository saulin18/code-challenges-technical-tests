// ¡Alerta en la fábrica de juguetes de Santa! El Grinch 😈 se ha infiltrado en el almacén
//  y ha saboteado algunos de los juguetes 💣.

// Los elfos necesitan ayuda para encontrar los juguetes saboteados y eliminarlos antes de que
//  llegue la Navidad. Para ello tenemos el mapa 🗺️ del almacén, que es una matriz.

// Los * representan los juguetes saboteados y las celdas vacías con un espacio en blanco son
//  los lugares seguros.

// Tu tarea es escribir una función que devuelva la misma matriz pero, en cada posición, nos indique
//  el número de juguetes saboteados que hay en las celdas adyacentes.

// Si una celda contiene un juguete saboteado, debe permanecer igual.
//
//  Si una celda no toca ningún juguete saboteado, debe contener un espacio en blanco .

// const store = [
//   ['*', ' ', ' ', ' '],
//   [' ', ' ', '*', ' '],
//   [' ', ' ', ' ', ' '],
//   ['*', ' ', ' ', ' ']
// ]

// console.log(revealSabotage(store))
// /* Debería mostrar:
// [
//     ['*', '2', '1', '1'],
//     ['1', '2', '*', '1'],
//     ['1', '2', '1', '1'],
//     ['*', '1', ' ', ' ']
// ]
// */
// Ten en cuenta que…

// Las celdas diagonales también se consideran adyacentes.
// El tablero siempre tendrá al menos una celda vacía y un juguete saboteado *.
// El tablero puede tener cualquier tamaño.
// Los números son cadenas de texto.

function revealSabotage(store: string[][]) {
  for (let index = 0; index < store.length; index++) {
    const row = store[index];
    for (let j = 0; j < row.length; j++) {
      const cell = row[j];

      if (cell === " " || (Number(cell) >= 0 && !isNaN(Number(cell)))) {
        continue;
      }

      exploreNeighbours(index, j, store);
    }
  }

  function exploreNeighbours(
    index: number,
    j: number,
    store: string[][],
  ) {
    const directions = [
      [-1, -1],
      [-1, 0],
      [-1, 1],
      [0, -1],
      [0, 1],
      [1, -1],
      [1, 0],
      [1, 1],
    ];

    directions.forEach(([dx, dy]) => {
      const newIndex = index + dx;
      const newJ = j + dy;
      if (
        newIndex >= 0 &&
        newIndex < store.length &&
        newJ >= 0 &&
        newJ < store[newIndex].length
      ) {
        const newCell = store[newIndex][newJ];
        //Si contiene un juguete saboteado, no hacer nada
        if (newCell === "*") {
          return;
        }
        //Si contiene un espacio en blanco, sumar 1
        if (newCell === " ") {
          store[newIndex][newJ] = "1";
        }

        //Si contiene un número, sumar 1
        if (Number(newCell) >= 0 && !isNaN(Number(newCell))) {
          store[newIndex][newJ] = (Number(newCell) + 1).toString();
        }
      }
    });
  }

  return store;
}
