//DIFÍCIL
//Papá Noel 🎅 está probando un nuevo simulador de trineo dentro de un laberinto en el taller. El laberinto se representa como
//  una matriz de caracteres.
//
//Tu tarea es implementar una función que determine si es posible llegar a la salida (E) partiendo desde la posición
// inicial (S).
//
//Reglas del laberinto:
//
//S: Posición inicial de Santa.
//E: Salida del laberinto.
//.: Camino libre.
//#: Pared (bloquea el paso).
//Movimientos permitidos: arriba, abajo, izquierda y derecha.
//Solo hay una S y una sola E.
//canEscape([
//  ['S', '.', '#', '.'],
//  ['#', '.', '#', '.'],
//  ['.', '.', '.', '.'],
//  ['#', '#', '#', 'E']
//])
//// → true
//
//canEscape([
//  ['S', '#', '#'],
//  ['.', '#', '.'],
//  ['.', '#', 'E']
//])
//// → false
//
//canEscape([['S', 'E']])
//// → true
//
//canEscape([
//  ['S', '.', '.', '.', '.'],
//  ['#', '#', '#', '#', '.'],
//  ['.', '.', '.', '.', '.'],
//  ['.', '#', '#', '#', '#'],
//  ['.', '.', '.', '.', 'E']
//])
//// → true
//
//canEscape([
//  ['S', '.', '.'],
//  ['.', '.', '.'],
//  ['#', '#', '#'],
//  ['.', '.', 'E']
//])
//// → false
//A tener en cuenta:
//
//No necesitas devolver el camino, solo si es posible llegar.
//Santa no puede salir de los límites del laberinto.
//Consejo: Este problema se puede resolver de varias formas, pero algoritmos de búsqueda como BFS (búsqueda en anchura)
//o DFS (búsqueda en profundidad) son ideales para este tipo de retos.

//function canEscape(maze: string[][]): boolean {
//
//    const numRows = maze.length;
//    const numCols = maze[0].length;
//    let initialPosition: [number, number] | null = null
//
//    const directions = [
//        [1, 0],
//        [0, 1],
//        [-1, 0],
//        [0, -1]
//    ]
//
//    for (let rowIndex = 0; rowIndex < numRows; rowIndex++) {
//        for (let colIndex = 0; colIndex < numCols; colIndex++) {
//            const colElement = maze[rowIndex][colIndex]
//
//            if (colElement === "S") {
//                initialPosition = [rowIndex, colIndex]
//            }
//        }
//    }
//
//    if (!initialPosition) return false
//
//    function recurse(position: [number, number], visited: Set<[number, number]>) {
//        if (visited.has(position)) return false
//
//        const [rowIndex, colIndex] = position
//
//        const isNotValidPosition = rowIndex < 0 || rowIndex >= numRows || colIndex < 0 || colIndex >= numCols
//
//        if (isNotValidPosition) return false
//
//        if (maze[rowIndex][colIndex] === "E") return true;
//
//        if (maze[rowIndex][colIndex] === "#") return false;
//
//        visited.add(position)
//
//        for (const direction of directions) {
//
//            const newRow = rowIndex + direction[0]
//            const newCol = colIndex + direction[1]
//            const newPosition: [number, number] = [newRow, newCol]
//
//            const isNotValidPositionNewPosition = newRow < 0 || newRow >= numRows || newCol < 0 || newCol >= numCols
//
//            if (isNotValidPositionNewPosition) continue
//
//            if (maze[newRow][newCol] === "E") return true
//
//            if (maze[rowIndex][colIndex] === "#") continue;
//
//            const foundExit = recurse(newPosition, visited)
//            if (foundExit) return true
//        }
//
//        return false
//    }
//
//    return recurse(initialPosition, new Set())
//}

//RangeError: Maximum call stack size exceeded

function canEscape(maze: string[][]): boolean {

    const numRows = maze.length;
    const numCols = maze[0].length;
    let initialPosition: [number, number] | null = null

    const directions = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]
    ]

    for (let rowIndex = 0; rowIndex < numRows; rowIndex++) {
        for (let colIndex = 0; colIndex < numCols; colIndex++) {
            const colElement = maze[rowIndex][colIndex]

            if (colElement === "S") {
                initialPosition = [rowIndex, colIndex]
            }
        }
    }


    if (!initialPosition) return false

    const visited = new Set<string>()

    const queue = [initialPosition]

    while (
        queue.length > 0
    ) {

        const position = queue.shift()

        if (!position) return false

        const [rowIndex, colIndex] = position

        if (visited.has(`${rowIndex},${colIndex}`)) continue

        const isNotValidPosition = rowIndex < 0 || rowIndex >= numRows || colIndex < 0 || colIndex >= numCols

        if (isNotValidPosition) continue

        if (maze[rowIndex][colIndex] === "E") return true;

        if (maze[rowIndex][colIndex] === "#") continue;

        visited.add(`${rowIndex},${colIndex}`)

        for (const direction of directions) {

            const newRow = rowIndex + direction[0]
            const newCol = colIndex + direction[1]
            const newPosition: [number, number] = [newRow, newCol]

            const isNotValidPositionNewPosition = newRow < 0 || newRow >= numRows || newCol < 0 || newCol >= numCols

            if (isNotValidPositionNewPosition) continue

            if (maze[newRow][newCol] === "E") return true

            if (maze[newRow][newCol] === "#") continue;

            if (visited.has(`${newRow},${newCol}`)) continue

            queue.push(newPosition)
        }
    }

    return false
}