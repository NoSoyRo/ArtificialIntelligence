from EstructurasDatos.ColaPrioridad import ColaPrioridad
from EstructurasDatos.Nodo import Nodo
from EstructurasDatos.NodoColaPrioridad import NodoColaPrioridad

class ColaPrioridadVoraz(ColaPrioridad):
    def __init__(self, arcos: dict, heuristica: dict) -> None:
        super().__init__(arcos)
        self.heuristica = heuristica
        self.arcos = arcos
    def extraeCabeza(self):
        if len(self.cola)==0:
            return -2
        auxiliar = self.cola[0]
        return self.cola.pop(0)
    def esVacia(self):
        val = len(self.cola) == 0
        return val
    def agregaVoraz(self, nodoHijo: Nodo):
        costo = self.busquedaHeuristica(nodoHijo)
        if len(self.cola) == 0:
            nodoColaPrioridadNodoHijo = NodoColaPrioridad(costo, nodoHijo)
            self.cola.append(nodoColaPrioridadNodoHijo)
            return
        # siempre existe
        nodoColaPrioridadNodoHijo = NodoColaPrioridad(costo, nodoHijo) # Creamos nodo con especificaciones correctas
        
        for elemento in self.cola:
            if elemento.costoAcumulado > nodoColaPrioridadNodoHijo.costoAcumulado:
                self.cola.insert(self.cola.index(elemento), nodoColaPrioridadNodoHijo)
                return
        self.cola.append(nodoColaPrioridadNodoHijo)   
    def busquedaHeuristica(self, nodoActual):
        distancia = self.heuristica[nodoActual]
        if distancia == None:
            return -1
        return distancia
