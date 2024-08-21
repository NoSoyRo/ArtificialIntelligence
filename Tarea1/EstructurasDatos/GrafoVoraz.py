from EstructurasDatos.Grafo import Grafo 

class GrafoVoraz(Grafo):
    def __init__(self, nodos: list, arcos: dict, heuristicas: dict) -> None:
        super().__init__(nodos, arcos)
        self.heuristicas = heuristicas
    def busquedaVoraz(self, nodoInicial, nodoFinal):
        # Solucion que no solamente guarda el path sino el minimo costo.
        visitados = set()
        self.inicializaFronteraBusquedaVoraz(nodoInicial, self.heuristicas)
        encontreSolucion = False
        nodoInicial.pathAMi = [nodoInicial.nombre]
        while encontreSolucion == False:
            if self.fronteraVoraz.esVacia():
                return -1 # Failure code
            nodoActual = self.fronteraVoraz.extraeCabeza()
            print(nodoActual.nodo.pathAMi)
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
                    self.fronteraVoraz.agregaVoraz(hijo, nodoActual.nodo)