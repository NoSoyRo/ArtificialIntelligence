from Models import Variable
from Models import AsignacionColoreado

class FabricaDeAsignacion():
    def __init__(self) -> None:
        pass
    def creaAsignacion(self):
        return AsignacionColoreado.AsignacionesColoreado()