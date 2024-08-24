from typing import Any
from EstructurasDatos.Nodo import Nodo

class ElementoMochila(Nodo):
    def __init__(self, hijos: list, nombre: str,valor, peso ) -> None:
        super().__init__(hijos, nombre)
        self.peso = peso
        self.valor = valor
    def __str__(self) -> str:
        return super().__str__()