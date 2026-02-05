

%(1) For below facts, rules, and goals write English Meanings.
%(1) color(carrots, orange).
%(2) likes(Person, carrots):-vegetarian(Person).
%(3) pass(Student) :- study_hard(Student).
%(4) ?- pass(Who).
%(5) ?- teaches(professor, Course).
%(6) enemies(X, Y) :- hates(X, Y), fights(X, Y).

% 1 - The color of carrots is orange.
% 2 - A person likes carrots if that person is vegetarian.
% 3 - A student pass if he study hard.
% 4 - Who passes? 
% 5 - Who is the professor who teaches this course?
% 6 - Is a enemy X of y (are) if they hate each other and fight each other.

%(2) For below english sentences write applicable Prolog facts, rules & goals.
%(1) Maria reads logic programming book by author peter lucas.
%(2) Anyone likes shopping if she is a girl.
%(3) Who likes shopping?
%(4) kirke hates any city if it is big and crowdy

% 1 - reads(Maria) :- Book(LogicProgrammingBook, PeterLucas).
% 2 - likesShopping(X) :- isAGirl(X).
% 3 - ?- likesShopping(Who).
% 4 - hatesCity(Kirke, City) :- isBigAndCrowdy(City)

% a) Write a simple prolog program that computes cube for the number.
%  
% (3.b) Try to read number from the query prompt and find cube.

computes_cube(0, 0).
computes_cube(1, 1).

computes_cube(N, Cube) :-

    Cube is N * N * N,
    write('The cube of '), write(N), write(' is '), write(Cube), nl,
    !.

read_and_compute_cube :-
    write('Enter a number: '),
    read(N),
    computes_cube(N, Cube),
    write('The cube of '), write(N), write(' is '), write(Cube), nl,
    !.


% (4) Find flaws in following clauses.
% (1) hates(X,Y), hates(Y,X) :- enemies(X, Y)
% (2) p(X):-(q(X):-r(X)).

% 1 - enemies(X, Y) :- hates(X,Y), hates(Y,X).
% 2 - p(X) :- q(X), r(X).

% (5) For given English statements write a prolog program.
% - Facts & Rules
% (1) jia is a woman. woman(Jia)
% (2) john is a man. man(John)
% (3) john is healthy. healthy(John)
% (4) jia is healthy. healthy(Jia)
% (5) john is wealthy. wealthy(John)
% (6) anyone is a traveler if he is healthy and wealthy. traveler(X) :- healthy(X), wealthy(X).
% (7) anyone can travel if he is a traveler. can_travel(X) :- traveler(X).
% - Goals.
% (1) Who can travel? ?- can_travel(Who).
% (2) Who is healthy and wealthy? ?- healthy(Who), wealthy(Who).

% 6) What answers do you get for below queries for given program.
% Program :
%      vegetarian(jose).  
%   vegetarian(james).  
%   vegetable(carrot).  
%   vegetable(egg_plant).  
%   likes(jose, X) :- vegetable(X).  
%   loves(Who, egg_plant) :- vegetarian(Who).
% Queries :
%     ?- vegetable(X).
%   ?- vegetable(potato).
%   ?- vegetarian(_).
%   ?- likes(jose, What).
%   ?- likes(Who, egg_plant).
%   ?- loves(Who, egg_plant).

% (1) Write english meaning for below prolog clause. 
% likes(mary, john); likes(john, mary). Mary likes John or John likes Mary.
% 
% (2) How would you break this into two clauses? 
% likes(X,Y):-likes(mary, john); likes(john, mary). 

% likes(X, Y) :- likes(mary, john).
% likes(X, Y) :- likes(john, mary).


% Assume given a set of facts of the form father(name1,name2) (name1 is the father of name2).
% Define a predicate brother(X,Y) which holds iff X and Y are brothers.
% Define a predicate cousin(X,Y) which holds iff X and Y are cousins.
% Define a predicate grandson(X,Y) which holds iff X is a grandson of Y.
% Define a predicate descendent(X,Y) which holds iff X is a descendent of Y.

brother(X, Y) :-
    father(F, X),
    father(F, Y),
    X \= Y.

cousin(X, Y) :-
    father(F1, X),
    father(F2, X),
    brothers(F1, F2),
    F1 \= F2.    

grandson(X, Y) :-
    father(F, X),
    father(Y, F).

