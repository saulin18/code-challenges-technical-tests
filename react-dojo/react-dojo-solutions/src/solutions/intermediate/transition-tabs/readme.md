Tabs sin bloqueo
Tres tabs, una renderiza 4000 items y bloquea el hilo. Al hacer click la UI se congela y la tab activa no responde hasta que termina. Usa useTransition para mantener los clicks responsivos y mostrar un indicador de carga.

Objetivos
1.
Envuelve setActiveTab en startTransition
2.
Usa isPending para atenuar visualmente la tab que está cargando
3.
Comprueba que las tabs responden al instante aunque la lista tarde en renderizar
tu código
