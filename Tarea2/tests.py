import unittest
from datetime import datetime
from Fabricas import FabricaDeCSP
from Fabricas import FabricaDeAsignacion
from Busqueda import BusquedaCSP



class TestBusquedas(unittest.TestCase):

    # Tests de grafos para busqueda de costo uniforme, implementado.

    def test1Elemento(self):
        # definimos csp para las damas
        # tablero 3x3
        csp = FabricaDeCSP.FabricaDeCSP(100).creaCSP()
        asignaciones = FabricaDeAsignacion.FabricaDeAsignacion().creaAsignacion()
        busqueda = BusquedaCSP.BusquedaCSP(csp, asignaciones)
        resultado = busqueda.busquedaBackTrack()
        print(resultado)
        return resultado

if __name__ == '__main__':
    unittest.main()