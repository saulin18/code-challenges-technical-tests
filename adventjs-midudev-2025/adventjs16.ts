
//Reto #16: 🎁 Empaquetando regalos para Santa
//Santa quiere repartir regalos de la forma más eficiente posible 🎁. Tiene una lista de regalos, cada uno con un peso, y un trineo que solo
//puede cargar hasta un peso máximo.
//
//Los regalos se entregan en orden, y Santa no puede cambiar ese orden. Cuando un regalo no cabe en el trineo actual, Santa envía el trineo y 
// prepara uno nuevo.
//
//Tu tarea es escribir una función que calcule el número mínimo de trineos necesarios para entregar todos los regalos.
//
//Eso sí, ten en cuenta que a veces hay un regalo que no cabe en el trineo, entonces hay que devolver null porque ese trineo no sirve para ese 
// pack de regalos.
//
//packGifts([2, 3, 4, 1], 5)
//// 2 trineos
//// Trineo 1: 2 + 3 = 5
//// Trineo 2: 4 + 1 = 5
//
//packGifts([3, 3, 2, 1], 3)
//// 3 trineos
//// Trineo 1: 3
//// Trineo 2: 3
//// Trineo 3: 2 + 1 = 3
//
//packGifts([1, 1, 1, 1], 2)
//// 2 trineos
//// Trineo 1: 1 + 1 = 2
//// Trineo 2: 1 + 1 = 2
//
//packGifts([5, 6, 1], 5)
//// null
//// Hay un regalo de peso 6 que no cabe
//
//packGifts([], 10)
// 0 trineos
// No hay regalos que entregar
/**
 * @param {number[]} gifts - The gifts to pack
 * @param {number} maxWeight - The maximum weight of the sleigh
 * @returns {number | null} The number of sleighs needed
 * Return null if no sleigh can carry all the gifts
 */
type Gifts = number[]
type MaxWeight = number
type Result = number | null
//function packGifts(gifts: Gifts, maxWeight: MaxWeight): Result {
//
//    if (gifts.length === 0) {
//        return 0;
//    }
//
//    let currentSleighWeight = maxWeight;
//    let sleighCount = 1;
//
//    for (const gift of gifts) {
//
//        if (gift > maxWeight) {
//            return null;
//        }
//
//        if(gift > currentSleighWeight){
//          currentSleighWeight = maxWeight
//          sleighCount++
//        }
//
//        currentSleighWeight -= gift;
//
//        if (currentSleighWeight == 0) {
//            sleighCount++;
//            currentSleighWeight = maxWeight;
//        }
//    }
//
//    if (currentSleighWeight < maxWeight) sleighCount +=1
//    return sleighCount;
//}
function packGifts(gifts: Gifts, maxWeight: MaxWeight): Result {

    if (gifts.length === 0) {
        return 0;
    }

    let currentSleighWeight = maxWeight;
    let sleighCount = 1;

    for (const gift of gifts) {

        if (gift > maxWeight) {
            return null;
        }

        if (gift > currentSleighWeight) {
            currentSleighWeight = maxWeight
            sleighCount++
        }

        currentSleighWeight -= gift;
    }

    return sleighCount;
}

