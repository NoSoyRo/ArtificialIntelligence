import unittest
from EstructurasDatos.Nodo import Nodo
from EstructurasDatos.Grafo import Grafo


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

if __name__ == '__main__':
    unittest.main()
        