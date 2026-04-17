// En la fábrica de juguetes de Santa, los elfos están desarrollando un
// lenguaje de programación llamado Santa.js 👨‍💻👩‍💻 basado en símbolos
// para controlar sus máquinas de juguetes 🚂.

// Han creado un sistema de instrucciones simple y necesitan tu ayuda
// para construir un compilador que interprete estos símbolos.

// El compilador trabaja con un contador que inicialmente tiene un valor
// de 0. Las instrucciones modificarán el valor de este contador.

// Instrucciones del lenguaje de los elfos en base a símbolos:

// +: Incrementa en 1 el valor del contador.
// *: Multiplica por 2 el valor del contador.
// -: Resta 1 al valor del contador.
// %: Marca un punto de retorno. No modifica el contador.
// <: Vuelve atrás una vez a la última instrucción con el símbolo % que haya visto.
// Si no hay un % previo, no hace nada.
// ¿: Inicia un bloque condicional que se ejecuta si el contador es mayor a 0.
// ?: Finaliza un bloque condicional.
// Crea una función compile que reciba un string con las instrucciones del lenguaje y devuelve el resultado
// de ejecutarlas. Aquí tienes algunos ejemplos:

// compile('++*-') // 3
// // (1 + 1) * 2 - 1 = 3

// compile('++%++<') // 6
// // 1 + 1 + 1 + 1 + 1 + 1 = 6

// compile('++<--') // 0
// // 1 + 1 - 1 - 1 = 0

// compile('++¿+?') // 3
// // 1 + 1 + 1 = 3

// compile('--¿+++?') // -2
// // - 1 - 1 = -2

function compile(code: string): number {
  let counter: number = 0;
  /** Return addresses from `%`, scoped to ¿…? nesting (`depth` matches `blockStack.length` at push time). */
  const stack: { pc: number; depth: number }[] = [];
  /** Un nivel por cada `¿…?` que estamos ejecutando (counter > 0 al abrir). La profundidad es `length`. */
  const blockStack: true[] = [];

  let index = 0;
  while (index < code.length) {
    const element = code[index];
    let resultOfAction: unknown | number = undefined;

    switch (element) {
      case "+":
        counter += 1;
        break;
      case "*":
        counter *= 2;
        break;
      case "-":
        counter -= 1;
        break;
      case "%":
        stack.push({ pc: index, depth: blockStack.length });
        break;
      case "<": {
        const top = stack[stack.length - 1];
        if (top !== undefined && top.depth === blockStack.length) {
          stack.pop();
          resultOfAction = top.pc;
        }
        break;
      }
      case "¿":
        if ((counter ?? 0) > 0) {
          resultOfAction = 0;
          blockStack.push(true);
        } else {
          let depth = 1;
          let closing = -1;
          for (let i = index + 1; i < code.length; i++) {
            const c = code[i];
            if (c === "¿") depth += 1;
            else if (c === "?") {
              depth -= 1;
              if (depth === 0) {
                closing = i;
                break;
              }
            }
          }
          resultOfAction = closing + 1;
        }
        break;
      case "?":
        blockStack.pop();
        break;
      default:
        break;
    }

    if (
      element === "<" &&
      resultOfAction !== undefined &&
      typeof resultOfAction === "number"
    ) {
      index = resultOfAction + 1;
      continue;
    }

    if (
      element === "¿" &&
      typeof resultOfAction === "number" &&
      resultOfAction > 0
    ) {
      index = resultOfAction;
      continue;
    }

    index += 1;
  }

  return counter;
}
