
type Factory = string[]
type Result = 'completed' | 'broken' | 'loop'

function runFactory(factory: Factory): Result {

  const numRows = factory.length;
  const numCols = factory[0].length;


  const currentPosition = { row: 0, col: 0 };
  const visited = new Set<string>();

  const isOutOfBounds = (i: number, j: number, numRows: number, numCols: number): boolean => {
    if (i < 0 || i >= numRows || j < 0 || j >= numCols) return true;
    return false;
  };

  while (true) {
    const posKey = `${currentPosition.row},${currentPosition.col}`;
    if (visited.has(posKey)) return "loop";
    visited.add(posKey);

    const cell = factory[currentPosition.row][currentPosition.col];

    if (cell === ".") return "completed";

    switch (cell) {
      case ">":
        currentPosition.col += 1;
        break;
      case "<":
        currentPosition.col -= 1;
        break;
      case "^":
        currentPosition.row -= 1;
        break;
      case "v":
        currentPosition.row += 1;
        break;
    }

    const isOut = isOutOfBounds(
      currentPosition.row,
      currentPosition.col,
      numRows,
      numCols
    );
    if (isOut) return "broken";
  }
}


///type Factory = string[]
///type Result = 'completed' | 'broken' | 'loop'
///
///function runFactory(factory: Factory): Result {
///  const numRows = factory.length;
///  const numCols = factory[0].length;
///
///  // For duplicates
///  const visited = new Set<string>();
///
///  const isOutOfBounds = (i: number, j: number, numRows: number, numCols: number) => {
///    if (i < 0 || i >= numRows || j < 0 || j >= numCols) return true;
///
///    return false;
///  };
///
///  function solve(visited: Set<string>, cell: string, currentPosition: { row: number, col: number }, numRows: number, numCols: number) {
///    const posKey = `${currentPosition.row},${currentPosition.col}`;
///    if (visited.has(posKey)) return "loop";
///    visited.add(posKey);
///
///    if (cell === ".") return "completed";
///
///    switch (cell) {
///      case ">":
///        currentPosition.col += 1;
///        break;
///      case "<":
///        currentPosition.col -= 1;
///        break;
///      case "^":
///        currentPosition.row -= 1;
///        break;
///      case "v":
///        currentPosition.row += 1;
///        break;
///    }
///
///    const isOut = isOutOfBounds(
///      currentPosition.row,
///      currentPosition.col,
///      numRows,
///      numCols
///    );
///    if (isOut) return "broken";
///  }
///
///  if (numRows === 1) {
///    for (let index = 0; index < numCols; index++) {
///      const element = factory[0][index];
///
///      const result = solve(
///        visited,
///        element,
///        { row: 0, col: index },
///        numRows,
///        numCols
///      );
///
///      if (result) return result;
///    }
///  }
///
///  const currentPosition = { row: 0, col: 0 };
///  for (let rowIndex = 0; rowIndex < numRows; rowIndex++) {
///    for (let colIndex = 0; colIndex < numCols; colIndex++) {
///      const cell = factory[currentPosition.row][currentPosition.col];
///
///      const result = solve(visited, cell, currentPosition, numRows, numCols);
///
///      if (result) return result;
///    }
///  }
///
///  return "broken";
///}

//console.log(runFactory(["v.", "^."]));

