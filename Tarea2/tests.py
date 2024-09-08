import unittest
from datetime import datetime
from Fabricas import FabricaDeCSP
from Fabricas import FabricaDeAsignacion
from Busqueda import BusquedaCSP
from Busqueda import BusquedaCSPBackTrackColoreado
from Fabricas import FabricaDeCSPColoreado
from Fabricas import FabricaDeAsignacionColoreado



class TestBusquedas(unittest.TestCase):

    # Tests de grafos para busqueda de costo uniforme, implementado.

    # def testCSPBusquedaBacktrackNReinas(self):
    #     # definimos csp para las damas
    #     # tablero 3x3
    #     csp = FabricaDeCSP.FabricaDeCSP(100).creaCSP()
    #     asignaciones = FabricaDeAsignacion.FabricaDeAsignacion().creaAsignacion()
    #     busqueda = BusquedaCSP.BusquedaCSP(csp, asignaciones)
    #     resultado = busqueda.busquedaBackTrack()
    #     print(resultado)
    #     return resultado

    # def testCSPBusquedaBacktrackColoreado50(self):
    #     csp = FabricaDeCSPColoreado.FabricaDeCSPColoreado().creaCSP()

    def testCSPBusquedaBacktrackColoreado5(self):
        csp = FabricaDeCSPColoreado.FabricaDeCSPColoreado().creaCSP(1)
        asignacion = FabricaDeAsignacionColoreado.FabricaDeAsignacion().creaAsignacion()
        busqueda = BusquedaCSPBackTrackColoreado.BusquedaCSPBackTrackColoreado(csp, asignacion)
        resultado = busqueda.busquedaBackTrack()
        print(resultado)

    # def testCSPBusquedaBacktrackColoreado50(self):
    #     csp = FabricaDeCSPColoreado.FabricaDeCSPColoreado().creaCSP(2)
    #     asignacion = FabricaDeAsignacionColoreado.FabricaDeAsignacion().creaAsignacion()
    #     busqueda = BusquedaCSPBackTrackColoreado.BusquedaCSPBackTrackColoreado(csp, asignacion)
    #     resultado = busqueda.busquedaBackTrack()
    #     print(resultado)

    # def testCSPBusquedaBacktrackColoreado1000(self):
    #     csp = FabricaDeCSPColoreado.FabricaDeCSPColoreado().creaCSP(3)
    #     asignacion = FabricaDeAsignacionColoreado.FabricaDeAsignacion().creaAsignacion()
    #     busqueda = BusquedaCSPBackTrackColoreado.BusquedaCSPBackTrackColoreado(csp, asignacion)
    #     resultado = busqueda.busquedaBackTrack()
    #     print(resultado)


if __name__ == '__main__':
    unittest.main()