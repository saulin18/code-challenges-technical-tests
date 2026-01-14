set(a, [1, 4, 3, 6, 9, 2, 5]).
set(b, [9, 0, 3, 1, 10, 95, 91, 2]).
set(c, [5, 3, 6, 9, 2, 8]).

% a) Imprima en consola la unión entre los 3 conjuntos.
% b) Imprima en consola la intersección dos de ellos.
% - En caso de resultar en un conjunto vacío o nulo,
% imprimir  “Conjunto nulo” .
% c) Imprima en consola la diferencia entre el primer
% conjunto y el tercer conjunto.
% - En caso de resultar en un conjunto vacío o nulo,
% imprimir  “Conjunto nulo” .
% d) Imprima en consola la diferencia simétrica entre el segundo conjunto y el tercer conjunto.
% - En caso de resultar en un conjunto vacío o nulo, imprimir  “Conjunto nulo” 

union([], [], []).

union([], [H|T], [H|Union]) :-
    union([], T, Union).


union([H|T], [], [H|Union]) :-
    union(T, [], Union).

union([H|T], List2, Union) :-
    member(H, List2),
    union(T, List2, Union).
union([H|T], List2, [H|Union]) :-
    \+member(H, List2),
    union(T, List2, Union).

intersection([], [], []).

intersection(List1, [], []).

intersection([], List2, []).

intersection([H|T], List2, [H|Union]) :-
    member(H, List2),
    intersection(T, List2, Union).

intersection([H|T], List2, Union) :-
    \+member(H, List2),
    intersection(T, List2, Union).

% The difference between two sets is the set of elements that are in the first set but not in the second.

difference([], [], []).

difference(List1, [], List1).

difference([], List2, []).

difference([H|T], List2, [H|Difference]) :-
    \+member(H, List2),
    difference(T, List2, Difference).

difference([H|T], List2, Difference) :-
    member(H, List2),
    difference(T, List2, Difference).


