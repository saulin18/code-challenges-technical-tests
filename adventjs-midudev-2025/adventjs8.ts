//Santa 🎅 quiere saber cuál es la primera letra no repetida en el nombre de un juguete 🎁.
//
//Escribe una función que reciba un string y devuelva la primera letra que no se repite, ignorando mayúsculas y minúsculas al contar, pero devolviendo la letra tal como aparece en el string.
//
//Si no hay ninguna, devuelve una cadena vacía ("").
//
//Ejemplos:
//
//findUniqueToy('Gift') // 'G'
//// ℹ️ La G es la primera letra que no se repite
//// y la devolvemos tal y como aparece
//
//findUniqueToy('sS') // ''
//// ℹ️ Las letras se repiten, ya que no diferencia mayúsculas
//
//findUniqueToy('reindeeR') // 'i'
//// ℹ️ La r se repite (aunque sea en mayúscula)
//// y la e también, así que la primera es la 'i'
//
//// Más casos:
//findUniqueToy('AaBbCc') // ''
//findUniqueToy('abcDEF') // 'a'
//findUniqueToy('aAaAaAF') // 'F'
//findUniqueToy('sTreSS') // 'T'
//findUniqueToy('z') // 'z'

/**
 * @param {string} toy - The toy to find the first unique one letter
 * @returns {string} The first unique letter in the toy
 */
function findUniqueToy(toy: string) {
  const map: Record<string, number> = {};

  for (const char of toy.split('')) {
    const normalizedChar = char.toLowerCase()
    if (map[normalizedChar] >= 0) map[normalizedChar] += 1;
    else map[normalizedChar] = 0;
  }

  for (const char of toy) {
    const normalized = char.toLowerCase()

    if (map[normalized] === 0) {
      return char
    }
    continue
  }
  return ''
}

