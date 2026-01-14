
//Reto #23: 🎁 Ruta de regalos
//Papá Noel 🎅 tiene que repartir regalos en un pueblo representado como un mapa en cuadrícula.
//Cada celda del mapa puede ser:
//
//'S' → Punto de partida de Papá Noel
//'G' → Casa que debe recibir un regalo
//'.' → Camino libre
//'#' → Obstáculo (no se puede pasar)
//Papá Noel realiza entregas independientes para cada regalo. Sale de 'S', entrega el regalo en una casa 'G' y vuelve inmediatamente a 'S'
// para recoger el siguiente. Sin embargo, para este reto, solo queremos calcular la suma de las distancias mínimas de ida desde 'S' hasta cada casa 'G'.
//Tu tarea
//Escribe la función minStepsToDeliver(map) que devuelva el número total de pasos necesarios para llegar a todas las casas con regalos desde la posición
// inicial.
//Ten en cuenta:
//Siempre se parte de la posición inicial 'S'.
//Para cada regalo, calcula la distancia mínima desde 'S' hasta esa casa 'G'.
//No puedes atravesar obstáculos ('#').
//Si alguna casa con regalo es inalcanzable, la función debe devolver -1.
//minStepsToDeliver([
//  ['S', '.', 'G'],
//  ['.', '#', '.'],
//  ['G', '.', '.']
//])
//// Resultado: 4
//
///*
//Explicación:
//- Distancia mínima de S (0,0) a G (0,2): 2 pasos
//- Distancia mínima de S (0,0) a G (2,0): 2 pasos
//- Total: 2 + 2 = 4
//*/
//
//minStepsToDeliver([
//  ['S', '#', 'G'],
//  ['#', '#', '.'],
//  ['G', '.', '.']
//])
//// Resultado: -1
//// (La casa en (0,2) es inalcanzable por los obstáculos)
//
//minStepsToDeliver([['S', 'G']])
//// Resultado: 1
//Reglas
//El mapa siempre contiene exactamente una 'S'.
//Puede haber 0 o más casas con regalos ('G').
//No importa el orden de las entregas, ya que cada una se mide de forma independiente desde 'S'.
//Debes devolver la suma de las distancias mínimas de ida.
//Calcula la distancia más corta desde 'S' hasta cada 'G' (puedes usar un algoritmo de búsqueda en anchura o BFS).
//Si algún regalo no tiene camino posible, el resultado total es -1

/**
 * @param {string[][]} map - The town map.
 * @returns {number} - Minimum steps to deliver all gifts.
 */
function minStepsToDeliver(map: string[][]): number {


    const numRows = map.length;
    const numCols = map[0].length;
    let initialPosition: [number, number] | null = null
    let minSteps = 0
    //Total of G's
    let Gcounter = 0
    let Gfoundeds = 0


    const directions = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]
    ]

    for (let rowIndex = 0; rowIndex < numRows; rowIndex++) {
        for (let colIndex = 0; colIndex < numCols; colIndex++) {
            const colElement = map[rowIndex][colIndex]

            if (colElement === "S") {
                initialPosition = [rowIndex, colIndex]
            }

            if (colElement === "G") {
                Gcounter += 1
            }
        }
    }

    if (!initialPosition) return -1

    const visited = new Set<string>()

    const queue = [[initialPosition, 0]] satisfies [[number, number], number][]


    if (Gcounter === 0) return 0

while (queue.length > 0) {
  const [coords, currentStep] = queue.shift()!
  const [rowIndex, colIndex] = coords


  if (rowIndex < 0 || rowIndex >= numRows || colIndex < 0 || colIndex >= numCols) continue

 
  if (visited.has(`${rowIndex},${colIndex}`)) continue

  if (map[rowIndex][colIndex] === "#") continue

  visited.add(`${rowIndex},${colIndex}`)

  if (map[rowIndex][colIndex] === "G") {
    minSteps += currentStep
    Gfoundeds += 1
  }

 
  for (const direction of directions) {
    const newRow = rowIndex + direction[0]
    const newCol = colIndex + direction[1]

    if (newRow < 0 || newRow >= numRows || newCol < 0 || newCol >= numCols) continue
    if (map[newRow][newCol] === "#") continue
    if (visited.has(`${newRow},${newCol}`)) continue

   
    queue.push([[newRow, newCol], currentStep + 1])
  }
}

    return Gfoundeds === Gcounter ? minSteps : -1;

}
