import unittest
from EstructurasDatos.Nodo import Nodo
from EstructurasDatos.Grafo import Grafo
from EstructurasDatos.GrafoVoraz import GrafoVoraz


class TestBusquedaCostoUniforme(unittest.TestCase):
    
    def test1Elemento(self):
        # A -> B E = 2
        # B -> C E = 2 
        # A -> C E = 3

        C = Nodo([], 'C')
        B = Nodo([C], 'B')
        A = Nodo([B, C], 'A')

        nodos = [A,B,C]

        arcos = dict()
        arcos[(A,B)] = 1
        arcos[(B,C)] = 1
        arcos[(A,C)] = 3

        grafo = Grafo(nodos, arcos)
        self.assertEqual(grafo.busquedaCostoUniforme(A, C), 2)

    def test2Elemento(self):
        # A -> B E = 2
        # B -> C E = 2 
        # A -> C E = 3

        C = Nodo([], 'C')
        B = Nodo([C], 'B')
        D = Nodo([C], 'D')
        A = Nodo([B, D], 'A')

        nodos = [A,B,C,D]

        arcos = dict()
        arcos[(A,B)] = 1
        arcos[(B,C)] = 1
        arcos[(A,D)] = 3
        arcos[(D,C)] = 3

        heuristica = {A: 4, B: 10, C: 0, D: 2}


        grafo = GrafoVoraz(nodos, arcos, heuristica)
        self.assertEqual(grafo.busquedaVoraz(A, C), 0)

    def test3Elemento(self):
        # A -> B E = 2
        # B -> C E = 2 
        # A -> C E = 3

        C = Nodo([], 'c')
        B = Nodo([C], 'b')
        D = Nodo([C], 'd')
        A = Nodo([B, D], 'a')

        nodos = [A,B,C,D]

        arcos = dict()
        arcos[(A,B)] = 1
        arcos[(B,C)] = 1
        arcos[(A,D)] = 3
        arcos[(D,C)] = 3

        heuristica = {A: 4, B: 10, C: 0, D: 2}


        grafo = GrafoVoraz(nodos, arcos, heuristica)
        self.assertEqual(grafo.busquedaVoraz(A, C), 0)

if __name__ == '__main__':
    unittest.main()
        