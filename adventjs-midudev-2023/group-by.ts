// Santa 🎅 está organizando una gran cena navideña 🫓 y quiere asegurarse de que todos los
//  platos sean únicos y variados!

// Te da una lista de platos navideños donde cada elemento consiste en una lista de
// strings que comienza con el nombre del plato, seguido de todos los ingredientes utilizados para su preparación.

// Tienes que escribir una función que agrupe los platos por ingredientes siempre qu
// e haya al menos 2 platos que los contengan.

// Así que devolvemos un array de arrays donde la primera posición es el nombre del ingrediente
//  y el resto los nombres de los platos.

// Tanto la lista de ingredientes como los platos deben estar ordenados alfabéticamente.

// const dishes = [
//   ["christmas turkey", "turkey", "sauce", "herbs"],
//   ["cake", "flour", "sugar", "egg"],
//   ["hot chocolate", "chocolate", "milk", "sugar"],
//   ["pizza", "sauce", "tomato", "cheese", "ham"],
// ]

// organizeChristmasDinner(dishes)

// /*

// "sauce" está en 2 platos: "christmas turkey" y "pizza".
// "sugar" está en 2 platos: "cake" y "hot chocolate".
// El resto de ingredientes solo aparecen en un plato, por lo que no los mostramos.

// Enseñamos primero "sauce" porque alfabéticamente está antes que "sugar".
// Y los platos de cada ingrediente también están ordenados alfabéticamente.

// [
//   ["sauce", "christmas turkey", "pizza"],
//   ["sugar", "cake", "hot chocolate"]
// ]
// */
// Ten en cuenta que:

// Todos los nombres de los platos son diferentes.
// Los nombres de los ingredientes para un plato dado son distintos entre sí.
// Si no hay ingredientes repetidos, devolvemos un array vacío.

// function organizeChristmasDinner(dishes: string[][]){
//   const ingredientMap = new Map();
//   const result = [];

//   dishes.forEach(([dish, ...ingredients]) => {

//     ingredients.forEach(ingredient => {

//       if(!ingredientMap.has(ingredient)) {
//         ingredientMap.set(ingredient, new Set());
//       }
//       ingredientMap.get(ingredient).add(dish);

//     })

//   });

//   for (const [ingredient, dishesSet] of ingredientMap.entries()) {
//     if (dishesSet.size >= 2) {
//       result.push([ingredient, ...Array.from(dishesSet).sort()]);
//     }
//   }

//   result.sort(([a], [b]) => a.localeCompare(b));
//   return result
// }


function organizeChristmasDinner(dishes: string[][]) {
  const pairs = [];
  for (const row of dishes) {
    const [dishName, ...ingredients] = row;
    for (const ingredient of ingredients) {
      pairs.push([ingredient, dishName]);
    }
  }

  pairs.sort((a, b) => a[0].localeCompare(b[0]) || a[1].localeCompare(b[1]));

  const grouped = Object.groupBy(pairs, ([ingredient]) => ingredient);

  return Object.entries(grouped)
    .filter(
      (entry) =>
        entry[1] !== undefined && entry[1].length >= 2,
    )
    .map(([ingredient, rows]) => [
      ingredient,
      ...rows!.map(([, dishName]) => dishName),
    ]);
}
console.log(
  organizeChristmasDinner([
    ["christmas turkey", "turkey", "sauce", "herbs"],
    ["cake", "flour", "sugar", "egg"],
    ["hot chocolate", "chocolate", "milk", "sugar"],
    ["pizza", "sauce", "tomato", "cheese", "ham"],
  ]),
);
// [
//   ["sauce", "christmas turkey", "pizza"],
//   ["sugar", "cake", "hot chocolate"]
// ]