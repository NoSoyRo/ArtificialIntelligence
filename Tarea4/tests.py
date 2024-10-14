import unittest
from datetime import datetime
from RedesBayesianas import BayesianNetwork
from Constructores import ConstructorDeDAG


class TestBusquedas(unittest.TestCase):

    def test_to_d_separation_algorithm(self):
        file_name = './Tarea4/Data/barley.bif'
        constructor = ConstructorDeDAG.ConstructorDeDAG(file_name)
        redBayesiana = constructor.parse_bif()
        result = redBayesiana.is_d_separated("nedbarea", "komm", [])
        redBayesiana.print_network()
        print('\n')
        print(result)  # Para ver el resultado, aunque no es necesario

        print('\n A continuacion se hacen los siguiente queries \n')

        # Realizar una consulta: P(nedbarea | komm = state0)
        # query = "nedbarea"
        # evidence = {"komm": "state0"}

        # # Obtener inferencia
        # result = redBayesiana.inference(query, evidence)
        # query = "nmin"
        # evidence = {"komm": "state0"}

        # # Obtener inferencia
        # result = redBayesiana.inference(query, evidence)
        # query = "jordn"
        # evidence = {"komm": "state0"}

        # # Obtener inferencia
        # result = redBayesiana.inference(query, evidence)
        # print(result)
    
    def test_to_inference_algorithm(self):
        file_name = './Tarea4/Data/burglar.bif'
        constructor = ConstructorDeDAG.ConstructorDeDAG(file_name)
        redBayesiana = constructor.parse_bif()
        print('A continuacion la red modelada y tambien una revision de d-separacion \n')
        redBayesiana.print_network()
        print('\n')
        result = redBayesiana.is_d_separated("Alarm", "Burglar", []) # Lector debe de tener cuidado de usar a discresion el metodo is_d_separated, toma como primer variable el nodo final y la segunda variable es el nodo inicial
        print(result)  # Para ver el resultado, aunque no es necesario
        # Realizar una consulta: P(Burglar | JohnCalls=true, MaryCalls=true)

        print('\n A continuacion se hacen los siguiente queries \n')

        query = "Burglar"
        evidence = {"JohnCalls": "True", "MaryCalls": "True"}

        # Obtener inferencia
        result = redBayesiana.inference(query, evidence)
        print(result)

        query = "Burglar"
        evidence = {"JohnCalls": "True"}

        # Obtener inferencia
        result = redBayesiana.inference(query, evidence)
        print(result)

        query = "Alarm"
        evidence = {"MaryCalls": "True"}

        # Obtener inferencia
        result = redBayesiana.inference(query, evidence)
        print(result)



if __name__ == '__main__':
    unittest.main()

