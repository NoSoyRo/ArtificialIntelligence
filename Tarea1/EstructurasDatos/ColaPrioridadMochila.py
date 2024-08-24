

from EstructurasDatos.NodoColaPrioridadMochila import NodoColaPrioridadMochila
from EstructurasDatos.Nodo import Nodo
from EstructurasDatos.Ayudante import Ayudante


class ColaPrioridadMochila():
    def __init__(self, pesos, valores, capacidad) -> None:
        self.cola = [] # lista de elementos tipo nodocolaprioridadmochila
        self.pesos = pesos
        self.valores = valores
        self.capacidad = capacidad
    def extraeCabeza(self):
        if len(self.cola)==0:
            return -2
        return self.cola.pop(0)
    def esVacia(self):
        val = len(self.cola) == 0
        return val
    def agrega(self, nodoActual: Nodo):
        if self.esVacia():
            pesoTotal, costoTotal = Ayudante.productoPunto(nodoActual, self.pesos), Ayudante.productoPunto(nodoActual, self.valores)
            nodoColaPrioridadActual = NodoColaPrioridadMochila(nodoActual, pesoTotal, costoTotal, self.capacidad)
            self.cola.append(nodoColaPrioridadActual)
            return
        pesoTotal, costoTotal = Ayudante.productoPunto(nodoActual, self.pesos), Ayudante.productoPunto(nodoActual, self.valores)
        nodoColaPrioridadActual = NodoColaPrioridadMochila(nodoActual, pesoTotal, costoTotal, self.capacidad)
        for elemento in self.cola:
            if elemento.valorHeuristica < nodoColaPrioridadActual.valorHeuristica:
                self.cola.insert(self.cola.index(elemento), nodoColaPrioridadActual)
                return
        self.cola.append(nodoColaPrioridadActual)  
    