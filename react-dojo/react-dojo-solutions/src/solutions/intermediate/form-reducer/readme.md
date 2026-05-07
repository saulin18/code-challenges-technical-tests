Formulario con validación
Un formulario de registro con tres campos (email, password, confirmación). Modela los cambios y la validación con useReducer: cada acción nombrada, reducer puro, errores derivados en cada transición.

Objetivos
1.
Reducer con acciones 'change', 'blur', 'submit'
2.
Estado: { values, touched, submitted } — errors se derivan en render, no se guardan
3.
Valida email (formato), password (≥ 6 chars), confirm (igual a password)
4.
Solo muestra errores de un campo cuando está 'touched' o tras submit
5.
Submit deshabilitado si hay errores — pero calculado en render, no guardado
6.
Al submit exitoso, muestra un estado 'enviado'
tu código
