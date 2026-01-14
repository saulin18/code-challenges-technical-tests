//surviveRoulette(4, 2)
//// Resultado: 0
//
//// Explicación:
//// Inicio de 4 víctimas: [0, 1, 2, 3]
//// Cuenta 2 desde posición 0: elimina 1 → [0, 2, 3]
//// Cuenta 2 desde la última víctima: elimina 3 → [0, 2]
//// Cuenta 2 desde la última víctima: elimina 2 → [0]
//// Sobrevive: 0
//
//surviveRoulette(5, 3)
//// Resultado: 3
//
//// Explicación:
//// Inicio de 5 víctimas: [0, 1, 2, 3, 4]
//// Cuenta 3 desde 0: elimina 2 → [0, 1, 3, 4]
//// Cuenta 3 desde 3: elimina 0 → [1, 3, 4]
//// Cuenta 3 desde 1: elimina 4 → [1, 3]
//// Cuenta 3 desde 1: elimina 1 → [3]
//// Sobrevive: 3
//
//surviveRoulette(5, 10)
//// Resultado: 3
//
//// Explicación:
//// Inicio de 5 víctimas: [0, 1, 2, 3, 4]
//// Cuenta 10 desde 0: elimina 4 → [0, 1, 2, 3]
//// Cuenta 10 desde 0: elimina 2 → [0, 1, 3]
//// Cuenta 10 desde 0: elimina 0 → [1, 3]
//// Cuenta 10 desde 1: elimina 1 → [3]
//// Sobrevive: 3
//Nota: Este es un problema clásico conocido como el "Problema de Josefo". Debes encontrar
// una solución eficiente, ya que n puede ser muy grande.

//int josephus(int n, int k) {
//    int res = 0;
//    for (int i = 1; i <= n; ++i)
//      res = (res + k) % i;
//    return res + 1;
//}

function surviveRoulette(n: number, k: number): number {
    
    let res: number = 0
    let arr = Array.from({length: n}, (index, arr) => index) as number[]


    for (let index = 0; index < arr.length; index++) {
        res = (res + k) % index
        arr.splice(res, 1)
    }

    return arr[0]
  }