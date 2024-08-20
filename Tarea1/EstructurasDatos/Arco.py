class Arco():
    def __init__(self, nodoInicial, nodoFinal, costo) -> None:
        self.nodoInicial = nodoInicial
        self.nodoFinal = nodoFinal
        self.costo = costo
    def __str__(self) -> str:
        return self.nodoInicial.nombre + ' -> ' + self.nodoFinal.nombre + ' costo: ' + self.costo 