class BusquedaCSPBackTrackColoreado():
    def __init__(self, csp, asignacion) -> None:
        self.csp = csp
        self.asignacion = asignacion

    def busquedaBackTrack(self):
        return self.backtrack()
    
    def backtrack(self):
        if self.esAsignacionCompleta(): return self.asignacion
        nuevaVariable = self.seleccionaVariableInasignada()
        vAO = self.valoresAdmisiblesOrdenados(nuevaVariable)
        for color in vAO: 
            # preguntar si el valor tiene que ser sobre el total de restricciones o sobre las restricciones restantes,
            # si es con las restricciones restantes, entonces siempre la eleccion será consistente
            self.inasignadas.remove(nuevaVariable) 
            nuevaVariable.color = color
            self.asignacion.agrega(nuevaVariable, self.csp.variables)
            resultado = self.backtrack()
            if resultado != -1:
                return resultado
                    # remueve inferencias de csp falta esto <---
                # remueve variable de asignacion 
            self.asignacion.elimina(nuevaVariable, self.csp.variables) # recuerda que variables es un set de Variable
            self.inasignadas.insert(nuevaVariable.columna, nuevaVariable)
        return -1
    
    def esAsignacionCompleta(self):
        return len(self.asignacion.asignaciones) == len(self.csp.variables)
    
    def seleccionaVariableInasignada(self):
        aux = self.csp.variablesOrdenadas.copy()
        for i in self.asignacion.asignaciones:
            aux.remove(i)
        self.inasignadas = aux
        return self.inasignadas[0]
    
    def valoresAdmisiblesOrdenados(self, nuevaVariable):
        # Ya esta asignado el self.inasignado
        # Uso una lista porque me interesa el orden
        dictAux = {}
        nuevaVariable.creaValoresAdmisiblesExistentes()
        if len(nuevaVariable.valoresAdmisiblesExistentes) == 0:
            if len(nuevaVariable.dominioComunColores) == 0:
                nuevaVariable.dominioComunColores.append(1)
                return [1]
            nuevaVariable.dominioComunColores.append(nuevaVariable.dominioComunColores[-1] + 1)
            return [nuevaVariable.dominioComunColores[-1]]
        for valor in nuevaVariable.valoresAdmisiblesExistentes:
            auxConjunto = set([valor])
            cuentaAux = 0 
            for variableInasignada in self.inasignadas:
                if auxConjunto.intersection(variableInasignada.restricciones):
                    cuentaAux+=1
            dictAux[valor] = cuentaAux
        dominioOrdenado = list(sorted(dictAux.items(), key=lambda item: item[1]))
        return [i[0] for i in dominioOrdenado]