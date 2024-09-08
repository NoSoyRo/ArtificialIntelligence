class AsignacionesColoreado():
    def __init__(self) -> None: # No lo agrego al construc tor porque este metodo de asignaciones solamente cambia el valor que ya existe.
        self.asignaciones = set()

    # ESTO ES SOLO CODIGO QUE TIENE QUE VER CON LA ASIGNACION DEL MODELADO DEL PROBLEMA DE N REINAS
    def agrega(self, variablePorAgregar, variables):
        for variable in variablePorAgregar.vecinos:
            if variable != variablePorAgregar:
                self.agregaRestriccion(variablePorAgregar.color, variables[variable])
        self.asignaciones.add(variablePorAgregar)
        
    def agregaRestriccion(self, color, variable):
        variable.restricciones.append(color)
        # No te olvides que al terminar actualizar los valores admisibles porque actualizaste restricciones y solo debes calcyular D - Restricciones uvu
        variable.creaValoresAdmisiblesExistentes()

    def elimina(self, variablePorEliminar, variables):
        for variable in variablePorEliminar.vecinos:
            self.eliminaRestriccion(variablePorEliminar.color, variables[variable])
        self.asignaciones.remove(variablePorEliminar)
        for i in self.asignaciones:
            self.agrega(i)
        print("checkpoint")
    
    def eliminaRestriccion(self, color, variable):
        variable.restricciones.remove(color)
        # No te olvides que al terminar actualizar los valores admisibles porque actualizaste restricciones y solo debes calcyular D - Restricciones uvu
        variable.creaValoresAdmisiblesExistentes()
    # AQUI TERMINA

    def __str__(self) -> str:
        coloresNecesarios = len(list(self.asignaciones)[0].dominioComunColores)
        string = str(coloresNecesarios) + '\n'
        for i in self.asignaciones:
            string += '|' + str(i.region) + '-' + str(i.color) + '|' + '\n'
        return(string)
