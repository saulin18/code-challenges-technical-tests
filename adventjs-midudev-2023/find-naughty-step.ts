// En el taller de Santa, un elfo travieso ha estado jugando en la cadena de 
// fabricación de regalos, añadiendo o eliminando un paso no planificado.

// Tienes la secuencia original de pasos en la fabricación original y la secuencia 
// modificada modified que puede incluir un paso extra o faltar un paso.

// Tu tarea es escribir una función que identifique y devuelva el primer paso extra 
// que se ha añadido o eliminado en la cadena de fabricación. Si no hay ninguna diferencia 
// entre las secuencias, devuelve una cadena vacía.

// const original = 'abcd'
// const modified = 'abcde'
// findNaughtyStep(original, modified) // 'e'

// const original = 'stepfor'
// const modified = 'stepor'
// findNaughtyStep(original, modified) // 'f'

// const original = 'abcde'
// const modified = 'abcde'
// findNaughtyStep(original, modified) // ''
// A tener en cuenta:

// Siempre habrá un paso de diferencia o ninguno.
// La modificación puede ocurrir en cualquier lugar de la cadena.
// La secuencia original puede estar vacía


function findNaughtyStep(original: string, modified: string): string {
  
  let left: number = 0
  let right: number = Math.max(original.length, modified.length)

  let res: string = ""
  while (left <= right){
    let firstChar = original[left] ?? ""
    let secondChar = modified[left] ?? ""

    if(firstChar === "" && firstChar != secondChar){
      res += secondChar
      return res
    }

    if(firstChar != "" && firstChar != secondChar){
      original.length > modified.length ? res += firstChar :   res += secondChar
      return res
    }
    left +=1
  }
  return res
}