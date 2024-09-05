# Las asignaciones son un set que tiene variables con valor neq nulo
class BusquedaCSP():
    def __init__(self, csp) -> None:
        self.csp = csp
        self.asignacion = set()
    def busquedaBackTrack(self):
        return self.backtrack()
    def backtrack(self):
        if self.esAsignacionCompleta(): return self.asignacion
        nuevaVariable = self.seleccionaVariableInasignada()
        for valor in self.valoresDominioOrdenado():
            if self.esConsistente(valor):
                nuevaVariable.valor = valor
                self.asignacion.add(nuevaVariable)
                inferencias = self.infiere()
                if inferencias != -1: #falla
                    # agrega inferencia a csp falta esto <---
                    resultado = self.backtrack()
                    if resultado != -1:
                        return resultado
                    # remueve inferencias de csp falta esto <---
                # remueve variable de asignacion
            return -1


    def esAsignacionCompleta(self):
        return len(self.asignacion) == len(self.csp.variables)
    def seleccionaVariableInasignada(self):
        self.inasignadas = self.csp.variables - self.asignacion
        nMinValoresAdmisibles = float('inf')
        mejorVariable = None
        for variable in self.inasignadas:
            if nMinValoresAdmisibles > len(variable.valoresAdmisibles):
                mejorVariable = variable
                nMinValoresAdmisibles = len(variable.valoresAdmisibles)
        return mejorVariable
    def valoresDominioOrdenado(self):
        # Ya esta asignado el self.inasignado
        # Uso una lista porque me interesa el orden
        dominioOrdenado = []
        # TO-DO: Terminar de crear este metodo

    def esConsistente(self):
        # TO-DO: temrina esta implementacion
        return
    
    def infiere(self):
        # TO-DO: temrina esta implementacion
        return







