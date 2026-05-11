Input controlado
Un input que muestra en tiempo real lo que el usuario escribe. El valor del input viene del estado y se actualiza con onChange. Este patrón se llama 'controlled component'.

Objetivos
1.
Declara estado text con string vacío
2.
El input tiene value={text}
3.
onChange actualiza con setText(e.target.value)
4.
Muestra el texto debajo en un elemento <p>