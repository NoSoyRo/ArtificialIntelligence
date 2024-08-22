from EstructurasDatos.GrafoVoraz import GrafoVoraz

class GrafoAS(GrafoVoraz):
    def __init__(self, nodos: list, arcos: dict, heuristicas: dict) -> None:
        super().__init__(nodos, arcos, heuristicas)
    def busquedaAS(self, nodoInicial, nodoFinal):
        visitados = set()
        self.inicializaFronteraBusquedaAS(nodoInicial, self.heuristicas)
        encontreSolucion = False
        nodoFinal.pathAMi = []
        nodoFinal.pathAMiNombres = []
        nodoFinal.costoOptimo = 0
        while encontreSolucion == False:
            if self.fronteraAS.esVacia():
                return -1 # Failure code
            nodoActual = self.fronteraAS.extraeCabeza()
            # TO-DO agrega la forma de ir guardando el caminito
            if nodoActual.nodo.nombre == nodoFinal.nombre: # cambiar a un objeto.equals(objeto)
                encontreSolucion = True
                nodoFinal.pathAMi = nodoActual.nodo.pathAMi.copy()
                nodoFinal.pathAMi.append((nodoActual.nodo.nombre, nodoActual.nodo))
                print(nodoFinal.pathAMi)
                nodoFinal.costoOptimo = 0 
                for i in range(len(nodoFinal.pathAMi[1:])): 
                    nodoFinal.costoOptimo = self.fronteraAS.busquedaCostoArco(nodoFinal.pathAMi[i][1], nodoFinal.pathAMi[i+1][1]) + nodoFinal.costoOptimo
                return nodoFinal.costoOptimo
            if nodoActual not in visitados:
                visitados.add(nodoActual)
                for hijo in nodoActual.nodo.expandeHijos():
                    hijo.pathAMi = nodoActual.nodo.pathAMi.copy()
                    hijo.pathAMi.append((nodoActual.nodo.nombre, nodoActual.nodo))
                    self.fronteraAS.agregaAS(hijo, nodoActual.nodo, nodoActual.costoAcumulado)