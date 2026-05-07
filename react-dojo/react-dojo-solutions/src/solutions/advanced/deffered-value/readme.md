Búsqueda sin bloqueo
Un input filtra una lista de 6.000 ítems. Tal cual está, el input se siente lento porque el filtrado pesa. Usa useDeferredValue para que el input responda al instante y la lista se actualice con prioridad baja.

Objetivos
1.
Mantén el input controlado (setState urgente)
2.
Crea un valor diferido a partir de query
3.
Pasa el deferred — no query — al componente pesado
4.
Muestra un indicador 'actualizando...' mientras query !== deferred
5.
Atenúa visualmente la lista mientras está desfasada (opacity)