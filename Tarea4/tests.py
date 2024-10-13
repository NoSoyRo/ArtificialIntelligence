import unittest
from datetime import datetime
from RedesBayesianas import BayesianNetwork
from Constructores import ConstructorDeDAG


class TestBusquedas(unittest.TestCase):

    # def test_to_d_separation_algorithm(self):
    #     file_name = './Tarea4/Data/barley.bif'
    #     constructor = ConstructorDeDAG.ConstructorDeDAG(file_name)
    #     redBayesiana = constructor.parse_bif()
    #     result = redBayesiana.is_d_separated("nedbarea", "komm", [])
    #     print(result)  # Para ver el resultado, aunque no es necesario
    
    def test_to_inference_algorithm(self):
        file_name = './Tarea4/Data/burglar.bif'
        constructor = ConstructorDeDAG.ConstructorDeDAG(file_name)
        redBayesiana = constructor.parse_bif()
        redBayesiana.print_network()
        result = redBayesiana.is_d_separated("Alarm", "Burglar", []) # Lector debe de tener cuidado de usar a discresion el metodo is_d_separated, toma como primer variable el nodo final y la segunda variable es el nodo inicial
        print(result)  # Para ver el resultado, aunque no es necesario
        # Realizar una consulta: P(Burglar | JohnCalls=true, MaryCalls=true)
        query = "Burglar"
        evidence = {"JohnCalls": "true", "MaryCalls": "true"}

        # Obtener inferencia
        result = redBayesiana.inference(query, evidence)


if __name__ == '__main__':
    unittest.main()

