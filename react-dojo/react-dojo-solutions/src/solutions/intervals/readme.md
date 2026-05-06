práctica
básico
Marcar como completado
Cronómetro con intervalos
Construye un cronómetro que puedes iniciar, pausar y resetear. Usa una ref para guardar el id del intervalo — no estado — y limpia siempre en el cleanup para que el timer no quede vivo al desmontar.

Objetivos
1.
Estado elapsed (ms) que empieza en 0
2.
Estado running (boolean) que controla el botón start/pause
3.
Al correr, usa setInterval cada 10ms con actualización funcional: setElapsed(e => e + 10)
4.
Guarda el id del intervalo en una useRef — no en estado
5.
El cleanup del useEffect llama clearInterval con el id guardado
6.
Botón 'reset' pone elapsed en 0 y pausa
7.
Formato de salida: mm:ss.cc (centésimas)