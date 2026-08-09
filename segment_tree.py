"""
Segment Tree (arbol de segmentos)
==================================

Problema que resuelve:
  Dado un array, responder rapido preguntas de tipo "dame el resultado
  (suma, min, max, etc.) de un rango [l, r]" y permitir actualizar un
  elemento, todo en O(log n), en vez de O(n) por consulta como haria
  un enfoque ingenuo.

Idea central:
  Se construye un arbol binario donde cada nodo representa un RANGO del
  array original:
    - La raiz representa el array completo [0, n-1].
    - Cada nodo se divide en dos mitades: hijo izquierdo [l, mid] e
      hijo derecho [mid+1, r].
    - Las hojas representan rangos de tamano 1, es decir, un solo
      elemento del array original.
    - Cada nodo interno guarda el resultado combinado de sus dos hijos
      (en este caso, la suma; pero podria ser min, max, gcd, etc.).

  Como cada nivel del arbol divide el rango a la mitad, la altura es
  O(log n). Por eso build es O(n), y update/query son O(log n): en el
  peor caso recorremos un camino desde la raiz hasta una hoja (mas una
  rama extra cuando el rango de la consulta no calza perfecto con los
  nodos).

Representacion en memoria (arbol implicito en un array):
  En vez de crear nodos con punteros (como un arbol "de verdad"), se
  usa un array `self.tree` donde, para un nodo en la posicion `node`:
    - Hijo izquierdo esta en `2*node + 1`
    - Hijo derecho esta en `2*node + 2`
  Esta es la misma tecnica que usa un heap binario. Es mas simple y
  cache-friendly que manejar nodos con punteros.

  Tamano del array: en el peor caso (n no es potencia de 2) se necesita
  hasta ~4*n posiciones para que la indexacion 2*node+1/2*node+2 nunca
  se salga de rango. Es un desperdicio de memoria aceptable a cambio de
  simplicidad (la alternativa es un arbol iterativo mas compacto pero
  mas dificil de entender).
"""


class SegmentTree:
    def __init__(self, data, combine=lambda a, b: a + b, identity=0):
        """
        data: lista original sobre la que se construye el arbol.
        combine: funcion binaria usada para mezclar dos rangos hijos
                 en el valor del padre. Por defecto, suma.
                 Para minimos: combine=min, identity=float('inf')
                 Para maximos: combine=max, identity=float('-inf')
        identity: elemento neutro de `combine`, se usa quiero pedir
                  un rango que cae fuera de los limites del nodo
                  actual (no debe afectar el resultado).
        """
        self.n = len(data)
        self.combine = combine
        self.identity = identity
        # 4*n es una cota segura para evitar overflow de indices con
        # la indexacion 2*node+1 / 2*node+2 en un arbol no perfectamente
        # balanceado.
        self.tree = [identity] * (4 * self.n)
        if self.n > 0:
            self._build(data, node=0, start=0, end=self.n - 1)

    def _build(self, data, node, start, end):
        """
        Construye recursivamente el arbol para el rango [start, end],
        guardando el resultado en self.tree[node].
        """
        # Caso base: rango de tamano 1 -> es una hoja, guarda el valor
        # directo del array original.
        if start == end:
            self.tree[node] = data[start]
            return

        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2

        # Construye primero ambas mitades (post-order: hijos antes que
        # el padre), porque el valor del padre depende de los hijos.
        self._build(data, left_node, start, mid)
        self._build(data, right_node, mid + 1, end)

        # El nodo actual es la combinacion de sus dos hijos.
        self.tree[node] = self.combine(self.tree[left_node], self.tree[right_node])

    def update(self, index, value):
        """Punto de entrada publico: cambia data[index] = value."""
        if not (0 <= index < self.n):
            raise IndexError("index out of bounds")
        self._update(node=0, start=0, end=self.n - 1, index=index, value=value)

    def _update(self, node, start, end, index, value):
        """
        Baja por el arbol hasta encontrar la hoja que representa
        `index`, la actualiza, y al volver (en la recursion) recalcula
        cada ancestro combinando sus hijos de nuevo.
        """
        if start == end:
            # Llegamos a la hoja correspondiente al indice buscado.
            self.tree[node] = value
            return

        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2

        if index <= mid:
            # El indice cae en la mitad izquierda: solo hace falta
            # bajar por ese lado, el derecho no cambia.
            self._update(left_node, start, mid, index, value)
        else:
            self._update(right_node, mid + 1, end, index, value)

        # Al deshacer la recursion, recomponemos el valor de este nodo
        # con los valores (posiblemente actualizados) de sus hijos.
        self.tree[node] = self.combine(self.tree[left_node], self.tree[right_node])

    def query(self, left, right):
        """Punto de entrada publico: combina el rango [left, right] (inclusive)."""
        if not (0 <= left <= right < self.n):
            raise IndexError("range out of bounds")
        return self._query(node=0, start=0, end=self.n - 1, left=left, right=right)

    def _query(self, node, start, end, left, right):
        """
        Compara el rango del nodo actual [start, end] contra el rango
        pedido [left, right]. Hay tres casos:

        1) Sin overlap: [start, end] no toca [left, right] en absoluto.
           -> no aporta nada, devolvemos el elemento neutro.
        2) Overlap total: [start, end] esta completamente dentro de
           [left, right].
           -> todo el subarbol sirve, devolvemos el valor precalculado
              del nodo directamente (esto es lo que da el O(log n): no
              hace falta bajar mas).
        3) Overlap parcial: se solapan mas no coinciden.
           -> hay que bajar a ambos hijos y combinar lo que devuelvan.
        """
        # Caso 1: sin overlap.
        if right < start or end < left:
            return self.identity

        # Caso 2: overlap total, el nodo completo esta dentro del rango pedido.
        if left <= start and end <= right:
            return self.tree[node]

        # Caso 3: overlap parcial, hay que partir en dos.
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2

        left_result = self._query(left_node, start, mid, left, right)
        right_result = self._query(right_node, mid + 1, end, left, right)
        return self.combine(left_result, right_result)


if __name__ == "__main__":
    # Ejemplo con suma de rangos.
    data = [2, 4, 5, 7, 8, 9]
    st = SegmentTree(data)  # combine=sum por defecto

    print(st.query(1, 3))  # 4 + 5 + 7 = 16
    st.update(1, 10)       # data pasa a ser [2, 10, 5, 7, 8, 9]
    print(st.query(1, 3))  # 10 + 5 + 7 = 22
    print(st.query(0, 5))  # suma total: 2+10+5+7+8+9 = 41

    # Ejemplo con minimo de rango, usando el mismo arbol generico.
    min_st = SegmentTree(data, combine=min, identity=float("inf"))
    print(min_st.query(0, 5))  # 2
    min_st.update(0, 100)
    print(min_st.query(0, 5))  # 4
