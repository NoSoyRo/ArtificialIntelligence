

from EstructurasDatos.ElementoMochila import ElementoMochila
from EstructurasDatos.NodoGrafoMochila import NodoGrafoMochila
from EstructurasDatos.ColaPrioridadMochila import ColaPrioridadMochila
from EstructurasDatos.NodoGrafoMochila import NodoGrafoMochila


class GrafoMochila():
    def __init__(self, elementosOrdenadoConBaseEnPeso, capacidadMochila) -> None:
        self.elementos = elementosOrdenadoConBaseEnPeso
        self.pesos = []
        self.valores = []
        self.pesosRelativos = []
        self.capacidadMochila = capacidadMochila
        self.frontera = ColaPrioridadMochila(self.pesos, self.valores, capacidadMochila)
        for i in elementosOrdenadoConBaseEnPeso:
            self.pesos.append(i.peso)
            self.valores.append(i.valor)
            self.pesosRelativos.append(i.peso/capacidadMochila)
        self.nodoInicial = NodoGrafoMochila([0]*len(self.elementos), capacidadMochila, self.pesos, self.valores)
    def busquedaAStar(self):
        visitados = set()
        self.inicializaFrontera()
        self.inicializaMejorEstado()
        acabeDeBuscar = False
        while not acabeDeBuscar:
            if self.frontera.esVacia():
                return -1
            nodoActual = self.frontera.extraeCabeza()
            if nodoActual.valorHeuristica > self.mejorEstado.valorHeuristica:
                self.mejorEstado = nodoActual
            if nodoActual not in visitados:
                visitados.add(nodoActual)
                nodoGrafoParaHijos = NodoGrafoMochila(nodoActual.estado, self.capacidadMochila, self.pesos, self.valores)
                for hijo in nodoGrafoParaHijos.expandeHijosUtiles():
                    self.frontera.agrega(hijo)


        # TO-DO continue code del busqueda estrella con inicializa frontera
    def inicializaFrontera(self):
        for hijo in self.nodoInicial.expandeHijosUtiles():
            self.frontera.agrega(hijo)

    def inicializaMejorEstado(self):
        self.mejorEstado = self.frontera.cola[0]
        
