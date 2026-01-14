//¡El almacén vertical de Santa se ha modernizado! Ahora, además de apilar los regalos, hay un robot 🤖 en el almacen que recoje
// los regalos si hay una fila completa.
//
//El almacén es una matriz con # regalos y . espacios vacíos. Debes crear una función clearGifts que reciba el estado del almacén y un array
// con las columnas donde se dejan caer los regalos.
//
//Reglas de la caída:
//
//El regalo cae por la columna indicada desde arriba.
//Se coloca en la celda vacía (.) más baja de esa columna.
//Si la columna está llena, el regalo se ignora.
//Regla del robot de limpieza:
//
//Si al colocar un regalo, una fila se completa totalmente con regalos (#), esa fila desaparece.
//Todas las filas que estaban por encima de la fila eliminada bajan una posición.
//Al eliminarse una fila, aparece una nueva fila vacía (.) en la parte superior para mantener el tamaño del almacén.
//clearGifts(
//  [
//    ['.', '.', '.'],
//    ['.', '.', '.'],
//    ['#', '.', '#']
//  ],
//  [1]
//)
///*
//1. El regalo cae en la columna 1
//2. La fila 2 se convierte en [# # #].
//3. La fila 2 está completa, el robot la limpia.
//6. Se añade una nueva fila vacía en la posición 0.
//
//Resultado:
//[
//  ['.', '.', '.'],
//  ['.', '.', '.'],
//  ['.', '.', '.']
//]
//*/
//
//clearGifts(
//  [
//    ['.', '.', '#'],
//    ['#', '.', '#'],
//    ['#', '.', '#']
//  ],
//  [0, 1, 2]
//)
//
///*
//1. El regalo cae en la columna 0
//2. El regalo cae en la columna 1
//3. La fila 2 se convierte en [# # #]
//4. La fila 2 está completa, el robot la limpia
//
//Por ahora queda así:
//[
//  ['.', '.', '.']
//  ['#', '.', '#'],
//  ['#', '.', '#'],
//]
//
//5. El regalo cae en la columna 2
//
//Resultado:
//[
//  ['.', '.', '#'],
//  ['#', '.', '#'],
//  ['#', '.', '#']
//]
//*/

/**
 * @param {string[][]} warehouse
 * @param {number[]} drops
 * @returns {string[][]}
 */
//type Gift = '#'
//type EmptySlot = '.'
//type WarehouseCell = Gift | EmptySlot
type Gift = "#";
type EmptySlot = ".";
type WarehouseCell = Gift | EmptySlot;


export default function clearGifts(warehouse: WarehouseCell[][], drops: number[]): WarehouseCell[][] {
        const GIFT: Gift = '#'
        const EMPTY_SLOT: EmptySlot = '.'

        const newWarehouse: WarehouseCell[][] = Array.from(warehouse, (row) => [...row])

        for (const drop of drops) {
                let level = 0
                while (level < newWarehouse.length && newWarehouse[level][drop] === EMPTY_SLOT) level++

                level--
                if (level > -1 && level < newWarehouse.length) {
                        newWarehouse[level][drop] = GIFT

                        if (newWarehouse[level].every((cell) => cell === GIFT)) {
                                newWarehouse.unshift(Array.from({ length: newWarehouse[level].length }, () => EMPTY_SLOT))
                                newWarehouse.splice(level + 1, 1)
                        }
                }
        }

        return newWarehouse
}
console.log(
  clearGifts(
    [
      [".", ".", "#"],
      ["#", ".", "#"],
      ["#", ".", "#"],
    ],
    [0, 1, 2]
  )
);
