
from EstructurasDatos.NodoGrafoMochila import NodoGrafoMochila
from EstructurasDatos.ColaPrioridadMochila import ColaPrioridadMochila
from EstructurasDatos.NodoGrafoMochila import NodoGrafoMochila
from EstructurasDatos.Ayudante import Ayudante


class GrafoMochila():
    def __init__(self, elementosOrdenadoConBaseEnPeso, capacidadMochila) -> None:
        self.elementos = elementosOrdenadoConBaseEnPeso
        self.pesos = []
        self.valores = []
        #self.pesosRelativos = []
        self.capacidadMochila = capacidadMochila
        self.frontera = ColaPrioridadMochila(self.pesos, self.valores, capacidadMochila)
        for i in elementosOrdenadoConBaseEnPeso:
            self.pesos.append(i.peso)
            self.valores.append(i.valor)
            #self.pesosRelativos.append(i.peso/capacidadMochila)
        self.nodoInicial = NodoGrafoMochila([0]*len(self.elementos), capacidadMochila, self.pesos, self.valores)
    def busquedaAStar(self):
        visitados = set()
        Ayudante.loggeaTexto("Inicia inicializacion de frontera")
        self.inicializaFrontera()
        Ayudante.loggeaTexto("Finaliza iniciacion de frontera")
        Ayudante.loggeaTexto("Inicia inicializacion de mejor estado")
        self.inicializaMejorEstado()
        Ayudante.loggeaTexto("Finaliza inicializacion de mejor estado")

        acabeDeBuscar = False
        while not acabeDeBuscar:
            Ayudante.loggeaTexto("Inicia nuevo ciclo")
            if self.frontera.esVacia():
                return -1
            Ayudante.loggeaTexto("Extraemos cabeza")
            nodoActual = self.frontera.extraeCabeza()
            Ayudante.loggeaTexto("comparacion heuristica")
            if nodoActual.valorHeuristica > self.mejorEstado.valorHeuristica:
                self.mejorEstado = nodoActual
            Ayudante.loggeaTexto("logica de nodos no visitados y agregadop de hijos.")
            if nodoActual not in visitados:
                visitados.add(nodoActual)
                nodoGrafoParaHijos = NodoGrafoMochila(nodoActual.estado, self.capacidadMochila, self.pesos, self.valores)
                for hijo in nodoGrafoParaHijos.expandeHijosUtiles():
                    self.frontera.agrega(hijo)

    def busquedaAStarOptim(self):
        visitados = set()
        Ayudante.loggeaTexto("Inicia inicializacion de frontera")
        self.inicializaFrontera()
        Ayudante.loggeaTexto("Finaliza iniciacion de frontera")
        Ayudante.loggeaTexto("Inicia inicializacion de mejor estado")
        self.inicializaMejorEstado()
        Ayudante.loggeaTexto("Finaliza inicializacion de mejor estado")

        acabeDeBuscar = False
        while not acabeDeBuscar:
            Ayudante.loggeaTexto("Inicia nuevo ciclo")
            if self.frontera.esVacia():
                return -1
            Ayudante.loggeaTexto("Extraemos cabeza")
            nodoActual = self.frontera.extraeCabeza()
            Ayudante.loggeaTexto("comparacion heuristica")
            if nodoActual.valorHeuristica > self.mejorEstado.valorHeuristica:
                self.mejorEstado = nodoActual
            Ayudante.loggeaTexto("logica de nodos no visitados y agregadop de hijos.")
            if nodoActual not in visitados:
                visitados.add(nodoActual)
                nodoGrafoParaHijos = NodoGrafoMochila(nodoActual.estado, self.capacidadMochila, self.pesos, self.valores)
                nodosNuevos, ultimoInidiceCon1 = nodoGrafoParaHijos.expandeHijosUtilesOptim()
                for hijo in nodosNuevos:
                    if hijo == ultimoInidiceCon1 + 1:
                        nodoActual.estado[hijo] = 1
                        self.frontera.agrega(nodoActual=nodoActual.estado)
                        continue
                    nodoActual.estado[hijo] = 1
                    nodoActual.estado[hijo-1] = 0
                    self.frontera.agrega(nodoActual=nodoActual.estado)

        # TO-DO continue code del busqueda estrella con inicializa frontera
    def inicializaFrontera(self):
        for hijo in self.nodoInicial.expandeHijosUtiles():
            self.frontera.agrega(hijo)

    def inicializaFronteraOptim(self):
        nodos, ultimoIndiceCon1 = self.nodoInicial.expandeHijosUtilesOptim()
        for hijo in nodos:
            if hijo == ultimoIndiceCon1 + 1:
                self.nodoInicial.estado[hijo] = 1
                continue
            self.nodoInicial.estado[hijo-1] = 0
            self.nodoInicial.estado[hijo] = 1   
            self.frontera.agrega(self.nodoInicial.estado[hijo])

    def inicializaMejorEstado(self):
        self.mejorEstado = self.frontera.cola[0]
        
