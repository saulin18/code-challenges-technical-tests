
//Reto #17: 🎄 El panel de luces navideñas
//En el Polo Norte han montado un panel de luces navideñas 🎄✨ para decorar el taller. Cada luz puede estar encendida con un color o apagada.
//
//El panel se representa como una matriz donde cada celda puede ser:
//
//'.' → luz apagada
//'R' → luz roja
//'G' → luz verde
//Los elfos quieren saber si en el panel existe una línea de 4 luces del mismo color encendidas y alineadas (solo horizontal ↔ o vertical ↕). Las luces 
//apagadas ('.') no cuentan.
//hasFourLights([
//  ['.', '.', '.', '.', '.'],
//  ['R', 'R', 'R', 'R', '.'],
//  ['G', 'G', '.', '.', '.']
//])
//// true → hay 4 luces rojas en horizontal
//
//hasFourLights([
//  ['.', 'G', '.', '.'],
//  ['.', 'G', '.', '.'],
//  ['.', 'G', '.', '.'],
//  ['.', 'G', '.', '.']
//])
//// true → hay 4 luces verdes en vertical
//
//hasFourLights([
//  ['R', 'G', 'R'],
//  ['G', 'R', 'G'],
//  ['G', 'R', 'G']
//])
//// false → no hay 4 luces del mismo color seguidas
//Nota: El tablero puede ser de cualquier tamaño. No hay diagonales.

/**
 * @param {string[][]} board
 * @returns {boolean}
 */
function hasFourLights(board: string[][]): boolean {

    const rowNumber = board.length
    if (!board || board.length < 1 || board[0].length < 1) {
        return false
    }
    const colNumber = board[0].length
    function checkRows(rowNumber: number, board: string[][], rowTotal: number): boolean {

        let redCounter = 0
        let greenCounter = 0

        for (let index = 0; index < rowTotal; index++) {
            const cell = board[rowNumber][index];


            if (redCounter === 4 || greenCounter === 4) {
                return true
            }

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
        }
        return false
    }
    function checkColumns(colNumber: number, board: string[][], colTotal: number): boolean {


        let redCounter = 0
        let greenCounter = 0

        for (let index = 0; index < colTotal; index++) {
            const cell = board[index][colNumber];
            if (redCounter === 4 || greenCounter === 4) {
                return true
            }

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
        }
        return false
    }

    for (let rowCount = 0; rowCount < rowNumber; rowCount++) {
        const rowRes = checkRows(rowCount, board, rowNumber)

        if (rowRes) {
            return true
        }
    }

    for (let colCount = 0; colCount < colNumber; colCount++) {
        const colRes = checkColumns(colCount, board, colNumber)

        if (colRes) {
            return true
        }

    }
    return false
}