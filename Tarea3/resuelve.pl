leer_cnf(File, Clauses) :-
    open(File, read, Stream),
    leer_clausulas(Stream, Clauses),
    close(Stream).

leer_clausulas(Stream, Clauses) :-
    read_line_to_string(Stream, Line), % Leer línea como string
    writeln(Line), % Añadir esta línea para imprimir cada línea
    ( Line == end_of_file -> Clauses = [] ;
      ( sub_string(Line, 0, _, _, "c") -> % Ignorar comentarios
        leer_clausulas(Stream, Clauses)
      ; sub_string(Line, 0, _, _, "p") -> % Ignorar encabezado
        leer_clausulas(Stream, Clauses)
      ; split_string(Line, " ", " ", LiteralsString), % Separar los literales
        maplist(atom_number, LiteralsString, Literals), % Convertir a números
        eliminar_ceros(Literals, Clause), % Eliminar el 0 al final de cada cláusula
        leer_clausulas(Stream, Rest),
        Clauses = [Clause | Rest]
      )
    ).

eliminar_ceros([0 | _], []).  % Si hay un cero al final, lo eliminamos
eliminar_ceros([X | Xs], [X | Ys]) :- eliminar_ceros(Xs, Ys).  % De lo contrario, los dejamos

% --- DPLL ---
resolver(File) :-
    leer_cnf(File, Clauses),
    dpll(Clauses, [], Resultado),
    (Resultado == sat -> write('SATISFIABLE'), nl;
     Resultado == unsat -> write('UNSATISFIABLE'), nl).

% --- Algoritmo DPLL ---
dpll([], _, sat). % Si no quedan más cláusulas, es SAT
dpll(Clauses, Asignaciones, Resultado) :-
    (hay_clausula_vacia(Clauses) -> Resultado = unsat ; % Si hay una cláusula vacía, es UNSAT
    seleccion_literal(Clauses, Literal), % Seleccionar un literal
    simplificar(Clauses, Literal, NewClauses), % Simplificar cláusulas
    dpll(NewClauses, [Literal | Asignaciones], Resultado)).

seleccion_literal([[Lit | _] | _], Lit). % Selecciona el primer literal

simplificar([], _, []). % Simplificación de cláusulas
simplificar([Clause | Clauses], Lit, NewClauses) :-
    (member(Lit, Clause) -> NewClauses = Rest ;
    eliminar_literal(-Lit, Clause, SimplifiedClause),
    (SimplifiedClause == [] -> NewClauses = [] ; NewClauses = [SimplifiedClause | Rest])),
    simplificar(Clauses, Lit, Rest).

eliminar_literal(_, [], []). % Eliminar literal de una cláusula
eliminar_literal(Lit, [X | Xs], Ys) :-
    (X == Lit -> Ys = Zs ; Ys = [X | Zs]),
    eliminar_literal(Lit, Xs, Zs).

hay_clausula_vacia([[] | _]). % Verifica si hay cláusulas vacías
hay_clausula_vacia([_ | Clauses]) :-
    hay_clausula_vacia(Clauses).

% --- Ejecución del algoritmo con el DIMACS ---
?- resolver('D:/maestria/AI/Tarea3/CBS_k3_n100_m403_b10_37.cnf').

