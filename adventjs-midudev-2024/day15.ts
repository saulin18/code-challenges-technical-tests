// ✏️ Drawing tables
// ChatGPT has arrived at the North Pole and the elf Sam Elfman is working on an application for managing gifts and
// children.
// 
// To enhance the presentation, he wants to create a function drawTable that receives an array of objects and 
// converts it into a text table.
// 
// The drawn table should represent the object data as follows:
// 
// It has a header with the column name.
// The column name has the first letter capitalized.
// Each row should contain the values of the objects in the corresponding order.
// Each value must be left-aligned.
// Fields always leave a space on the left.
// Fields leave the necessary space on the right to align the box.
// Look at the example to see how you should draw the table:
// 
// drawTable([
//   { name: "Alice", city: "London" },
//   { name: "Bob", city: "Paris" },
//   { name: "Charlie", city: "New York" },
// ]);
// // +---------+-----------+
// // | Name    | City      |
// // +---------+-----------+
// // | Alice   | London    |
// // | Bob     | Paris     |
// // | Charlie | New York  |
// // +---------+-----------+
// 
// drawTable([
//   { gift: "Doll", quantity: 10 },
//   { gift: "Book", quantity: 5 },
//   { gift: "Music CD", quantity: 1 },
// ]);
// // +----------+----------+
// // | Gift     | Quantity |
// // +----------+----------+
// // | Doll     | 10       |
// // | Book     | 5        |
// // | Music CD | 1        |

/**
 * @param {Array<Object>} data - The data to draw the table
 * @param {string} sortBy - The field to sort the table
 * @returns {string}
 */

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
