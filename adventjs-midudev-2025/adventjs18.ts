//MEDIO
//El panel de luces navideñas 🎄✨ del taller ha sido un éxito total. Pero los elfos quieren ir un paso más allá: ahora quieren detectar si 
// hay una línea de 4 luces del mismo color también en diagonal.
//
//El panel sigue siendo una matriz donde cada celda puede ser:
//
//'.' → luz apagada
//'R' → luz roja
//'G' → luz verde
//Ahora tu función debe devolver true si existe una línea de 4 luces del mismo color encendidas y alineadas, ya sea horizontal ↔, 
// vertical ↕ o diagonal ↘↙.
//
//hasFourInARow([
//  ['R', '.', '.', '.'],
//  ['.', 'R', '.', '.'],
//  ['.', '.', 'R', '.'],
//  ['.', '.', '.', 'R']
//])
//// true → hay 4 luces rojas en diagonal ↘
//
//hasFourInARow([
//  ['.', '.', '.', 'G'],
//  ['.', '.', 'G', '.'],
//  ['.', 'G', '.', '.'],
//  ['G', '.', '.', '.']
//])
//// true → hay 4 luces verdes en diagonal ↙
//
//hasFourInARow([
//  ['R', 'R', 'R', 'R'],
//  ['G', 'G', '.', '.'],
//  ['.', '.', '.', '.'],
//  ['.', '.', '.', '.']
//])
//// true → hay 4 luces rojas en horizontal
//
//hasFourInARow([
//  ['R', 'G', 'R'],
//  ['G', 'R', 'G'],
//  ['G', 'R', 'G']
//])
//// false → no hay 4 luces del mismo color seguidas
//Nota: El tablero puede ser de cualquier tamaño.

/**
 * @param {string[][]} board
 * @returns {boolean}
 */

function hasFourInARow(board: string[][]): boolean {


    const rowNumber = board.length
    if (!board || board.length < 1 || board[0].length < 1) {
        return false
    }
    const colNumber = board[0].length

    const directions = [
        //First row is row direction, second is column direction
        [1, 0], //vertical
        [0, 1], // horizontal
        [1, 1], // diagonal down-right
        [1, -1] // diagonal down-left
    ]

    function checkDirection(startRow: number, startCol: number, dirRow: number, dirCol: number, rows: number, cols: number): boolean {
        let redCounter = 0;
        let greenCounter = 0;

        for (let step = 0; step < 4; step++) {
            const row = startRow + step * dirRow;
            const col = startCol + step * dirCol;

            // Verificar límites
            if (row < 0 || row >= rows || col < 0 || col >= cols) {
                return false;
            }

            const cell = board[row][col]

            if (cell === ".") {
                redCounter = 0
                greenCounter = 0
            }

            if (cell === "R") {
                redCounter += 1
                greenCounter = 0
            }

            if (cell === "G") {
                greenCounter += 1
                redCounter = 0
            }

            if (redCounter === 4 || greenCounter === 4) {
                return true
            }
        }
        return false
    }

    for (let row = 0; row < rowNumber; row++) {
        for (let col = 0; col < colNumber; col++) {
            for (const [rowDirection, columnDirection] of directions) {
                if (checkDirection(row, col, rowDirection, columnDirection, rowNumber, colNumber)) {
                    return true
                }
            }

        }

    }

    return false

}


