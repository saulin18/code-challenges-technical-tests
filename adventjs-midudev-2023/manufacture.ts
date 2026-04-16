// En el taller de Santa, los elfos tienen una lista de regalos 
// que desean fabricar y un conjunto limitado de materiales.
// Los regalos son cadenas de texto y los materiales son caracteres. 
// Tu tarea es escribir una función que, dada una lista de regalos y 
// los materiales disponibles, devuelva una lista de los regalos que se pueden fabricar.
// Un regalo se puede fabricar si contamos con todos los materiales necesarios para fabricarlo.
// const gifts = ['tren', 'oso', 'pelota']
// const materials = 'tronesa'
// manufacture(gifts, materials) // ["tren", "oso"]
// // 'tren' SÍ porque sus letras están en 'tronesa'
// // 'oso' SÍ porque sus letras están en 'tronesa'
// // 'pelota' NO porque sus letras NO están en 'tronesa'
// const gifts = ['juego', 'puzzle']
// const materials = 'jlepuz'
// manufacture(gifts, materials) // ["puzzle"]
// const gifts = ['libro', 'ps5']
// const materials = 'psli'
// manufacture(gifts, materials) // []
function manufacture(gifts: string[], materials: string) {
    const materialsMap: Record<string, number> = {}
    materials.split("").forEach((material) => {
        materialsMap[material] = (materialsMap[material] || 0) + 1
    })

    return gifts.filter((gift) => {
        const giftMap: Record<string, number> = {}
        gift.split("").forEach((letter) => {
            giftMap[letter] = (giftMap[letter] || 0) + 1
        })
        return Object.keys(giftMap).every((letter) => {
            return materialsMap[letter] >= 0
        })
    })
}