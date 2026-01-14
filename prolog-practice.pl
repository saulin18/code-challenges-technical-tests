

% Caso base: si Y es 0, el MCD es X
mcd(X, 0, X).

% Caso recursivo: si Y no es 0, calculamos MCD(Y, X mod Y)
mcd(X, Y, MCD) :-
    Y > 0,
    Resto is X mod Y,
    mcd(Y, Resto, MCD).

% 5. Dada la función de 2 variables de Ackerman (Ejemplo 5.1.1 p. 265 de 
% Johnsonbaugh) definida como: 
% A(0,n)= n+1 para n=0,1, 2, … 
% A(m,0)= A(m-1,1) para m=1, 2, … 
% A(m,n)= A(m-1, A(m,n-1)) para m=1, 2, …; n= m=1, 2, … 
%  
% a) Escriba el pseudocódigo (o código en Java, C, C++ o Pascal) que permita 
% obtener el valor A(M,N) para dos valores M y N que se reciban. 
% b) Describa la traza de la misma para M=2, N=2. 
% c) Escriba en Prolog un predicado a(M,N) que permita obtener el valor A(M,N) para 
% dos valores M y N que se reciban

A(0, N, Result) :-
    Result is N + 1.

A(M, 0, Result) :-
    M > 0,
    M1 is M - 1,
    A(M1, 1, Result).

A(M, N, Result) :-
    M > 0, 
    N > 0, 
    M1 is M - 1, 
    N1 is N - 1, 
 %   A(M, A(M, N1, TempResult), Result). % wrong, should be A(M1, TempResult, Result), in prolog we cant have nested calls like that
    A(M, N1, TempResult),
    A(M, TempResult, Result)


% 6. Dadas las siguientes relaciones que permiten describen la complejidad temporal 
% de algunos algoritmos en el peor caso. 
% 6.1. Búsqueda secuencial: Sn= n    para n≥0 
% 6.2. Búsqueda binaria (p. 289-): S1= 2, Sn= S└n/2┘ +1    para n≥2     

sequential_search(0, 0).
sequential_search(N, S) :-
    N > 0,
    sequential_search(N - 1, S1),
    S is S1 + 1.

binary_search(1, 2).
binary_search(NumberToFind, Left, Right, N) :-
    Left < Right,
    Mid is (Left + Right) // 2,
    (   NumberToFind =:= Mid
    ->  N = 1
    ;   NumberToFind < Mid
    ->  binary_search(NumberToFind, Left, Mid - 1, N1),
        N is N1 + 1
    ;   binary_search(NumberToFind, Mid + 1, Right, N1),
        N is N1 + 1
    ).




