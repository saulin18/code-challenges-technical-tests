Context sin re-renders espurios
Crea un ThemeProvider que expone theme y setTheme. El reto: si pasas { theme, setTheme } como value inline, cada render crea un objeto nuevo y TODOS los consumidores se re-renderizan — incluso los que no leen theme. Memoiza el value.

Objetivos
1.
Define ThemeContext con createContext
2.
ThemeProvider guarda theme en useState
3.
El value pasado al Provider se memoiza con useMemo
4.
Un hook useTheme() que lee el contexto y lanza error si no hay Provider
5.
Un componente <Toolbar/> que lee setTheme — NO debe re-renderizarse al cambiar tick del padre
6.
Un componente <Card/> memoizado que lee theme