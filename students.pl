is_parent('Luis', 'Carlos Jr.').
is_parent('Luis', 'Luis Raúl').
is_parent('Niurka', 'Carlos Jr.').
is_parent('Niurka', 'Brayam').
is_parent('Raquel', 'Niurka').
is_parent('Raquel', 'Norelis').
is_parent('Raquel', 'Nuris').
is_parent('Carlos', 'Luis').

%   Dado una base de conocimientos donde exista la
%   relación entre padre e hijo como reglas, realice una
%   aplicación de consola que pueda ser capaz de:
%   a) Imprimir en consola, dado un nombre, los padres
%   de esa persona por su nombre con el formato de  "X
%   tiene n padres: nombreA, nombreB" .
%   - en caso de que no estén registrados los padres,
%   imprimir  "No se han registrado los padres" ,
%   - en caso de que no exista el nombre en la base de
%   conocimientos, imprimir  "Nombre no registrado" .
%   b) Imprimir en consola, dado un nombre, los hijos de
%   esa persona con el formato  "X tiene n hijos:
%   nombreA, nombreB, ..., NombreN"
%   - en caso de que no estén registrados los padres,
%   imprimir  "No se han registrado hijos de esta
%   persona" ,
%   - en caso de que no exista el nombre en la base de
%   conocimientos, imprimir  "Nombre no registrado" .
%   c) Imprimir en consola, dado un nombre, los abuelos
%   de esa persona por su nombre con el formato de  "X tiene de abuelos a nombreA, nombreB, nombreC
%   y nombreD" . (Solo se deben mostrar los que estén registrados, si solo hay 1, pues solo se debe mostrar
%   ese).
%   - en caso de que no estén registrados los abuelos, imprimir  "No se han registrado abuelos de esta
%   persona" ,
%   - en caso de que no exista el nombre en la base de conocimientos, imprimir  "Nombre no registrado" .
%   d) Imprimir en consola, dado un nombre, los hermanos de esa persona.
%   - en caso de que no estén registrados los hermanos, imprimir  "No se han registrado hermanos de
%   esta persona" ,
%   - en caso de que no exista el nombre en la base de conocimientos, imprimir  "Nombre no registrado"

% Verificar si una persona existe en la base de conocimientos
person_exists(Person) :-
    is_parent(Person, _) ; is_parent(_, Person).

% Encontrar todos los padres de una persona
find_parents(Person, Parents) :-
    findall(Parent, is_parent(Parent, Person), Parents).

% Encontrar todos los hijos de una persona
find_children(Person, Children) :-
    findall(Child, is_parent(Person, Child), Children).

% Encontrar todos los abuelos de una persona
find_grandparents(Person, Grandparents) :-
    findall(Grandparent, (is_parent(Parent, Person), is_parent(Grandparent, Parent)), Grandparents).

% Encontrar todos los hermanos de una persona
find_siblings(Person, Siblings) :-
    findall(Sibling, (
        is_parent(Parent, Person),
        is_parent(Parent, Sibling),
        Sibling \= Person
    ), Siblings).

% Formatear e imprimir lista de nombres
print_names_list([]).
print_names_list([Name]) :-
    write(Name).
print_names_list([Name1, Name2]) :-
    write(Name1), write(" y "), write(Name2).
print_names_list([Name|Rest]) :-
    write(Name), write(", "),
    print_names_list(Rest).

% a) Imprimir padres
print_parents(Person) :-
    \+ person_exists(Person),
    write("Nombre no registrado"), nl.
print_parents(Person) :-
    find_parents(Person, []),
    write("No se han registrado los padres"), nl.
print_parents(Person) :-
    find_parents(Person, Parents),
    length(Parents, N),
    N > 0,
    write(Person), write(" tiene "), write(N), write(" padres: "),
    print_names_list(Parents), nl.

% b) Imprimir hijos
print_children(Person) :-
    \+ person_exists(Person),
    write("Nombre no registrado"), nl.
print_children(Person) :-
    find_children(Person, []),
    write("No se han registrado hijos de esta persona"), nl.
print_children(Person) :-
    find_children(Person, Children),
    length(Children, N),
    N > 0,
    write(Person), write(" tiene "), write(N), write(" hijos: "),
    print_names_list(Children), nl.

% c) Imprimir abuelos
print_grandparents(Person) :-
    \+ person_exists(Person),
    write("Nombre no registrado"), nl.
print_grandparents(Person) :-
    find_grandparents(Person, []),
    write("No se han registrado abuelos de esta persona"), nl.
print_grandparents(Person) :-
    find_grandparents(Person, Grandparents),
    length(Grandparents, N),
    N > 0,
    write(Person), write(" tiene de abuelos a "),
    print_names_list(Grandparents), nl.

% d) Imprimir hermanos
print_siblings(Person) :-
    \+ person_exists(Person),
    write("Nombre no registrado"), nl.
print_siblings(Person) :-
    find_siblings(Person, []),
    write("No se han registrado hermanos de esta persona"), nl.
