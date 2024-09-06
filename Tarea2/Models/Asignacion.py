class Asignaciones():
    def __init__(self) -> None: # No lo agrego al construc tor porque este metodo de asignaciones solamente cambia el valor que ya existe.
        self.asignaciones = set()

    # ESTO ES SOLO CODIGO QUE TIENE QUE VER CON LA ASIGNACION DEL MODELADO DEL PROBLEMA DE N REINAS
    def agrega(self, variablePorAgregar, variables):
        if self.asignaciones != set():
            self.asignaciones.add(variablePorAgregar) ## Ojo la variable ya debe traer el valor asignado != nulo
            return
        for variable in variables:
            self.agregaRestriccion(variablePorAgregar, variable)
        self.asignaciones.add(variablePorAgregar)
        
    def agregaRestriccion(self, variablePorAgregar, variable):
        # Horizontal
        variable.valoresAdmisibles.remove(variablePorAgregar.valor)
        a = abs(variable.columna - variablePorAgregar.columna)
        # Diagonales encima
        if variable.valor + a <= variable.columna: 
            variable.restricciones.add(variable.valor + a)
        # Diagonales debajo
        if variable.valor - a > 0: 
            variable.restricciones.add(variable.valor + a)
        variable.creaValoresAdmisibles()


    def elimina(self, variablePorEliminar, variables):
        if self.asignaciones != set():
            self.asignaciones.add(variablePorEliminar) ## Ojo la variable ya debe traer el valor asignado != nulo
            return
        for variable in variables:
            self.eliminaRestriccion(variablePorEliminar, variable)
        self.asignaciones.remove(variablePorEliminar)
    
    def eliminaRestriccion(variablePorEliminar, variable):
        # Horizontal
        variable.valoresAdmisibles.remove(variablePorEliminar.valor)
        a = abs(variable.columna - variablePorEliminar.columna)
        # Diagonales encima
        if variable.valor + a <= variable.columna: 
            variable.restricciones.pop(variable.valor + a)
        # Diagonales debajo
        if variable.valor - a > 0: 
            variable.restricciones.pop(variable.valor + a)
        variable.creaValoresAdmisibles()
    # AQUI TERMINA

