//Al Polo Norte ha llegado ChatGPT y el elfo Sam Elfman está trabajando en una aplicación de administración de regalos y niños.
//
//Para mejorar la presentación, quiere crear una función drawTable que reciba un array de objetos y lo convierta en una tabla de texto.
//
//La tabla dibujada debe tener:
//
//Cabecera con letras de columna (A, B, C…).
//El contenido de la tabla son los valores de los objetos.
//Los valores deben estar alineados a la izquierda.
//Los campos dejan siempre un espacio a la izquierda.
//Los campos dejan a la derecha el espacio necesario para alinear la caja.
//La función recibe un segundo parámetro sortBy que indica el nombre del campo por el que se deben ordenar las filas. El orden será alfabético ascendente
//si los valores son strings y numérico ascendente si son números.
//
//Mira el ejemplo para ver cómo debes dibujar la tabla:
//
//drawTable(
//  [
//    { name: 'Charlie', city: 'New York' },
//    { name: 'Alice', city: 'London' },
//    { name: 'Bob', city: 'Paris' }
//  ],
//  'name'
//)
//// +---------+----------+
//// | A       | B        |
//// +---------+----------+
//// | Alice   | London   |
//// | Bob     | Paris    |
//// | Charlie | New York |
//// +---------+----------+
//
//drawTable(
//  [
//    { gift: 'Book', quantity: 5 },
//    { gift: 'Music CD', quantity: 1 },
//    { gift: 'Doll', quantity: 10 }
//  ],
//  'quantity'
//)
// +----------+----+
// | A        | B  |
// +----------+----+
// | Music CD | 1  |
// | Book     | 5  |
// | Doll     | 10 |
// +----------+----+

/**
 * @param {Array<Object>} data - The data to draw the table
 * @param {string} sortBy - The field to sort the table
 * @returns {string}
 */

type Data = Array<Record<string, string | number>>
type SortBy = string
function drawTable(data: Data, sortBy: SortBy): string {
  const allColumns = Object.keys(data[0]);
  const columns = [...allColumns];

  const sortedData = data.slice().sort((a, b) => {
    const valA = a[sortBy];
    const valB = b[sortBy];

    if (typeof valA === "number" && typeof valB === "number") {
      return valA - valB;
    }

    return String(valA).localeCompare(String(valB));
  });

  const rows = [];

  // We need to calculate the max length of the values and that will be the length of the rows and the header row
  const lengthOfRow = () => {
    const dictWithLengths = columns.reduce((acc, column) => {
      const maxLengthInColumn = Math.max(
        1,
        ...sortedData.map((row) => String(row[column]).length)
      );
      acc[column] = maxLengthInColumn + 2;
      return acc;
    }, {} as Record<string, number>);
    return dictWithLengths;
  };

  const createHeader = (columns: string[], lengths: ReturnType<typeof lengthOfRow>) => {
    let header = "|";
    columns.forEach((column, index) => {
      const headerLetter = String.fromCharCode(65 + index);
      const length = lengths[column];
      header += " " + headerLetter + " ".repeat(length - 2) + "|";
    });
    return header + "\n";
  };

  const lengths = lengthOfRow();

  // Create top line
  let table = "";
  let topLine = "+";
  columns.forEach((column) => {
    const length = lengths[column];
    topLine += "-".repeat(length) + "+";
  });
  table += topLine + "\n";
  // Create header
  table += createHeader(columns, lengths);
  // Create separator line
  table += topLine + "\n";
  // Create rows
  sortedData.forEach((row) => {
    let rowString = "|";
    columns.forEach((column, index) => {
      const length = lengths[column];
      const value = String(row[column]);
      rowString += " " + value + " ".repeat(length - value.length - 1) + "|";
    });
    table += rowString + "\n";
  });

  return table + topLine;
}

