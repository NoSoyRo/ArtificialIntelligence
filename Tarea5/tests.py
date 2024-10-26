import unittest
from datetime import datetime
import numpy as np
from src.Fabricas import FabricaDeTablas
from src.Modelos import RegresionLinealSalarios
from src.Modelos import NeuralNetwork
from src.Modelos import KMeans



class TestBusquedas(unittest.TestCase):

    # def test_fabricas_tablas(self):
    #     fabrica = FabricaDeTablas.FabricaDeTablas({0:'User ID', 1:'Gneder', 2:'Age', 3:'EstimatedSalary', 4:'Purchased'}, './Tarea5/src/Data/Social_Network_Ads.csv')
    #     fabrica.crea_matriz_de_datos()
    #     #print(fabrica.data)

    # def test_creacion_tablas_test_train(self):
    #     fabrica = FabricaDeTablas.FabricaDeTablas({0:'User ID', 1:'Gneder', 2:'Age', 3:'EstimatedSalary', 4:'Purchased'}, './Tarea5/src/Data/Social_Network_Ads.csv')
    #     fabrica.crea_matriz_de_datos()
    #     x_train, y_train, x_test, y_test = fabrica.crea_tablas_entrenamiento_validacion(80)
    #     #print(x_train)

    # def test_regresion_lineal(self):
    #     fabrica = FabricaDeTablas.FabricaDeTablas({0:'User ID', 1:'Gneder', 2:'Age', 3:'EstimatedSalary', 4:'Purchased'}, './Tarea5/src/Data/Social_Network_Ads.csv')
    #     fabrica.crea_matriz_de_datos()
    #     x_train, y_train, x_test, y_test = fabrica.crea_tablas_entrenamiento_validacion(80)
    #     regresion_lineal = RegresionLinealSalarios.RegresionLinealSalarios(x_train, y_train, x_test, y_test)

    # def test_red_neuronal(self):
    #     fabrica = FabricaDeTablas.FabricaDeTablas({0:'User ID', 1:'Gneder', 2:'Age', 3:'EstimatedSalary', 4:'Purchased'}, './Tarea5/src/Data/Social_Network_Ads.csv')
    #     fabrica.crea_matriz_de_datos()
    #     x_train, y_train, x_test, y_test = fabrica.crea_tablas_entrenamiento_validacion(70)
    #     y_train = y_train.reshape(-1, 1)
    #     #normalizamos:
    #     max_age_train = np.max(x_train[:, 1])
    #     max_salary_train = np.max(y_train)
    #     max_age_test = np.max(x_train[:, 1])
    #     max_salary_test = np.max(y_train)
    #     # Normaliza X (si es necesario)
    #     x_train[:, 1] = x_train[:, 1] / max(max_age_train, max_age_test)  # Normaliza la edad
    #     x_test[:, 1] = x_test[:, 1] / max(max_age_train, max_age_test)  # Normaliza la edad

    #     # Normaliza y
    #     y_train = y_train / max(max_salary_train,max_salary_test)  # Normaliza el salario
    #     # Inicializar y entrenar la red neuronal
    #     nn = NeuralNetwork.SimpleNeuralNetwork(input_size=2, hidden_size=100, output_size=1)
    #     nn.train(x_train, y_train, epochs=10000)

    #     # Hacer predicciones
    #     final_predictions = nn.predict(x_test) * max(max_salary_test, max_salary_train)

    #     print("Predicciones finales del salario estimado:", final_predictions.flatten())
    #     print(y_test)

    # def test_kmeans(self):
    #     fabrica = FabricaDeTablas.FabricaDeTablas({0:'User ID', 1:'Gneder', 2:'Age', 3:'EstimatedSalary', 4:'Purchased'}, './Tarea5/src/Data/Social_Network_Ads.csv')
    #     fabrica.crea_matriz_de_datos()
    #     # Separar las características
    #     X = fabrica.data[:, 1:]  # Usamos las dos columnas (edad, salario)

    #     # Crear el modelo KMeans
    #     kmeans = KMeans.KMeans(n_clusters=2)
    #     kmeans.fit(X)

    #     # Predicciones
    #     labels = kmeans.predict(X)
    #     print("Etiquetas de clústeres:", labels)
    #     print("Centroides calculados:", kmeans.centroids)


if __name__ == '__main__':
    unittest.main()