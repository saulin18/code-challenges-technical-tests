
//Reto #14: 🗃️ Encuentra el camino al regalo
//En el Polo Norte, los elfos han simplificado su sistema de almacenamiento para evitar errores.
//Ahora guardan los regalos en un objeto mágico con profundidad limitada, donde cada valor aparece una sola vez.
//Santa necesita una forma rápida de saber qué camino de claves debe seguir para encontrar un regalo concreto.
//Tu tarea es escribir una función que, dado un objeto y un valor, devuelva el array de claves que hay que recorrer para llegar a ese valor.
//Reglas:
//El objeto tiene como máximo 3 niveles de profundidad.
//El valor a buscar aparece como mucho una vez.
//El objeto solo contiene otros objetos y valores primitivos (strings, numbers, booleans).
//Si el valor no existe, devuelve un array vacío.
//Ejemplos:
//
//const workshop = {
//  storage: {
//    shelf: {
//      box1: 'train',
//      box2: 'switch'
//    },
//    box: 'car'
//  },
//  gift: 'doll'
//}
//
//findGiftPath(workshop, 'train')
// ➜ ['storage', 'shelf', 'box1']



type Gift = string | number | boolean
type Workshop = Record<string, any>
type Path = string[]

/**
 * @param {object} workshop - A representation of the workshop
 * @param {string|number|boolean} gift - The gift to find
 * @returns {number[]} The path to the gift
 */
function findGiftPath(workshop: Workshop, gift: Gift): Path {

  const result = recurse(workshop, gift, []);
  return result ? result : [];

  function recurse(obj: Workshop, target: Gift, currentPath: Path): Path | null {

    for (const key in obj) {
      const value = obj[key];

      if (value === target) {
        return [...currentPath, key];
      }

      if (typeof value === "object") {
        const recursedPath = recurse(value, target, [...currentPath, key]);
        if (recursedPath) {
          return recursedPath;
        }
      }
    }

    return null;
  }
}
