% Factorial program with automatic output

factorial(0, 1).
factorial(N, F) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, F1),
    F is N * F1.

% Main entry point to run automatically
:- initialization(main).

main :-
    factorial(5, F),
    format('Factorial of 5 is ~w~n', [F]),
    halt.