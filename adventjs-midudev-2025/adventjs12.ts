//Reto #12: ⚔️ Batalla de elfos
//Dos elfos están jugando una batalla por turnos. Cada uno tiene un mazo de movimientos que se representan como un string
// donde cada carácter es una acción.
//
//A Ataque normal: causa 1 punto de daño si no es bloqueado
//B Bloqueo: bloquea un ataque normal (A)
//F Ataque fuerte: causa 2 puntos de daño, no puede ser bloqueado
//Ambos elfos comienzan con 3 puntos de vida. El primer elfo que llegue a 0 puntos de vida o menos pierde y la batalla termina
//  inmediatamente (no se siguen procesando más movimientos).
//Reglas por ronda
//Si ambos usan ataque (A o F), ambos reciben daño según el tipo.
//B bloquea A, pero no bloquea F.
//Todo se resuelve simultáneamente.
//Tu tarea
//
//Devuelve el resultado de la batalla como un número:
//
//1 → si el Elfo 1 gana
//2 → si el Elfo 2 gana
//0 → si empatan (ambos llegan a 0 a la vez o terminan con la misma vida)
//elfBattle('A', 'B')
// Ronda 1: A vs B -> Elfo 2 bloquea
// Resultado: Elfo 1 = 3 de vida
//            Elfo 2 = 3 de vida
// → 0

//elfBattle('F', 'B')
// Ronda 1: F vs B -> Elfo 2 recibe 2 de daño (F no se bloquea)
// Resultado: Elfo 1 = 3 de vida
//            Elfo 2 = 1 de vida
// → 1

//elfBattle('AAB', 'BBA')
// R1: A vs B → Elfo 2 bloquea
// R2: A vs B → Elfo 2 bloquea
// R3: B vs A → Elfo 1 bloquea
// Resultado: Elfo 1 = 3, Elfo 2 = 3
// → 0

//elfBattle('AFA', 'BBA')
// R1: A vs B → Elfo 2 bloquea
// R2: F vs B → Elfo 2 recibe 2 de daño (F no se bloquea)
// R3: A vs A → ambos -1
// Resultado: Elfo 1 = 2, Elfo 2 = 0
// → 1

//elfBattle('AFAB', 'BBAF')
// R1: A vs B → Elfo 2 bloquea
// R2: F vs B → Elfo 2 recibe 2 de daño (F no se bloquea)
// R3: A vs A → ambos -1 → Elfo 2 llega a 0 ¡Batalla termina!
// R4: no se juega, ya que Elfo 2 no tiene vida
// → 1

//elfBattle('AA', 'FF')
// R1: A vs F → Elfo 1 -2, Elfo 2 -1
// R2: A vs F → Elfo 1 -2, Elfo 2 -1 → Elfo 1 llega a -1
// → 2

/**
 * @param {string} elf1 - The moves of the first elf
 * @param {string} elf2 - The moves of the second elf
 * @return {number} - The result of the battle
 */
function elfBattle(elf1: string, elf2: string) {
  // Code here

  let elf1Health = 3;
  let elf2Health = 3;

  const rounds = Math.max(elf1.length, elf2.length);

  function performActions(move1: string, move2: string) {
    let damageToElf1 = 0;
    let damageToElf2 = 0;

    if (move1 === "A" && move2 !== "B") {
      damageToElf2 += 1;
    }
    if (move1 === "F") {
      damageToElf2 += 2;
    }

    if (move2 === "A" && move1 !== "B") {
      damageToElf1 += 1;
    }

    if (move2 === "F") {
      damageToElf1 += 2;
    }

    return [damageToElf1, damageToElf2];
  }

  for (let i = 0; i < rounds; i++) {
    const move1 = elf1[i] || "";
    const move2 = elf2[i] || "";

    const [damageToElf1, damageToElf2] = performActions(move1, move2);

    elf1Health -= damageToElf1;
    elf2Health -= damageToElf2;

    if (elf1Health === 0 && elf2Health === 0) {
        return 0
    }

    if (elf1Health <= 0) {
      return elf2Health > 0 ? 2 : 0;
    }


    if (elf2Health <=0) {
      return elf1Health > 0 ? 1 : 0;
    }
  }

  if (elf1Health === elf2Health) {
    return 0;
  }

  return elf1Health > elf2Health ? 1 : 2;
}

console.log(elfBattle("AFAB", "BBAF")); // -> 1