print_siblings(Person) :-
    find_siblings(Person, Siblings),
    length(Siblings, N),
    N > 0,
    write(Person), write(" tiene "), write(N), write(" hermanos: "),
    print_names_list(Siblings), nl.

student('Ike', 25, informatics, [maths, history, uml], [3,2,3]).
student('Juan', 19, informatics, [maths, history, uml, programming], [4,4,4,3]).
student('Luis', 23, mechanic, [physics], [5]).
student('Roberto', 20, architecture, [desing], [4]).
student('Maria', 22, architecture, [maths, drawing, history], [3, 4, 5]).
student('Pedro', 21, architecture, [drawing, history], [3, 5]).
student('Lisa', 19, informatics, [maths], [3]).
student('Jean', 22, informatics, [discrete_maths], [5]).
student('Rafael', 21, informatics, [uml, discrete_maths], [2, 3]).
student('Catania', 21, antropology, [investigation_methodology], [4]).
student('Xavier', 20, medicine, [cells, pharmacology], [3, 5]).
student('Joan', 20, medicine, [history], [3]).


% a) Imprimir en consola, dado un nombre, la carrera que cursa y su edad, con el formato  "X tiene Y
% años y cursa en la carrera de Z" , siendo X el nombre, Y su edad, y Z la carrera.
% - en caso de que no exista el nombre en la base de conocimientos, imprimir  "Nombre no registrado" .
% b) Imprimir en consola, dado un nombre de carrera, todos los estudiantes de la misma con el formato
% "En la carrera de X, están cursando los estudiantes Nombre1, nombre2, ..., nombre N" , siendo
% X la carrera.
% - en caso de que no exista la asignatura en la base de conocimientos, imprimir  "Carrera no
% registrada" .
% c) Imprimir en consola, dado un nombre de estudiante, las notas de cada una de las asignaturas con
% el formato  "X: Asignatura1 - Nota 1, Asignatura 2 - Nota 2, ..., AsignaturaN - NotaN" .
% - en caso de que no exista el nombre en la base de conocimientos, imprimir  "Nombre no registrado" .
% d) Imprimir en consola el promedio de notas de todos los estudiantes en la base de conocimiento.
% e) Imprimir en consola, dado un nombre de estudiante, el promedio de sus notas.
% - en caso de que no exista el nombre en la base de conocimientos, imprimir  "Nombre no registrado" 

% Verificar si un estudiante existe
student_exists(Name) :-
    student(Name, _, _, _, _).

% a) Imprimir información del estudiante (nombre, edad, carrera)
print_student(Name) :-
    \+ student_exists(Name),
    write("Nombre no registrado"), nl.
print_student(Name) :-
    student(Name, Age, Career, _, _),
    write(Name), write(" tiene "), write(Age), write(" años y cursa en la carrera de "), write(Career), nl.

% Verificar si una carrera existe
career_exists(Career) :-
    student(_, _, Career, _, _).

% Encontrar todos los estudiantes de una carrera
find_students_by_career(Career, Students) :-
    findall(Name, student(Name, _, Career, _, _), Students).

% b) Imprimir estudiantes de una carrera
print_students_by_career(Career) :-
    \+ career_exists(Career),
    write("Carrera no registrada"), nl.
print_students_by_career(Career) :-
    find_students_by_career(Career, []),
    write("No se han registrado estudiantes en la carrera de "), write(Career), nl.
print_students_by_career(Career) :-
    find_students_by_career(Career, Students),
    length(Students, N),
    N > 0,
    write("En la carrera de "), write(Career), write(", están cursando los estudiantes "),
    print_names_list(Students), nl.

% c) Imprimir notas de un estudiante

print_notes([], []).
print_notes([Matter], [Note]) :-
    write(Matter), write(" - "), write(Note).
print_notes([Matter|Rest], [Note|RestNotes]) :-
    write(Matter), write(" - "), write(Note),
    print_notes(Rest, RestNotes).

print_student_notes(Name) :-
    \+ student_exists(Name),
    write("Nombre no registrado"), nl.
print_student_notes(Name) :-
    student(Name, _, _, Matters, Notes),
    length(Matters, N),
    N > 0,
    write(Name), write(": "), print_notes(Matters, Notes), nl.

% d) Imprimir los promedios de notas de todos los estudiantes

% -----------------------------
% Helpers para promedios
% -----------------------------

% suma los elementos de una lista de números
sum_list([], Sum, Sum).
sum_list([H|T], Sum, NewSum) :-
    NewSum is H + Sum,
    sum_list(T, NewSum, Sum).

sum_list(List, Sum) :-
    sum_list(List, 0, Sum).

% aplanar (flatten) lista de listas de notas en una sola lista
flatten_notes([], []).
flatten_notes([L|Ls], Flat) :-
    flatten_notes(Ls, FlatTail),
    append(L, FlatTail, Flat).

