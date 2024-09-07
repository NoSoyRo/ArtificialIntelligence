from Models import Variable
from Models import Asignacion

class FabricaDeAsignacion():
    def __init__(self) -> None:
        pass
    def creaAsignacion(self):
        return Asignacion.Asignaciones()