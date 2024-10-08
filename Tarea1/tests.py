import unittest
from EstructurasDatos.GrafoMochila import GrafoMochila
from EstructurasDatos.Nodo import Nodo
from EstructurasDatos.Grafo import Grafo
from EstructurasDatos.GrafoVoraz import GrafoVoraz
from EstructurasDatos.GrafoAS import GrafoAS
from EstructurasDatos.ElementoMochila import ElementoMochila
from datetime import datetime
from EstructurasDatos.Ayudante import Ayudante



class TestBusquedaCostoUniforme(unittest.TestCase):

    # Tests de grafos para busqueda de costo uniforme, implementado.

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

    # Tests de grafos para busqueda voraz, implementado.

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

    # Test 2 para busqueda Voraz.

    def test3Elemento(self):
        print("Test grafo A*")
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

        grafo = GrafoAS(nodos, arcos, heuristica)
        self.assertEqual(grafo.busquedaVoraz(A, C), 0)

    # Test de busqueda A* en grafo, usando el problema de ARAD, imprime en consola el path y tambien imprime el costo óptimo
    # El orden de desarrollo fue primero Grafos y busquedas voracez y costo uniforme, despues se unen los dos algoritmos para generar
    # A*

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

    # Primer test para el algoritmo alterado de busqueda A* usando la nueva heurística.

    def testMochilaDummyCase1(self):
        
        listaElementos = []

        listaElementos.append(ElementoMochila([], 'e'+str(0), 3, 1))
        listaElementos.append(ElementoMochila([], 'e'+str(1), 3, 2))
        listaElementos.append(ElementoMochila([], 'e'+str(2), 3, 3))
        
        capacidadMochila = 5

        grafo = GrafoMochila(listaElementos, capacidadMochila)
        grafo.busquedaAStar()
        self.assertEqual(grafo.mejorEstado.estado, [1,1,0])

    # Segundo test para el algoritmo alterado de busqueda A* usando la nueva heurística.

    def testMochilaDummyCase2(self):
        
        listaElementos = []

        listaElementos.append(ElementoMochila([], 'e'+str(0), 3, 3))
        listaElementos.append(ElementoMochila([], 'e'+str(1), 3, 3))
        listaElementos.append(ElementoMochila([], 'e'+str(2), 3, 3))
        
        capacidadMochila = 5

        grafo = GrafoMochila(listaElementos, capacidadMochila)
        grafo.busquedaAStar()
        self.assertEqual(grafo.mejorEstado.estado, [1,0,0])

    # Tercer test para el algoritmo alterado de busqueda A* usando la nueva heurística.

    def testMochilaDummyCase3(self):
        
        listaElementos = []

        listaElementos.append(ElementoMochila([], 'e'+str(0), 100, 5))
        listaElementos.append(ElementoMochila([], 'e'+str(1), 3, 1))
        listaElementos.append(ElementoMochila([], 'e'+str(2), 3, 1))
        
        capacidadMochila = 5

        grafo = GrafoMochila(listaElementos, capacidadMochila)
        grafo.busquedaAStar()
        self.assertEqual(grafo.mejorEstado.estado, [1,0,0])

    # Test 4 de lo mismo.

    def testMochilaDummyCase4(self):
        
        listaElementos = []

        listaElementos.append(ElementoMochila([], 'e'+str(0), 1, 1))
        listaElementos.append(ElementoMochila([], 'e'+str(1), 1, 1))
        listaElementos.append(ElementoMochila([], 'e'+str(2), 1, 1))
        
        capacidadMochila = 5

        grafo = GrafoMochila(listaElementos, capacidadMochila)
        grafo.busquedaAStarOptim()
        self.assertEqual(grafo.mejorEstado.estado, [1,1,1])

    #  NOTE: PROBLEMA CON LA MEMORIA, TUVE DOS EJECUCIONES FALLIDAS POR USO DE MEMORIA, 
    #        NO ME DIO TIEMPO DE OPTIMIZAR EL USO DE MEMORIA EN MI PROGRAMA

    # def testMochila10k(self):
    #         #importamos la data
    #         Ayudante.loggeaTexto("INICIA EL PROCESO DE TESTEO")
    #         Ayudante.loggeaTexto("Importamos data")
    #         with open('./Data/ks_10000_0', 'r') as file:
    #             lines = file.readlines()
    #         cantidadElementos, capacidadMochila = int(lines[0].split(' ')[0]), int(lines[0].split(' ')[1])
    #         lines.pop(0)
    #         listaElementos = []
    #         cont = 0
    #         for i in range(cantidadElementos):
    #             listaElementos.append(ElementoMochila([], 'e'+str(cont), int(lines[i].split(' ')[0]), int(lines[i].split(' ')[1])))
    #             cont+=1
    #         Ayudante.loggeaTexto("Sort inicial de la data")
    #         elementosOrdenadoConBaseEnPeso = sorted(listaElementos, key=lambda elemento: elemento.peso)
    #         Ayudante.loggeaTexto("Grafo inicializacion")
    #         grafo = GrafoMochila(elementosOrdenadoConBaseEnPeso, capacidadMochila)
    #         Ayudante.loggeaTexto("Inicia Busqueda//////////////////////////////////")
    #         grafo.busquedaAStar()
    #         Ayudante.loggeaTexto("Finaliza Busqueda//////////////////////////////////")

    #         print(grafo.mejorEstado.estado)

    # Test de para el archivo de mochila de 19 elementos, se imprime la mejor configuracion, revisar documentacion de la terea 
    # para entender el resultado.

    def testMochila19(self):
            #importamos la data
            timestamp_actual = datetime.now()
            fecha_formateada = timestamp_actual.strftime("%Y-%m-%d %H:%M:%S")
            print('iniciamos proceso a las: ' + str(fecha_formateada))
            with open('./Data/ks_19_0', 'r') as file:
                lines = file.readlines()
            cantidadElementos, capacidadMochila = int(lines[0].split(' ')[0]), int(lines[0].split(' ')[1])
            lines.pop(0)
            listaElementos = []
            cont = 0
            for i in range(cantidadElementos):
                listaElementos.append(ElementoMochila([], 'e'+str(cont), int(lines[i].split(' ')[0]), int(lines[i].split(' ')[1])))
                cont+=1
            elementosOrdenadoConBaseEnPeso = sorted(listaElementos, key=lambda elemento: elemento.peso)
            grafo = GrafoMochila(elementosOrdenadoConBaseEnPeso, capacidadMochila)
            grafo.busquedaAStar()
            timestamp_actual = datetime.now()
            fecha_formateada = timestamp_actual.strftime("%Y-%m-%d %H:%M:%S")
            print('fin proceso a las: ' + str(fecha_formateada))
            print(grafo.mejorEstado.estado)
            l1 = [i.peso for i in elementosOrdenadoConBaseEnPeso]
            l2 = [i.valor for i in elementosOrdenadoConBaseEnPeso]
            print('peso: '+str(l1))
            print('valor: '+str(l2))
            print('capacidad: '+str(capacidadMochila))



if __name__ == '__main__':
    unittest.main()
