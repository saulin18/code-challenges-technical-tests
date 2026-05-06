Lista con búsqueda en tiempo real
Un campo de búsqueda filtra una lista de frutas mientras el usuario escribe. El resultado filtrado se deriva directamente del estado — sin useState extra ni useMemo necesario a esta escala.

Objetivos
1.
Declara un estado query que empiece en cadena vacía
2.
Vincula el input al estado con value y onChange
3.
Deriva filtered como FRUTAS.filter(...) directamente en el render, sin useState adicional
4.
Muestra el número de resultados: '{n} resultado(s)'
5.
Muestra el mensaje 'Sin resultados' cuando filtered está vacío
6.
Botón 'limpiar' resetea query a cadena vacía
tu código
