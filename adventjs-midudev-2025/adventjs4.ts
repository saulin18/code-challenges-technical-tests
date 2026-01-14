//MEDIO
//Los elfos han encontrado el código cifrado que protege la puerta del taller de Santa 🔐. El PIN tiene 4 dígitos, y está escondido dentro de bloques como estos:
//
//[1++][2-][3+][<]
//Escribe una función que descifre el PIN a partir del código.
//
//El código está formado por bloques entre corchetes [...] y cada bloque genera un dígito del PIN.
//
//Un bloque normal tiene la forma [nOP...], donde n es un número (0-9) y después puede haber una lista de operaciones (opcionales).
//
//Las operaciones se aplican en orden al número y son:
//
//+ suma 1
//- resta 1
//El resultado siempre es un dígito (aritmética mod 10), por ejemplo 9 + 1 → 0 y 0 - 1 → 9.
//
//También existe el bloque especial [<], que repite el dígito del bloque anterior.
//
//Si al final hay menos de 4 dígitos, se debe devolver null.
//
//🧩 Ejemplos
//decodeSantaPin('[1++][2-][3+][<]')
//// "3144"
//
//decodeSantaPin('[9+][0-][4][<]')
//// "0944"
//
//decodeSantaPin('[1+][2-]')
//// null (solo 2 dígitos)

/**
 * @param {string} code - The code to decipher
 * @returns {string} The deciphered PIN
 */
function decodeSantaPin(code: string): string | null {
  const digits: string[] = [];

  if (code.split("[").length < 5) {
    return null;
  }

  let lastNum = Number(digits[digits.length - 1]) || 0;
  let isSpecialBlock = false

  for (const char of code) {

      if (char === "[") {
      lastNum = 0; 
      isSpecialBlock = false
      continue;
    }

    if (!isNaN(Number(char))) {
      lastNum = Number(char);
      continue;
    }

    //It's a operation
    switch (char) {
      case "+":
        lastNum = (lastNum + 1) % 10;
        break;
      case "-":
        lastNum = (lastNum -1 + 10) % 10;
        break;
      case "<":
        if(digits.length === 0){
          return null
        }
        digits.push(digits[digits.length - 1]);
        isSpecialBlock = true
        break;

      case "]":

        if (digits.length === 4) {
          return digits.join("");
        }

        if(!isSpecialBlock){
           digits.push(String((lastNum + 10) % 10));
        }
       
        break;
    }
  }

    if (digits.length !== 4) {
          return null
      }

  return digits.join("");
}