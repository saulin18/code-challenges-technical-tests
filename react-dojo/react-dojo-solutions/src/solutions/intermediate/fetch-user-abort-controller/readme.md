Fetch con cancelación
Carga datos de un usuario al cambiar de id. El truco: si el usuario hace click rápido entre varios ids, la respuesta vieja puede llegar después de la nueva y sobrescribir la UI. Cancela con AbortController.

Objetivos
1.
useEffect que dispara un fetch cada vez que cambia userId
2.
Crea un AbortController y pásalo al fetch como { signal }
3.
En el cleanup del efecto, llama ctrl.abort()
4.
Ignora el error AbortError — es esperado al cancelar
5.
Muestra 'cargando...', error, o los datos según el estado
6.
Los botones cambian userId instantáneamente, sin esperar al fetch