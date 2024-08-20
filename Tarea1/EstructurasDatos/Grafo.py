from EstructurasDatos.ColaPrioridad import ColaPrioridad
from EstructurasDatos.Nodo import Nodo

class Grafo():
    def __init__(self, nodos: list, arcos: dict) -> None:
        self.nodos = nodos
        self.arcos = arcos
        self.frontera = ColaPrioridad(arcos)
    def inicializaFronteraBusquedaCostoUniforme(self, nodoInicial: Nodo):
        for hijo in nodoInicial.expandeHijos():
            nodoActual = self.nodos[self.nodos.index(nodoInicial)]
            hijo.pathAMi.append(nodoInicial.nombre)
            self.frontera.agrega(hijo, nodoActual, 0) # Depende del nodo que se este visitando
    def busquedaCostoUniforme(self, nodoInicial, nodoFinal):
        # Solucion que no solamente guarda el path sino el minimo costo.
        visitados = set()
        self.inicializaFronteraBusquedaCostoUniforme(nodoInicial)
        encontreSolucion = False
        nodoInicial.pathAMi = [nodoInicial.nombre]
        while encontreSolucion == False:
            if self.frontera.esVacia():
                return -1 # Failure code
            nodoActual = self.frontera.extraeCabeza()
            print(nodoActual.nodo.pathAMi)
            # TO-DO agrega la forma de ir guardando el caminito
            if nodoActual.nodo.nombre == nodoFinal.nombre: # cambiar a un objeto.equals(objeto)
                encontreSolucion = True
                return nodoActual.costoAcumulado
            if nodoActual not in visitados:
                visitados.add(nodoActual)
                for hijo in nodoActual.nodo.expandeHijos():
                    hijo.pathAMi = nodoActual.nodo.pathAMi.copy()
                    hijo.pathAMi.append(hijo.nombre)
                    self.frontera.agrega(hijo, nodoActual.nodo, nodoActual.costoAcumulado)