average(List, Avg) :-
    sum_list(List, Sum),
    length(List, Len),
    Avg is Sum / Len.

% e) Promedio de un estudiante (por nombre)
print_student_average(Name) :-
    \+ student_exists(Name),
    write("Nombre no registrado"), nl.
print_student_average(Name) :-
    student(Name, _, _, _, Notes),
    length(Notes, N),
    N > 0,
    average(Notes, Avg),
    write(Name), write(" tiene promedio: "), write(Avg), nl.

% d) Promedio de todas las notas de todos los estudiantes
print_all_students_average :-
    findall(Notes, student(_, _, _, _, Notes), ListOfLists),
    flatten_notes(ListOfLists, AllNotes),
    ( AllNotes == [] ->
        write("No hay notas registradas"), nl
    ;
        average(AllNotes, Avg),
        write("Promedio de todos los estudiantes: "), write(Avg), nl
    ).


% Ejemplos de uso (consultas):
% ?- print_student_average('Juan').
% ?- print_all_students_average.

% Ejercicio 4
% Se necesita realizar una aplicación de consola para trabajar con números de la serie de Fibonacci,
% cuyos requisitos funcionales son:
% a) Imprima en consola, dado un número n, todos los números de la
% serie hasta ese número sin incluirlo y con el formato  (a0, a1, ...,
% an-1) ,
% b) Imprima en consola, dado un número n, la suma de todos los
% números de la serie hasta ese número incluyéndolo y con el formato
% (a0, a1, ..., an-1) ,
% c) Imprima en consola, dado dos números n y k, todos los números
% de la serie, entre esos dos valores.
% d) Imprima en consola, dado un n valor, la proporción dorada o
% aurea que representa a esa posición en la serie.
% Nota: la proporción aurea se obtiene dividiendo el elemento actual
% entre el anterior en la serie de Fibonacci, es aproximadamente 1.618.


% Print all fibonacci numbers up to n - 1

% Fibonacci: F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
calc_fib(0, 0).
calc_fib(1, 1).
calc_fib(N, Fib) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    calc_fib(N1, F1),
    calc_fib(N2, F2),
    Fib is F1 + F2.

% Auxiliar para imprimir números de Fibonacci desde I hasta Max
aux_fib(I, Max) :-
    I > Max.
aux_fib(I, Max) :-
    I =< Max,
    calc_fib(I, FibAcc),
    write(FibAcc),
    ( I < Max -> write(", ") ; true ),
    I1 is I + 1,
    aux_fib(I1, Max).

% a) Imprimir números de Fibonacci hasta n-1
print_fib(N) :-
    N > 0,
    MaxIndex is N - 1,
    write("("),
    aux_fib(0, MaxIndex),
    write(")"), nl.
print_fib(N) :-
    N =< 0,
    write("("), write(")"), nl.

% b) Suma de todos los números de Fibonacci hasta n (incluyéndolo)
sum_fibonacci(N, Sum) :-
    sum_fibonacci_aux(0, N, 0, Sum).

% Caso base: cuando terminamos (I > N)
sum_fibonacci_aux(I, N, Acc, Sum) :-
    I > N,
    Sum = Acc.

% Caso recursivo: mientras I <= N
sum_fibonacci_aux(I, N, Acc, Sum) :-
    I =< N,
    calc_fib(I, F),
    NewAcc is Acc + F,
    I1 is I + 1,
    sum_fibonacci_aux(I1, N, NewAcc, Sum).

% Imprimir suma de Fibonacci hasta n
print_sum_fib(N) :-
    sum_fibonacci(N, Sum),
    write("("),
    aux_fib(0, N),
    write(") = "), write(Sum), nl.

% c) Imprimir todos los números de Fibonacci entre N y K
print_fib_between(N, K) :-
    N > K,
    write("N debe ser menor o igual que K"), nl.
print_fib_between(N, K) :-
    N =< K,
    write("("),
    aux_fib_between(N, K),
    write(")"), nl.

% Auxiliar para imprimir Fibonacci entre N y K
aux_fib_between(I, Max) :-
    I > Max.
aux_fib_between(I, Max) :-
    I =< Max,
    calc_fib(I, FibAcc),
    write(FibAcc),
    ( I < Max -> write(", ") ; true ),
    I1 is I + 1,
    aux_fib_between(I1, Max).

% d) Proporción áurea (golden ratio) en posición n
% La proporción áurea es F(n) / F(n-1) cuando n > 0
print_golden_ratio(N) :-
    N =< 0,
    write("N debe ser mayor que 0"), nl.
print_golden_ratio(N) :-
    N > 0,
    calc_fib(N, Fn),
    N1 is N - 1,
    calc_fib(N1, Fn1),
    ( Fn1 =:= 0 ->
        write("No se puede calcular la proporción áurea para n=1"), nl
    ;
        Ratio is Fn / Fn1,
        write("Proporción áurea en posición "), write(N), write(": "), write(Ratio), nl
    ).

