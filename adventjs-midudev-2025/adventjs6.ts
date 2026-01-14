//FÁCIL
//En el taller de Santa, los elfos han encontrado una montaña de guantes mágicos totalmente desordenados. Cada guante viene descrito por dos valores:
//
//hand: indica si es un guante izquierdo (L) o derecho (R)
//color: el color del guante (string)
//Tu tarea es ayudarles a emparejar guantes: Un par válido es un guante izquierdo y uno derecho del mismo color.
//
//Debes devolver una lista con los colores de todos los pares encontrados. Ten en cuenta que puede haber varios pares del mismo color.
//
//🧩 Ejemplos
//const gloves = [
//  { hand: 'L', color: 'red' },
//  { hand: 'R', color: 'red' },
//  { hand: 'R', color: 'green' },
//  { hand: 'L', color: 'blue' },
//  { hand: 'L', color: 'green' }
//]
//
//matchGloves(gloves)
//// ["red", "green"]
//
//const gloves2 = [
//  { hand: 'L', color: 'gold' },
//  { hand: 'R', color: 'gold' },
//  { hand: 'L', color: 'gold' },
//  { hand: 'L', color: 'gold' },
//  { hand: 'R', color: 'gold' }
//]
//
//matchGloves(gloves2)
//// ["gold", "gold"]
//
//const gloves3 = [
//  { hand: 'L', color: 'red' },
//  { hand: 'R', color: 'green' },
//  { hand: 'L', color: 'blue' }
//]
//
//matchGloves(gloves3)
//// []

type Glove = { hand: 'L' | 'R'; color: string }

/**
 * @param {{ hand: 'L' | 'R', color: string }[]} gloves
 * @returns {string[]} Colors of matched pairs
 */
function matchGloves(gloves: Glove[] ) {
  const result: string[] = [];

  const groups = Object.groupBy(gloves, (glove) => glove.color);

  for (const [color, group] of Object.entries(groups)) {
    const leftHands = group?.filter((glove) => glove.hand === "L");
    const rightHands = group?.filter((glove) => glove.hand === "R");
    const pairs = Math.min(leftHands?.length ?? 0, rightHands?.length ?? 0);

    for (let index = 0; index < pairs; index++) {
      result.push(color);
    }
  }

  return result;
}

const gloves = [
  { hand: "L", color: "red" },
  { hand: "R", color: "red" },
  { hand: "R", color: "green" },
  { hand: "L", color: "blue" },
  { hand: "L", color: "green" },
] satisfies Glove[]; 

matchGloves(gloves);
