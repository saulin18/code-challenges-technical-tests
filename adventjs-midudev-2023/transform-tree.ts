// Fácil
// Ayer viernes alguien hizo despliegue a producción y se rompió la aplicación de
// montaje de árboles de Navidad. Nos han pedido que lo arreglemos lo antes posible.

// El problema es que el formato de los árboles ha cambiado. Es un array de números…
// ¡pero debería ser un objeto! Por ejemplo el árbol: [3, 1, 0, 8, 12, null, 1] se ve así:

// //        3
// //      /   \
// //     1     0
// //    / \     \
// //   8  12     1
// Lo que necesitamos es transformar el array en un objeto donde cada nodo del árbol
//  tiene las propiedades value, left y right.

// Por ejemplo, al ejecutar tu función transformTree con [3, 1, 0, 8, 12, null, 1] debería devolver esto:

// {
//   value: 3,
//   left: {
//     value: 1,
//     left: {
//       value: 8,
//       left: null,
//       right: null
//     },
//     right: {
//       value: 12,
//       left: null,
//       right: null
//     }
//   },
//   right: {
//     value: 0,
//     left: null,
//     right: {
//       value: 1,
//       left: null,
//       right: null
//     }
//   }
// }
// El elfo que está de guardia y que intentó solucionar el problema antes de irse a casa, nos ha
// dejado algunas pistas:
// Si un nodo no tiene valor, se representa con null. Por lo tanto, si un nodo tiene valor
// null, no tendrá hijos.
// El nodo raíz se encuentra en el índice 0 del array.
// Existe una relación entre el índice de un nodo y el índice de sus hijos. ¡Busca el patrón!
//

type TreeNode = {
  value: number;
  left: TreeNode | null;
  right: TreeNode | null;
};

/** Recursivo: hijos en índices 2i+1 y 2i+2. */
function transformTree(tree: (number | null)[]): TreeNode | null {
  if (tree.length === 0) {
    return null;
  }

  function build(i: number): TreeNode | null {
    if (i >= tree.length || tree[i] === null) {
      return null;
    }
    return {
      value: tree[i] as number,
      left: build(2 * i + 1),
      right: build(2 * i + 2),
    };
  }

  return build(0);
}

/**
 * Iterativo (BFS): misma lógica, pero la cola debe guardar el índice en el array.
 * Nunca uses indexOf(value): varios nodos pueden tener el mismo valor.
 */
function transformTreeIterative(tree: (number | null)[]): TreeNode | null {
  if (tree.length === 0 || tree[0] === null) {
    return null;
  }

  const root: TreeNode = {
    value: tree[0] as number,
    left: null,
    right: null,
  };

  const queue: Array<{ node: TreeNode; i: number }> = [{ node: root, i: 0 }];

  while (queue.length > 0) {
    const item = queue.shift();
    if (!item) continue;
    const { node, i } = item;
    const leftIndex = 2 * i + 1;
    const rightIndex = 2 * i + 2;

    if (leftIndex < tree.length && tree[leftIndex] !== null) {
      node.left = {
        value: tree[leftIndex] as number,
        left: null,
        right: null,
      };
      queue.push({ node: node.left, i: leftIndex });
    } else {
      node.left = null;
    }

    if (rightIndex < tree.length && tree[rightIndex] !== null) {
      node.right = {
        value: tree[rightIndex] as number,
        left: null,
        right: null,
      };
      queue.push({ node: node.right, i: rightIndex });
    } else {
      node.right = null;
    }
  }

  return root;
}
