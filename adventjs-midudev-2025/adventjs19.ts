//¡El GPS del trineo se ha vuelto loco! 😱 Papá Noel tiene los tramos de su viaje, pero están todos desordenados.
//
//Tu misión es reconstruir la ruta completa desde el origen hasta el destino final.
//
//Ten en cuenta: El primer elemento del array es siempre el primer tramo del viaje. A partir de ahí, debes ir conectando los destinos con
// los siguientes orígenes.
//
//revealSantaRoute([
//  ['MEX', 'CAN'],
//  ['UK', 'GER'],
//  ['CAN', 'UK']
//])
//// → ['MEX', 'CAN', 'UK', 'GER']
//
//revealSantaRoute([
//  ['USA', 'BRA'],
//  ['JPN', 'PHL'],
//  ['BRA', 'UAE'],
//  ['UAE', 'JPN'],
//  ['CMX', 'HKN']
//])
//// → ['USA', 'BRA', 'UAE', 'JPN', 'PHL']
//
//revealSantaRoute([
//  ['STA', 'HYD'],
//  ['ESP', 'CHN']
//])
//// → ['STA', 'HYD']
//🔎 A tener en cuenta:
//
//No hay rutas duplicadas ni ciclos en el camino de Papá Noel.
//Puede haber tramos que no pertenezcan a la ruta; estos deben ignorarse.

/**
 * @param {string[][]} routes - Array of [origin, destination] pairs
 * @returns {string[]} The reconstructed route
 */
//function revealSantaRoute(routes) {
//
//
//  const result = [];
//
//  for (let path = 0; path < routes.length; path++) {
//    const [from, to] = routes[path]
//
//    if (result.length === 0) {
//    result.push(from);
//    result.push(to)
//    }
//
//    for (let index = 0; index < routes.length; index++) {
//      const [otherRoute, otherPath] = routes[index];
//
//      if (to === otherRoute) {
//        result.push(otherPath)
//        break;
//      }
//    }
//  }
//
//  return result;
//}

function revealSantaRoute(routes: string[][]): string[] {
  const routeMap = new Map<string, string>();
  const res: string[] = []

  for (const [origin, destination] of routes) {
    routeMap.set(origin, destination);
  }

    let currentLocation = routes[0][1]; 
    // Start from the destination of the first route  
    res.push(routes[0][0]);
    res.push(currentLocation);
   

    while (routeMap.has(currentLocation)){
      res.push(routeMap.get(currentLocation) as string);
      currentLocation = routeMap.get(currentLocation) as string 
    }


    return res
}

console.log(
  revealSantaRoute([
    ["MEX", "CAN"],
    ["UK", "GER"],
    ["CAN", "UK"],
  ])
);
