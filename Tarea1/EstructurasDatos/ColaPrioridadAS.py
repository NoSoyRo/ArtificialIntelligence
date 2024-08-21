from EstructurasDatos.Nodo import Nodo
from EstructurasDatos.NodoColaPrioridad import NodoColaPrioridad
from EstructurasDatos.ColaPrioridadVoraz import ColaPrioridadVoraz

class ColaPrioridadAS(ColaPrioridadVoraz):
    def __init__(self, arcos: dict, heuristica: dict) -> None:
        super().__init__(arcos, heuristica) 
    def agregaAS(self, nodoHijo: Nodo, nodoActual: Nodo, costoActual: int):

        costo = self.busquedaAS(nodoActual, nodoHijo, nodoHijo)

        self.cuentaCostoCaminoActual = costoActual
        if len(self.cola) == 0:
            nodoColaPrioridadNodoHijo = NodoColaPrioridad(costo, nodoHijo)
            self.cola.append(nodoColaPrioridadNodoHijo)
            return
        # siempre existe
        costoCompleto = costo + costoActual
        nodoColaPrioridadNodoHijo = NodoColaPrioridad(costoCompleto, nodoHijo) # Creamos nodo con especificaciones correctas
        for elemento in self.cola:
            if elemento.costoAcumulado > nodoColaPrioridadNodoHijo.costoAcumulado:
                self.cola.insert(self.cola.index(elemento), nodoColaPrioridadNodoHijo)
                return
        self.cola.append(nodoColaPrioridadNodoHijo)


    def busquedaAS(self, nodoInicial, nodoFinal, nodoActual):
        costo1 = self.busquedaHeuristica(nodoActual)
        costo2 = self.busquedaCostoArco(nodoInicial, nodoFinal)
        return costo1 + costo2
