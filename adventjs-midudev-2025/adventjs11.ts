//FÁCIL
//El grinch quiere robar los regalos de Navidad del almacén. Para ello necesita saber qué regalos no tienen vigilancia.
//
//El almacén se representa como un array de strings (string[]), donde cada regalo (*) está protegido si su posición está junto
//  a una cámara (#). Cada espacio vacío se representa con un punto (.).
//
//Tu tarea es contar cuántos regalos están sin vigilancia, es decir, que no tienen ninguna cámara adyacente (arriba, abajo, izquierda o derecha).
//
//Ten en cuenta: solo se considera como "adyacente" las 4 direcciones cardinales, no en diagonal.
//
//Los regalos en las esquinas o bordes pueden estar sin vigilancia, siempre que no tengan cámaras directamente al lado.
//
//findUnsafeGifts([
//  '.*.',
//  '*#*',
//  '.*.'
//]) // ➞ 0
//
//// Todos los regalos están junto a una cámara
//
//findUnsafeGifts([
//  '...',
//  '.*.',
//  '...'
//]) // ➞ 1
//
//// Este regalo no tiene cámaras alrededor
//
//findUnsafeGifts([
//  '*.*',
//  '...',
//  '*#*'
//]) // ➞ 2
//// Los regalos en las esquinas superiores no tienen cámaras alrededor
//
//findUnsafeGifts([
//  '.....',
//  '.*.*.',
//  '..#..',
//  '.*.*.',
//  '.....'
//]) // ➞ 4

// Los cuatro regalos no tienen cámaras, porque están en diagonal a la cámara

/**
 * @param {string[]} warehouse - The warehouse layout
 * @returns {number} The count of unwatched gifts
 */
function findUnsafeGifts(warehouse: string[]): number {


  let count = 0;

  const matrix = warehouse.map(row => row.split(''));
  console.log(matrix);

  const rows = matrix.length;
  const cols = matrix[0].length;

  for (let rowIndex = 0; rowIndex < rows; rowIndex++) {
    for (let colIndex = 0; colIndex < cols; colIndex++) {
      const cell = matrix[rowIndex][colIndex];

      if (cell === "*") {
       
        const haveCameraUp = rowIndex > 0 && matrix[rowIndex - 1][colIndex] === "#"
        const haveCameraDown = rowIndex < rows - 1 && matrix[rowIndex + 1][colIndex] === "#"
        const haveCameraLeft = colIndex > 0 && matrix[rowIndex][colIndex - 1] === "#"
        const haveCameraRight = colIndex < cols - 1 && matrix[rowIndex][colIndex + 1] === "#"

        if (!haveCameraUp && !haveCameraDown && !haveCameraLeft && !haveCameraRight) {
          count++;
        }
      }
    }
  }

  return count
}

console.log(findUnsafeGifts([
  '.....',
  '.*.*.',
  '..#..',
  '.*.*.',
  '.....'
]))