
from EstructurasDatos.Ayudante import Ayudante


class NodoGrafoMochila():
    def __init__(self, estado: list, capacidad, pesos, valores) -> None:
        self.hijos = []
        self.estado = estado
        self.capacidad = capacidad
        self.pesos = pesos
        self.valores = valores
    def expandeHijosUtiles(self):
        pesoTotal = Ayudante.productoPunto(self.estado,self.pesos)
        ultimoIndiceCon1 = [i for i, j in enumerate(self.estado) if j == 1]
        if len(ultimoIndiceCon1) == 0:
            auxList = []
            for i in range(len(self.estado)):
                if self.pesos[i]>self.capacidad:
                    return auxList
                listCopy = self.estado.copy()
                listCopy[i] = 1
                auxList.append(listCopy)
            return auxList
        auxList = []
        for i in range(ultimoIndiceCon1[-1]+1, len(self.estado)):
            if pesoTotal + self.pesos[i] > self.capacidad:
                return self.hijos
            listCopy = self.estado.copy()
            listCopy[i] = 1
            auxList.append(listCopy)
        return auxList
    