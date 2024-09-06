# Las asignaciones son un set que tiene variables con valor neq nulo
class BusquedaCSP():
    def __init__(self, csp, asignacion) -> None:
        self.csp = csp
        self.asignacion = asignacion # instancia del objeto asignacion
    def busquedaBackTrack(self):
        return self.backtrack()
    def backtrack(self):
        if self.esAsignacionCompleta(): return self.asignacion
        nuevaVariable = self.seleccionaVariableInasignada()
        for valor in self.valoresAdmisiblesOrdenados(nuevaVariable): 
            # preguntar si el valor tiene que ser sobre el total de restricciones o sobre las restricciones restantes,
            # si es con las restricciones restantes, entonces siempre la eleccion será consistente
            nuevaVariable.valor = valor
            self.asignacion.agrega(nuevaVariable, self.csp.variables)
            if self.infiere(): # esto solo significa revisa que para toda variable inasignada exista un valor en cada dominio
                               # que hace que este camino sea consistente, sino, lo volamos y nos regresamos 
                resultado = self.backtrack()
                if resultado != -1:
                    return resultado
                    # remueve inferencias de csp falta esto <---
                # remueve variable de asignacion 
                self.asignacion.elimina(nuevaVariable, self.csp.variables) # recuerda que variables es un set de Variable
                return -1
            self.asignacion.elimina(nuevaVariable, self.csp.variables)
            return -1


    def esAsignacionCompleta(self):
        return len(self.asignacion) == len(self.csp.variables)
    def seleccionaVariableInasignada(self):
        self.inasignadas = self.csp.variables - self.asignacion
        nMinValoresAdmisibles = float('inf')
        mejorVariable = None
        for variable in self.inasignadas:
            if nMinValoresAdmisibles >= len(variable.valoresAdmisibles):
                mejorVariable = variable
                nMinValoresAdmisibles = len(variable.valoresAdmisibles)
        return mejorVariable
    def valoresDominioOrdenado(self, nuevaVariable):
        # Ya esta asignado el self.inasignado
        # Uso una lista porque me interesa el orden
        dictAux = {}
        for valor in nuevaVariable.dominio:
            auxConjunto = set(valor)
            cuentaAux = 0 
            for variableInasignada in self.inasignadas:
                if auxConjunto.intersection(variableInasignada.restricciones):
                    cuentaAux+=1
            dictAux[valor] = cuentaAux
        dominioOrdenado = list(sorted(dictAux.items(), key=lambda item: item[1]))
        return dominioOrdenado
    
    def valoresAdmisiblesOrdenados(self, nuevaVariable):
        dictAux = {}
        for valor in nuevaVariable.valoresAdmisibles:
            auxConjunto = set(valor)
            cuentaAux = 0 
            for variableInasignada in self.inasignadas:
                if auxConjunto.intersection(variableInasignada.restricciones):
                    cuentaAux+=1
            dictAux[valor] = cuentaAux
        dominioOrdenado = list(sorted(dictAux.items(), key=lambda item: item[1]))
        return dominioOrdenado


    def esConsistente(self):
        # TO-DO: si necesitas puedes hacer mas compleja esta decision
        return True
    
    def infiere(self):
        # TO-DO: temrina esta implementacion
        return
