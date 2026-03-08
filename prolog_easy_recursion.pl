% 1. last(L,X). where X is the last element from the list L.

% 2. member(X,L). X is an element of the list L.

% 3. append(L1,L2,L3). L3 is the list L1 followed by the list L2.

% 4. length(L,N). N is the number of elements in the list L.

% 5. reverse(L,K). K is the list L with its elements in reverse order.

% 6. nth(N,L,X). X is the element at position N in the list L (1-based).

% 7. sumlist(L,N). L is a list of numbers; N is the sum of all elements in L.


last([H], H).
last([_|T], X) :- last(T, X).

member(X, [X|_]).
member(X, [_|T]) :- member(X, T).

append([], L, L).
append([H|T], L, [H|R]) :- append(T, L, R).

length([], 0).
length([_|T], N) :- length(T, N1), N is N1 + 1.

reverse([], []).
reverse([H|T], R) :- reverse(T, R1), append(R1, [H], R).

nth(1, [H|_], H).
nth(N, [_|T], X) :- N > 1, N1 is N - 1, nth(N1, T, X).