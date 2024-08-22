from EstructurasDatos.Nodo import Nodo
from EstructurasDatos.NodoColaPrioridad import NodoColaPrioridad

# TO-DO: ColaPrioridadBusquedaVoraz (considera heuristicas)

class ColaPrioridad():
    def __init__(self, arcos: dict) -> None:
        self.cola = []
        self.arcos = arcos
    def extraeCabeza(self):
        if len(self.cola)==0:
            return -2
        auxiliar = self.cola[0]
        return self.cola.pop(0)
    def esVacia(self):
        val = len(self.cola) == 0
        return val
    def agrega(self, nodoHijo: Nodo, nodoActual: Nodo, costoActual: int):
        costo = self.busquedaCostoArco(nodoActual, nodoHijo)
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
    def busquedaCostoArco(self, nodoInicial, nodoFinal):
        costo = self.arcos[(nodoInicial, nodoFinal)]
        if costo == None:
            return -1
        return costo

