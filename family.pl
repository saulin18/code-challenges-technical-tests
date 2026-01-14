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


persona_existe(Person) :-
    is_parent(_, Person) ; is_parent(Person, _).


imprimir_lista_con_y([Unico]) :-
    write(Unico).

% Two elements list
imprimir_lista_con_y([Primero, Segundo]) :-
    write(Primero), write(' y '), write(Segundo).

% Three or more elements list
imprimir_lista_con_y([Primero, Segundo | Resto]) :-
    write(Primero), write(', '),
    imprimir_lista_con_y([Segundo | Resto]).

 
imprimir_padres(Person) :-
    (persona_existe(Person) ->
        find_parents(Person, [], ParentList),
        (ParentList = [] ->
            write('No se han registrado los padres'), nl
        ;
            length(ParentList, Count),
            write(Person), write(' tiene '), write(Count), write(' padres: '),
            imprimir_lista_con_y(ParentList)
        )
    ;
        write('Nombre no registrado'), nl
    ).

% Recolectar padres en una lista
find_parents(Person, AccList, FinalList) :-
    is_parent(Parent, Person),
    find_parents(Person, [Parent | AccList], FinalList).

find_parents(_, ParentList, ParentList).


imprimir_hijos(Person) :-
    find_children(Person, [], ChildList),
    (ChildList = [] -> 
     write('No se han registrado hijos de esta persona'), nl
    ;
    length(ChildList, Count),
    write(Person), write(' tiene '), write(Count), write(' hijos: '),
    imprimir_lista_con_y(ChildList)
    ).

find_children(Person, AccList, FinalList) :-
    is_parent(Person, Child),
    find_children(Person, [Child | AccList], FinalList).


find_children(_, ChildList, ChildList).

imprimir_abuelos(Person) :-
    find_grandparents(Person, [], GrandparentList),
    (GrandparentList = [] ->
     write('No se han registrado abuelos de esta persona'), nl
    ;
    length(GrandparentList, Count),
    write(Person), write(' tiene '), write(Count), write(' abuelos: '),
    imprimir_lista_con_y(GrandparentList)
    ).

find_grandparents(Person, AccList, FinalList) :-
    is_parent(Parent, Person),
    is_parent(Grandparent, Parent),
    find_grandparents(Person, [Grandparent | AccList], FinalList).


find_grandparents(_, GrandparentList, GrandparentList).

imprimir_hermanos(Person) :-
    find_brothers(Person, [], BrotherList),
    (BrotherList = [] ->
     write('No se han registrado hermanos de esta persona'), nl
    ;
    length(BrotherList, Count),
    write(Person), write(' tiene '), write(Count), write(' hermanos: '),
    imprimir_lista_con_y(BrotherList)
    ).

find_brothers(Person, AccList, FinalList) :-
    is_parent(Parent, Person),
    is_parent(Parent, Brother),
    Brother \= Person,
    \+ member(Brother, AccList),
    find_brothers(Person, [Brother | AccList], FinalList).

find_brothers(_, BrotherList, BrotherList).