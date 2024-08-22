import unittest
from EstructurasDatos.Nodo import Nodo
from EstructurasDatos.Grafo import Grafo
from EstructurasDatos.GrafoVoraz import GrafoVoraz
from EstructurasDatos.GrafoAS import GrafoAS


class TestBusquedaCostoUniforme(unittest.TestCase):
    
    # def test1Elemento(self):
    #     # A -> B E = 2
    #     # B -> C E = 2 
    #     # A -> C E = 3

    #     C = Nodo([], 'C')
    #     B = Nodo([C], 'B')
    #     A = Nodo([B, C], 'A')

    #     nodos = [A,B,C]

    #     arcos = dict()
    #     arcos[(A,B)] = 1
    #     arcos[(B,C)] = 1
    #     arcos[(A,C)] = 3

    #     grafo = Grafo(nodos, arcos)
    #     self.assertEqual(grafo.busquedaCostoUniforme(A, C), 2)

    # def test2Elemento(self):
    #     # A -> B E = 2
    #     # B -> C E = 2 
    #     # A -> C E = 3

    #     C = Nodo([], 'C')
    #     B = Nodo([C], 'B')
    #     D = Nodo([C], 'D')
    #     A = Nodo([B, D], 'A')

    #     nodos = [A,B,C,D]

    #     arcos = dict()
    #     arcos[(A,B)] = 1
    #     arcos[(B,C)] = 1
    #     arcos[(A,D)] = 3
    #     arcos[(D,C)] = 3

    #     heuristica = {A: 4, B: 10, C: 0, D: 2}


    #     grafo = GrafoVoraz(nodos, arcos, heuristica)
    #     self.assertEqual(grafo.busquedaVoraz(A, C), 0)

    # def test3Elemento(self):
    #     print("Test grafo A*")
    #     # A -> B E = 2
    #     # B -> C E = 2 
    #     # A -> C E = 3

    #     C = Nodo([], 'c')
    #     B = Nodo([C], 'b')
    #     D = Nodo([C], 'd')
    #     A = Nodo([B, D], 'a')

    #     nodos = [A,B,C,D]

    #     arcos = dict()
    #     arcos[(A,B)] = 1
    #     arcos[(B,C)] = 1
    #     arcos[(A,D)] = 3
    #     arcos[(D,C)] = 3

    #     heuristica = {A: 4, B: 10, C: 0, D: 2}


    #     grafo = GrafoAS(nodos, arcos, heuristica)
    #     self.assertEqual(grafo.busquedaVoraz(A, C), 0)

    def testAradGraph(self):

            Arad = Nodo([], 'Arad')
            Timisoara = Nodo([], 'Timisoara')
            Zerind = Nodo([], 'Zerind')
            Oradea = Nodo([], 'Oradea')
            Sibiu = Nodo([], 'Sibiu')
            Lugoj = Nodo([], 'Lugoj')
            Mehadia = Nodo([], 'Mehadia')
            Dobreta = Nodo([], 'Dobreta')
            Cralova = Nodo([], 'Cralova')
            Pitesti = Nodo([], 'Pitesti')
            RimnicuVilcea = Nodo([], 'RimnicuVilcea')
            Fagaras = Nodo([], 'Fagaras')
            Bucharest = Nodo([], 'Bucharest')
            Giurgiu = Nodo([], 'Giurgiu')
            Urziceni = Nodo([], 'Urziceni')
            Vaslui = Nodo([], 'Vaslui')
            Iasi = Nodo([], 'Iasi')
            Neamt = Nodo([], 'Neamt')
            Hirsova = Nodo([], 'Hirsova')
            Eforie = Nodo([], 'Eforie')

            Arad.hijos = [Zerind, Sibiu, Timisoara]
            Zerind.hijos = [Arad, Oradea]
            Timisoara.hijos = [Arad, Lugoj]
            Oradea.hijos = [Zerind, Sibiu]
            Sibiu.hijos = [Oradea, Arad, Fagaras, RimnicuVilcea]
            Lugoj.hijos = [Timisoara, Mehadia]
            Mehadia.hijos = [Lugoj, Dobreta]
            Dobreta.hijos = [Mehadia, Cralova]
            Cralova.hijos = [RimnicuVilcea, Pitesti]
            RimnicuVilcea.hijos = [Sibiu, Pitesti, Cralova]
            Pitesti.hijos = [Bucharest, RimnicuVilcea, Cralova]
            Fagaras.hijos = [Sibiu, Bucharest]
            Bucharest.hijos = [Fagaras, Pitesti, Giurgiu, Urziceni]
            Giurgiu.hijos = [Bucharest]
            Urziceni.hijos = [Bucharest, Vaslui, Hirsova]
            Vaslui.hijos = [Urziceni, Iasi]
            Hirsova.hijos = [Urziceni, Eforie]
            Eforie.hijos = [Hirsova]
            Iasi.hijos = [Neamt, Vaslui]
            Neamt.hijos = [Iasi]

            arcos = dict()
            arcos[(Arad,Zerind)] = 75
            arcos[(Zerind,Arad)] = 75
            arcos[(Arad,Sibiu)] = 140
            arcos[(Sibiu,Arad)] = 140
            arcos[(Arad,Timisoara)] = 118
            arcos[(Timisoara,Arad)] = 118
            arcos[(Timisoara,Lugoj)] = 111
            arcos[(Lugoj,Timisoara)] = 111
            arcos[(Zerind,Oradea)] = 71
            arcos[(Oradea,Zerind)] = 71
            arcos[(Oradea,Sibiu)] = 151
            arcos[(Sibiu,Oradea)] = 151
            arcos[(Lugoj,Mehadia)] = 70
            arcos[(Mehadia,Lugoj)] = 70
            arcos[(Mehadia,Dobreta)] = 75
            arcos[(Dobreta,Mehadia)] = 75
            arcos[(Dobreta,Cralova)] = 120
            arcos[(Cralova,Dobreta)] = 120
            arcos[(Cralova,RimnicuVilcea)] = 146
            arcos[(RimnicuVilcea,Cralova)] = 146
            arcos[(Cralova,Pitesti)] = 138
            arcos[(Pitesti,Cralova)] = 138
            arcos[(Sibiu,Fagaras)] = 99
            arcos[(Fagaras,Sibiu)] = 99
            arcos[(Sibiu, RimnicuVilcea)] = 80
            arcos[(RimnicuVilcea, Sibiu)] = 80
            arcos[(Pitesti, RimnicuVilcea)] = 97
            arcos[(RimnicuVilcea, Pitesti)] = 97
            arcos[(Fagaras,Bucharest)] = 211
            arcos[(Bucharest,Fagaras)] = 211
            arcos[(Pitesti,Bucharest)] = 101
            arcos[(Bucharest,Pitesti)] = 101
            arcos[(Bucharest,Urziceni)] = 85
            arcos[(Urziceni,Bucharest)] = 85
            arcos[(Urziceni,Vaslui)] = 142
            arcos[(Vaslui,Urziceni)] = 142
            arcos[(Vaslui,Iasi)] = 92
            arcos[(Iasi,Vaslui)] = 92
            arcos[(Iasi,Neamt)] = 87
            arcos[(Neamt,Iasi)] = 87
            arcos[(Urziceni,Hirsova)] = 98 
            arcos[(Hirsova,Urziceni)] = 98
            arcos[(Eforie,Hirsova)] = 86
            arcos[(Hirsova,Eforie)] = 86

            heuristica = dict()
            heuristica[Arad] = 366
            heuristica[Bucharest] = 0
            heuristica[Cralova] = 160
            heuristica[Dobreta] = 242
            heuristica[Eforie] = 161
            heuristica[Fagaras] = 178
            heuristica[Giurgiu] = 77
            heuristica[Hirsova] = 151
            heuristica[Iasi] = 226
            heuristica[Lugoj] = 244
            heuristica[Mehadia] = 241
            heuristica[Neamt] = 234
            heuristica[Oradea] = 380
            heuristica[Pitesti] = 98
            heuristica[RimnicuVilcea] = 193
            heuristica[Sibiu] = 253
            heuristica[Timisoara] = 329
            heuristica[Urziceni] = 80
            heuristica[Vaslui] = 199
            heuristica[Zerind] = 374

            nodos = [Arad, Bucharest, Cralova, Dobreta, Eforie, Fagaras, Giurgiu, Hirsova, Iasi, Lugoj, Mehadia, Neamt, Oradea, Pitesti, RimnicuVilcea, Sibiu, Timisoara, Urziceni, Vaslui, Zerind]

            grafo = GrafoAS(nodos, arcos, heuristica)
            self.assertEqual(grafo.busquedaAS(Arad, Bucharest), 418)

if __name__ == '__main__':
    unittest.main()
        