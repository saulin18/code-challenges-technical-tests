//FÁCIL
//¡Es hora de decorar el árbol de Navidad 🎄! Escribe una función que reciba:
//
//height → la altura del árbol (número de filas).
//ornament → el carácter del adorno (por ejemplo, "o" o "@").
//frequency → cada cuántas posiciones de asterisco aparece el adorno.
//El árbol se dibuja con asteriscos *, pero cada frequency posiciones, el asterisco se reemplaza por el adorno.
//
//El conteo de posiciones empieza en 1, desde la copa hasta la base, de izquierda a derecha. Si frequency es 2,
// los adornos aparecen en las posiciones 2, 4, 6, etc.
//
//El árbol debe estar centrado y tener un tronco # de una línea al final.
//
//🧩 Ejemplos
//drawTree(5, 'o', 2)
////     *
////    o*o
////   *o*o*
////  o*o*o*o
//// *o*o*o*o*
////     #
//
//drawTree(3, '@', 3)
////   *
////  *@*
//// *@**@
////   #
//
//drawTree(4, '+', 1)
//    +
//   +++
//  +++++
// +++++++
//    #
/** @param {number} height - Height of the tree
 *  @param {string} ornament - Character to use as ornament
 *  @param {number} frequency - How often ornaments appear
 *  @returns {string} The decorated tree
 */
function drawTree(height: number, ornament: string, frequency: number) {
  const res: string[] = [];

  let counter = 1;
  const maxHeight = height * 2 - 1;
  for (let index = 0; index < height; index++) {
    const lengthOfLevel = index * 2 + 1;
    const level = [];

    for (let j = 0; j < lengthOfLevel; j++) {
      if (counter % frequency === 0) {
        level.push(ornament);
        counter += 1;
        continue;
      }
      level.push("*");
      counter += 1;
    }

    const spaces = (maxHeight - lengthOfLevel) / 2;
    const row = " ".repeat(spaces) + level.join("");
    res.push(row);
  }

  const spacesEnd = (maxHeight - 1) / 2;
  res.push(" ".repeat(spacesEnd) + "#");

  return res.join("\n");
}

console.log(drawTree(5, "o", 2));
