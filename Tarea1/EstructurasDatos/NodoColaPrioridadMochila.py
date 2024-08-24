class NodoColaPrioridadMochila():
    def __init__(self, estado,  pesoAcumulado, valorAcumulado, capacidad) -> None:
        self.pesoAcumulado = pesoAcumulado
        self.valorAcumulado = valorAcumulado
        self.estado = estado
        self.capacidad = capacidad 
        self.valorHeuristica = self.heuristica(self.pesoAcumulado, self.valorAcumulado)
    def heuristica(self, pesoTotal, costoTotal):
        return costoTotal - (pesoTotal/self.capacidad)
    def __str__(self) -> str:
        return str(self.costoAcumulado) + ' -> ' + str(self.nodo.nombre)