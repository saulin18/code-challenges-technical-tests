// el tema de las redes sociales, Santa Claus tiene pánico que los niños se despierten
//  mientras él está repartiendo regalos en sus casos, usen el móvil para grabarlo
// y se haga viral en TikTok.

// Quiere evitarlo a toda costa. Cada casa en esa calle tiene un número de regalos
// preparados. Sin embargo, las casas tienen un sistema de seguridad conectado entre
// casas adyacentes, por lo que no puede dejar los regalos en dos casas seguidas, o se activará
// la alarma que alertará a los niños.

// Dada un array de enteros no negativos regalos que representa la cantidad de regalos
// en cada casa, tu tarea es ayudar a Papá Noel a determinar la máxima cantidad
//  de regalos que puede entregar en una noche sin activar ninguna alarma.

// maxGifts([2, 4, 2]) // 4 (4)
// maxGifts([5, 1, 1, 5]) // 10 (5 + 5)
// maxGifts([4, 1, 1, 4, 2, 1]) // 9 (4 + 4 + 1)
// maxGifts([1, 3, 1, 3, 100]) // 103 (3 + 100)

// // Dp problem
// function maxGifts(houses: number[]): number {
//   function recurse(index: number, memo: Record<number, number>) {
//     if (index >= houses.length) return 0;
//     if (index in memo) return memo[index];
//     const skip = recurse(index + 1, memo);
//     const take = houses[index] + recurse(index + 2, memo);
//     memo[index] = Math.max(skip, take);
//     return memo[index];
//   }
//   const result = recurse(0, {});
//   return result;
// }



 function maxGifts(houses: number[]): number {
    const n = houses.length;
    const dp = Array(n).fill(0);
 
    dp[0] = houses[0];
    dp[1] = Math.max(houses[0], houses[1]);

    for(let i = 2; i < n; i++) {
        dp[i] = Math.max(dp[i - 1], dp[i - 2] + houses[i]);
    }
    
    return dp[n - 1];
}

console.log(maxGifts([2, 4, 2]));
console.log(maxGifts([5, 1, 1, 5]));
console.log(maxGifts([4, 1, 1, 4, 2, 1]));
console.log(maxGifts([1, 3, 1, 3, 100]));
