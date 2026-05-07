Memorizar callbacks
Un padre con un contador pasa onDelete a una lista memoizada. Cada render recrea onDelete, invalidando memo en todos los items. Usa useCallback para que los items dejen de re-renderizar cuando solo cambia el contador.

Objetivos
1.
Envuelve onDelete en useCallback con las dependencias correctas
2.
Verifica en la consola que los items ya no se re-renderizan al incrementar el contador
3.
Comprende por qué memo(Item) sin useCallback no es suficiente