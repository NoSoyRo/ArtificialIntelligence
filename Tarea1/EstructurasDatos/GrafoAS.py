from EstructurasDatos.GrafoVoraz import GrafoVoraz

class GrafoAS(GrafoVoraz):
    def __init__(self, nodos: list, arcos: dict, heuristicas: dict) -> None:
        super().__init__(nodos, arcos, heuristicas)
    def busquedaAS(self, nodoInicial, nodoFinal):
        visitados = set()
        self.inicializaFronteraBusquedaAS(nodoInicial, self.heuristicas)
        encontreSolucion = False
        nodoInicial.pathAMi = [nodoInicial.nombre]
        while encontreSolucion == False:
            if self.fronteraAS.esVacia():
                return -1 # Failure code
            nodoActual = self.fronteraAS.extraeCabeza()
            # TO-DO agrega la forma de ir guardando el caminito
            if nodoActual.nodo.nombre == nodoFinal.nombre: # cambiar a un objeto.equals(objeto)
                encontreSolucion = True
                nodoFinal.pathAMi = nodoActual.nodo.pathAMi.copy()
                nodoFinal.pathAMi.append(nodoActual.nodo.nombre)
                print(nodoFinal.pathAMi)
                return nodoActual.costoAcumulado
            if nodoActual not in visitados:
                visitados.add(nodoActual)
                for hijo in nodoActual.nodo.expandeHijos():
                    hijo.pathAMi = nodoActual.nodo.pathAMi.copy()
                    hijo.pathAMi.append(nodoActual.nodo.nombre)
                    self.fronteraAS.agregaVoraz(hijo, nodoActual.nodo)