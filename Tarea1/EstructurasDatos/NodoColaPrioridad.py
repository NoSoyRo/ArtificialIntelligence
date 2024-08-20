class NodoColaPrioridad():
    def __init__(self, costoAcumulado, nodo) -> None:
        self.costoAcumulado = costoAcumulado
        self.nodo = nodo
    def __str__(self) -> str:
        return str(self.costoAcumulado) + ' -> ' + str(self.nodo.nombre)