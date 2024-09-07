class Asignaciones():
    def __init__(self) -> None: # No lo agrego al construc tor porque este metodo de asignaciones solamente cambia el valor que ya existe.
        self.asignaciones = set()

    # ESTO ES SOLO CODIGO QUE TIENE QUE VER CON LA ASIGNACION DEL MODELADO DEL PROBLEMA DE N REINAS
    def agrega(self, variablePorAgregar, variables: list):
        for variable in variables:
            if variable != variablePorAgregar:
                self.agregaRestriccion(variablePorAgregar, variable)
        self.asignaciones.add(variablePorAgregar)
        
    def agregaRestriccion(self, variablePorAgregar, variable):
        # Horizontal
        variable.restricciones.add(variablePorAgregar.valor)
        a = abs(variable.columna - variablePorAgregar.columna)
        # Diagonales encima
        aux = variablePorAgregar.valor + a <= variable.tamanioTablero
        if aux: 
            variable.restricciones.add(variablePorAgregar.valor + a)
        # Diagonales debajo
        if variablePorAgregar.valor - a > 0: 
            variable.restricciones.add(variablePorAgregar.valor - a)
        # No te olvides que al terminar actualizar los valores admisibles porque actualizaste restricciones y solo debes calcyular D - Restricciones uvu
        variable.creaValoresAdmisibles()


    def elimina(self, variablePorEliminar, variables):
        for variable in variables:
            self.eliminaRestriccion(variablePorEliminar, variable)
        self.asignaciones.remove(variablePorEliminar)
        for i in self.asignaciones:
            self.agrega(i, variables)
        print("checkpoint")
    
    def eliminaRestriccion(self, variablePorEliminar, variable):
        # Horizontal
        variable.restricciones.remove(variablePorEliminar.valor)
        a = abs(variable.columna - variablePorEliminar.columna)
        # Diagonales encima
        aux = variablePorEliminar.valor + a <= variable.tamanioTablero
        if aux: 
            variable.restricciones.remove(variablePorEliminar.valor + a)
        # Diagonales debajo
        if variablePorEliminar.valor - a > 0: 
            variable.restricciones.remove(variablePorEliminar.valor - a)
        # No te olvides que al terminar actualizar los valores admisibles porque actualizaste restricciones y solo debes calcyular D - Restricciones uvu
        variable.creaValoresAdmisibles()
    # AQUI TERMINA

    def __str__(self) -> str:
        string = ''
        for i in self.asignaciones:
            string += '|' + str(i.valor) + '-' + str(i.columna) + '|'
        return(string)

