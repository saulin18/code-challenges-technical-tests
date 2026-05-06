Derivar listas con useMemo
Una lista de tareas se filtra y ordena con cada render — incluso cuando solo cambia un contador no relacionado. Usa useMemo para que el cálculo pesado solo se repita cuando cambien query u order.

Objetivos
1.
Envuelve el filtrado + ordenamiento en useMemo
2.
Declara [query, order] como dependencias
3.
Verifica que el contador ya no recalcula la lista (observa el log en consola)