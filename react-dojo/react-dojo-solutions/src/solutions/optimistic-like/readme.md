Like optimista
Un post con contador de likes. Al hacer click, el like tarda 800ms en guardarse y la UI no responde hasta que termina. Implementa useOptimistic para que el contador suba al instante y revierta si falla.

Objetivos
1.
Crea el estado optimista con useOptimistic a partir de likes
2.
Al hacer click, llama addOptimistic(1) antes de la petición async
3.
Actualiza el estado real con setLikes cuando la petición tiene éxito
4.
Muestra un indicador visual cuando el like está pendiente