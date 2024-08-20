class Nodo():
    def __init__(self, hijos: list, nombre: str) -> None:
        self.hijos = hijos
        self.nombre = nombre
        self.pathAMi = []
    def expandeHijos(self):
        return self.hijos
    def __str__(self) -> str:
        return self.nombre
        
