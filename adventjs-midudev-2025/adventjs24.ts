
//En el Polo Norte, los elfos tienen dos árboles binarios mágicos que generan energía 🌲🌲 para mantener encendida la estrella navideña
//⭐️. Sin embargo, para que funcionen correctamente, los árboles deben estar en perfecta sincronía como espejos 🪞.
//
//Dos árboles binarios son espejos si:
//
//Las raíces de ambos árboles tienen el mismo valor.
//Cada nodo del primer árbol debe tener su correspondiente nodo en la posición opuesta en el segundo árbol.
//Y el árbol se representa con tres propiedades value, left y right. Dentro de estas dos últimas va mostrando el resto de ramas (si es que tiene):
//
//const tree = {
//  value: '⭐️',
//  left: {
//    value: '🎅'
//    // left: {...}
//    // right: { ... }
//  },
//  right: {
//    value: '🎁'
//    // left: { ... }
//    // right: { ...&nbsp;}
//  }
//}
//Santa necesita tu ayuda para verificar si los árboles están sincronizados para que la estrella pueda seguir brillando.
//Debes devolver un array donde la primera posición indica si los árboles están sincronizados y la segunda posición devuelve el valor
//de la raíz del primer árbol.
//
//const tree1 = {
//  value: '🎄',
//  left: { value: '⭐' },
//  right: { value: '🎅' }
//}
//
//const tree2 = {
//  value: '🎄',
//  left: { value: '🎅' }
//  right: { value: '⭐' },
//}
//
//isTreesSynchronized(tree1, tree2) // [true, '🎄']
//
///*
//  tree1          tree2
//   🎄              🎄
//  / \             / \
//⭐   🎅         🎅   ⭐
//*/
//
//const tree3 = {
//  value: '🎄',
//  left: { value: '🎅' },
//  right: { value: '🎁' }
//}
//
//isTreesSynchronized(tree1, tree3) // [false, '🎄']
//
//const tree4 = {
//  value: '🎄',
//  left: { value: '⭐' },
//  right: { value: '🎅' }
//}
//
//isTreesSynchronized(tree1, tree4) // [false, '🎄']
//
//isTreesSynchronized(
//  { value: '🎅' },
//  { value: '🧑‍🎄' }
//) // [false, '🎅']


/**
 * @param {object} tree1 - The first binary tree.
 * @param {object} tree2 - The second binary tree.
 * @returns {[boolean, string]}
 */


interface Tree {
    value: string;
    left?: any;
    right?: any | undefined
}

//function isTreesSynchronized(
//    tree1: Tree | undefined,
//    tree2: Tree | undefined
//): [boolean, string] {
//
//    if (!tree1) {
//        return [false, ""];
//    }
//
//
//    if (!tree2) {
//        return [false, tree1.value];
//    }
//
//    const temp = tree1?.value
//
//    function invertBinaryTree(tree: Tree) {
//
//
//        const temp = tree.right
//
//        tree.right = tree.left
//        tree.left = temp
//
//        if (tree.left) invertBinaryTree(tree.left)
//        if (tree.right) invertBinaryTree(tree.right)
//
//        return tree
//    }
//
//    function isEqualTree(tree1: Tree | undefined, tree2: Tree | undefined): boolean {
//
//
//        if (tree1 === undefined && tree2 === undefined) {
//            return true
//        }
//
//        if (tree1 === undefined && tree2 !== undefined || tree2 === undefined && tree1 !== undefined) {
//            return false
//        }
//
//        if (tree1?.value !== tree2?.value) {
//            return false
//        }
//
//        const isValidLeft = isEqualTree(tree1?.left, tree2?.left)
//        const isValidRight = isEqualTree(tree1?.right, tree2?.right)
//
//        return isValidRight && isValidLeft
//    }
//
//    const inverted1 = invertBinaryTree(tree1)
//
//    const isValidTrees = isEqualTree(inverted1, tree2)
//
//    return isValidTrees ? [true, temp!] : [false, temp!]
//
//}

function isTreesSynchronized(
    tree1: Tree | undefined,
    tree2: Tree | undefined
): [boolean, string] {

    if (!tree1) {
        return [false, ""];
    }


    if (!tree2) {
        return [false, tree1.value];
    }

    const temp = tree1?.value

    function isMirrorTree(tree1: Tree | undefined, tree2: Tree | undefined): boolean {


        if (tree1 === undefined && tree2 === undefined) {
            return true
        }

        if (tree1 === undefined || tree2 === undefined) {
            return false
        }

        if (tree1?.value !== tree2?.value) {
            return false
        }

        const isValidLeft = isMirrorTree(tree1?.left, tree2?.right)
        const isValidRight = isMirrorTree(tree1?.right, tree2?.left)

        return isValidRight && isValidLeft
    }

    const isValidTrees = isMirrorTree(tree1, tree2)

    return [isValidTrees, temp]

}