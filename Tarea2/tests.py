import unittest
from datetime import datetime
from Fabricas import FabricaDeCSP
from Fabricas import FabricaDeAsignacion
from Busqueda import BusquedaCSP
from Busqueda import BusquedaCSPBackTrackColoreado
from Fabricas import FabricaDeCSPColoreado
from Fabricas import FabricaDeAsignacionColoreado
from AlgoritmoGenetico import AlgoritmoGeneticoNReinas
from MiniMax import MiniMaxGato


class TestBusquedas(unittest.TestCase):

    # Tests de backtracking.

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

    # def testCSPBusquedaBacktrackColoreado5(self):
    #     csp = FabricaDeCSPColoreado.FabricaDeCSPColoreado().creaCSP(1)
    #     asignacion = FabricaDeAsignacionColoreado.FabricaDeAsignacion().creaAsignacion()
    #     busqueda = BusquedaCSPBackTrackColoreado.BusquedaCSPBackTrackColoreado(csp, asignacion)
    #     resultado = busqueda.busquedaBackTrack()
    #     print(resultado)

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

    # Tests de genetico

    # def testAlgoritmoGeneticoNReinas(self):
    #     algoritmoGeneticoNReinas = AlgoritmoGeneticoNReinas.AlgoritmoGeneticoNReinas(100, 1000, 0.5, 10000)
    #     algoritmoGeneticoNReinas.algoritmoGenetico()

    # No me dio tiempo de implementar el genetico para coloreado de grafos.

    # Tests para tic tac toe (Gato)

    def testMiniMaxTicTacToe(self):
        mmg = MiniMaxGato.MiniMaxGato()

        # Inicia juego:
        while not mmg.esJuegoTerminado():
            mmg.imprimeTablero()
            
            # Human move
            print("tu movimiento! ingresa el numero de columna y fila  por ejemplo <<0 1>> representa la fila cero y columna 1:")
            row, col = map(int, input().split())
            if mmg.tablero[row][col] == '_':
                mmg.tablero[row][col] = mmg.humano
            else:
                print("movimiento invalido!")
                continue
            
            # AI move
            if not mmg.esJuegoTerminado():
                best_move = mmg.encuentraMejorMovimiento()
                mmg.tablero[best_move[0]][best_move[1]] = mmg.maquina 
    
        mmg.imprimeTablero()
        score = mmg.evaluaEstadoTerminal()
        if score == 3:
            print("maquina gana!")
        elif score == -3:
            print("humano gana!")
        else:
            print("empate!")




if __name__ == '__main__':
    unittest.main()