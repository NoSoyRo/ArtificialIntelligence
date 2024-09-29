% --- Hechos ---
woman(jia).
man(john).
healthy(john).
healthy(jia).
wealthy(john).

% --- Reglas ---
traveler(X) :- healthy(X), wealthy(X).
can_travel(X) :- traveler(X).

% --- Objetivos ---
% 1. ¿Quién puede viajar?
% Para resolver: can_travel(Who).

% 2. ¿Quién es sano y rico?
% Para resolver: traveler(Who).
