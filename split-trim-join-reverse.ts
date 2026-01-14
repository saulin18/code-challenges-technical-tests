//Es medianoche en Elm Street y necesitas dormir urgentemente. Intentas contar ovejas, pero las letras en tu mente están completamente desordenadas por culpa de Freddy.
//
//Tienes una cadena de texto caótica con letras mezcladas. Tu único escape es contar cuántas veces puedes formar la palabra "sheep" (oveja en inglés) antes de que Freddy te atrape en la pesadilla.
//
//Tu misión: Contar cuántas ovejas completas puedes formar con las letras disponibles.
//
//Crea una función countSheep(letters) que:
//
//Reciba un string con letras desordenadas
//Cuente cuántas veces se puede formar la palabra "sheep"
//Devuelva el número de ovejas completas que puedes contar
//Importante: Para formar "sheep" necesitas: s, h, e, e, p (la 'e' aparece 2 veces)
//
//countSheep('sheepxsheepy')
//// → 2 (puedes formar "sheep" dos veces)
//
//countSheep('sshhheeeepppp')
//// → 2 (s=2, h=3, e=4, p=4 → solo 2 "sheep" completas)
//
//countSheep('hola')
//// → 0 (no hay suficientes letras)
//
//countSheep('peesh')
//// → 1 (las letras están desordenadas pero están todas

interface mapOfOcurrences {
  [key: string]: number
}

function countSheep(letters: string): number {
  
  let map0fOcurrences: mapOfOcurrences = {}
  let numberOfSheeps = 0

  for (let index = 0; index < letters.length; index++) {
    const element = letters[index];

    map0fOcurrences[element] = (map0fOcurrences[element] || 0) + 1
  }

  while (
    map0fOcurrences['s'] && map0fOcurrences['s'] > 0 &&
    map0fOcurrences['h'] && map0fOcurrences['h'] > 0 &&
    map0fOcurrences['e'] && map0fOcurrences['e'] > 1 &&
    map0fOcurrences['p'] && map0fOcurrences['p'] > 0
  ) {
    numberOfSheeps += 1
    map0fOcurrences['s'] -= 1
    map0fOcurrences['h'] -= 1
    map0fOcurrences['e'] -= 2
    map0fOcurrences['p'] -= 1
  }

  return numberOfSheeps
}