//DIFÍCIL
//Los elfos han construido un reno 🦌 robot aspirador (@) para limpiar un poco el taller de cara a las navidades.
//
//El reno se mueve sobre un tablero para recoger cosas del suelo (*) y debe evitar obstáculos (#).
//
//Recibirás dos parámetros:
//
//board: un string que representa el tablero.
//moves: un string con los movimientos: 'L' (izquierda), 'R' (derecha), 'U' (arriba), 'D' (abajo).
//Reglas del movimiento:
//
//Si el reno se sale del tablero o choca contra un obstáculo (#) → devuelve 'crash'.
//Si el reno recoge algo del suelo (*) durante los movimientos → devuelve 'success'.
//Si el reno no recoge nada ni se estrella → devuelve 'fail'.
//Importante: Ten en cuenta que en el board la primera y última línea están en blanco y deben descartarse.
//
//Ejemplo:
//
//const board = `
//.....
//.*#.*
//.@...
//.....
//`
//
//moveReno(board, 'D')
//// ➞ 'fail' -> se mueve pero no recoge nada
//
//moveReno(board, 'U')
//// ➞ 'success' -> recoge algo (*) justo encima
//
//moveReno(board, 'RU')
//// ➞ 'crash' -> choca contra un obstáculo (#)
//
//moveReno(board, 'RRRUU')
//// ➞ 'success' -> recoge algo (*)
//
//moveReno(board, 'DD')
//// ➞ 'crash' -> se choca con la parte de abajo del tablero
//
//moveReno(board, 'UUU')
//// ➞ 'success' -> recoge algo del suelo (*) y luego se choca por arriba
//
//moveReno(board, 'RR')
// ➞ 'fail' -> se mueve pero no recoge nada
//
type Board = string
type Moves = string
type Result = 'fail' | 'crash' | 'success'
/**
 * @param {string} board - Represent the board situation
 * @param {string} moves - Movement direction
 * @returns {'fail' | 'crash' | 'success'}
 */
function moveReno(board: Board, moves: Moves): Result {
  if (board.trim() === "") {
    return "fail";
  }

  const lines: string[] = board.split("\n");

  // We dont need the last
  lines.pop();
  //We dont need the first
  lines.shift();

  //Transform to a matrix
  const transformations = (col: number, row: number, currentTransformation: Moves) => {
    switch (currentTransformation) {
      case "R":
        col += 1;
        break;
      case "L":
        col -= 1;
        break;
      case "U":
        row -= 1;
        break;
      case "D":
        row += 1;
        break;
    }
    return { col, row };
  };

  const matrix = lines.map((line) => line.split(""));

  let renoRow = 0, renoCol = 0;
  for (let row = 0; row < matrix.length; row++) {
    for (let col = 0; col < matrix[row].length; col++) {
      if (matrix[row][col] === "@") {
        renoRow = row;
        renoCol = col;
        break;
      }
    }
  }

  const positionOfTheReno =
    renoRow !== undefined && renoCol !== undefined
      ? { row: renoRow, col: renoCol }
      : null;

  if (!positionOfTheReno) {
    return "fail";
  }

  for (let i = 0; i < moves.length; i++) {
    const move = moves[i];

    let newRow = renoRow;
    let newCol = renoCol;

    const { row, col } = transformations(renoCol, renoRow, move);

    newRow = row;
    newCol = col;

    if (newRow < 0 || newRow >= matrix.length ||
      newCol < 0 || newCol >= matrix[0].length) {
      return 'crash';
    }


    if (matrix[newRow][newCol] === '#') {
      return 'crash';
    }

    if (matrix[newRow][newCol] === '*') {
      return 'success';
    }

    renoRow = newRow;
    renoCol = newCol;
  }

  return 'fail';

}

const board = `
.....
.*#.*
.@...
.....
`;
moveReno(board, "D");
