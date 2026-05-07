Lista con useReducer
Lista de tareas con tres acciones: agregar, alternar done, y eliminar. Implementa el reducer manteniendo las reglas de pureza: nada de mutación, cada transición devuelve un estado nuevo.

Objetivos
1.
Define un reducer con acciones: 'add', 'toggle', 'remove'
2.
Estado inicial: { items: [], next: 1 } — next sirve como ID incremental
3.
Submit del form hace dispatch de 'add'
4.
Click en el texto hace dispatch de 'toggle' (línea cruzada cuando done)
5.
Botón × hace dispatch de 'remove'
6.
El reducer NO debe mutar el estado (spread, filter, map)