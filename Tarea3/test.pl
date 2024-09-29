% --- Leer el archivo CNF ---
leer_cnf(File, Clauses) :-
    open(File, read, Stream),
    leer_clausulas(Stream, Clauses),
    close(Stream).

leer_clausulas(Stream, Clauses) :-
    read(Stream, Term),
    ( Term == end_of_file -> Clauses = [] ;
      ( Term = comment(_) -> % Ignorar comentarios
        leer_clausulas(Stream, Clauses) ;
        Term = p(_, _) -> % Ignorar encabezado
        leer_clausulas(Stream, Clauses) ;
        Term = clause(Literals) -> % Leer cláusula
        parsear_clausula(Literals, Clause),
        leer_clausulas(Stream, Rest),
        Clauses = [Clause | Rest]
      )
    ).

% Parsear cláusula
parsear_clausula([], []). % Caso base para cláusulas vacías
parsear_clausula([X|Xs], Clause) :-
    atom_number(X, Lit), % Convertir el literal a número
    (Lit = 0 -> Clause = [] ; % Termina la cláusula con 0
     Clause = [Lit | Rest],
     parsear_clausula(Xs, Rest)).

% --- Ejemplo de ejecución ---
% Para ejecutar, usa la siguiente consulta en la consola de Prolog:
% ?- leer_cnf('D:/maestria/AI/Tarea3/CBS_k3_n100_m403_b10_37.cnf', Clauses).