% descendent(X, Y) :-
%     father(Y, X);
%     grandson(X, Y);
%     cousin(CousinOfX, X), father(Y, CousinOfX).

descendent(X,Y) :- father(Y,X).                        % 9
   descendent(X,Y) :- father(Z,X), descendent(Z,Y).    

% Define a predicate reverse(L,K) which holds if and only if the list K is the reverse of the list L.

fast_reverse(L, R) :- fast_reverse(L, [], R).
fast_reverse([], Acc, Acc).
fast_reverse([H|T], Acc, R) :- fast_reverse(T, [H|Acc], R).

% Consider a representation of sets as lists. Define the following predicates:
% member(X,L), which holds iff the element X occurs in L.
% subset(L,K), which holds iff L is a subset of K.
% disjoint(L,K), which holds iff L and K are disjoint (i.e. they have no elements in common).
% union(L,K,M), which holds iff M is the union of L and K.
% intersection(L,K,M), which holds iff M is the intersection of L and K.
% difference(L,K,M), which holds iff M is the difference of L and K.
% Note that the solution to these exercises depends on the way you decide to represent sets. There are various possibilities:
% lists with possible repetitions of the same element
% lists without repetitions
% (in case of lists of integers) ordered lists
% For each of these representation, give your solution to the above problems.

% WITH REPETITIONS

redefined_member(X, [X|_]).
redefined_member(X, [_|T]) :- redefined_member(X, T).

redefined_subset([], _).
redefined_subset([H|T], K) :- redefined_member(H, K), redefined_subset(T, K).

redefined_disjoint([], _).
redefined_disjoint([H|T, K]) :- not(redefined_member(H, K)) :- redefined_disjoint(T, K).

is_union([], K, K).
is_union(K, [], K).

is_union([H|T], K, [H|Union]) :- is_union(T, K, Union).
is_union(T, [H|K], [H, Union]) , is_union(T, K, Union).

intersection([],_,[]).
% If x is in the first set and not in the second, dont include it in the intersection
intersection([X|L],K,M) :- not(member(X,K)), intersection(L,K,M).
intersection([X|L],K,[X|M]) :- member(X,K), intersection(L,K,M).

difference([],_,[]).
% If x is in both sets, dont include it in the difference
difference([X|L],K,M) :- member(X,K), difference(L,K,M).
% include it
difference([X|L],K,[X|M]) :- not(member(X,K)), difference(L,K,M).

% WITHOUT REPETITIONS

is_union([], K, K).
is_union(K, [], K).

is_union([H|T], K, [H|Union]) :- not(redefined_member(H, K)), is_union(T, K, Union).
is_union(T, [H|K], [H|Union]) :- not(redefined_member(H, T)), is_union(T, K, Union).
is_union(T, [H|K], Union) :- redefined_member(H, T), is_union(T, K, Union).


% WITH ORDERED LISTS (ascending)

redefined_union(X, K, m) :- ordered_merge(X, K, M).

ordered_merge([], K, K).
ordered_merge(K, [], K).
ordered_merge([H1|T1], [H2|T2], [H1|M]) :- H1 < H2, ordered_merge(T1, [H2|T2], M).
ordered_merge([H1|T1], [H2|T2], [H2|M]) :- H1 > H2, ordered_merge([H1|T1], T2, M).
ordered_merge([H1,T1], [H2, T2], M) :- H1 =:= H2, ordered_merge(T1, T2, M).

% Define a predicate length(L,N) which holds iff N is the length of the list L.

length([], 0).
length([_| T], N) :- length(T, N1), N is N1 + 1.

% Define a predicate occurrences(X,L,N) which holds iff the element X occurs N times in the list L.

occurrences(_, [], 0).
occurrences(X, [X|T], N) :- occurrences(X, T, N1), N is N1 + 1.
occurrences(X, [Y|T], N) :- X \= Y, occurrences(X, T, N).

% Define a predicate occurs(L,N,X) which holds iff X is the element occurring in position N of the list L.

occurs([H|_], 1, H).
% start from the back of the list, decrementing N until it reaches 1
occurs([_, T], N, X) :- N > 1, N1 is N - 1, occurs(T, N1, X).

% Define a predicate sumlist(L,N) which, given a list of integers L, returns the sum N of all the elements of L.

sumlist([], 0).
sumlist([H|T], N) :- sumlist(T, N1), N is N1 + H.

