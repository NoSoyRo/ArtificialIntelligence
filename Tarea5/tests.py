import unittest
from datetime import datetime
from src.Fabricas import FabricaDeTablas
from src.Modelos import RegresionLinealSalarios



class TestBusquedas(unittest.TestCase):

    def test_fabricas_tablas(self):
        fabrica = FabricaDeTablas.FabricaDeTablas({0:'User ID', 1:'Gneder', 2:'Age', 3:'EstimatedSalary', 4:'Purchased'}, './Tarea5/src/Data/Social_Network_Ads.csv')
        fabrica.crea_matriz_de_datos()
        #print(fabrica.data)

    def test_creacion_tablas_test_train(self):
        fabrica = FabricaDeTablas.FabricaDeTablas({0:'User ID', 1:'Gneder', 2:'Age', 3:'EstimatedSalary', 4:'Purchased'}, './Tarea5/src/Data/Social_Network_Ads.csv')
        fabrica.crea_matriz_de_datos()
        x_train, y_train, x_test, y_test = fabrica.crea_tablas_entrenamiento_validacion(80)
        #print(x_train)

    def test_regresion_lineal(self):
        fabrica = FabricaDeTablas.FabricaDeTablas({0:'User ID', 1:'Gneder', 2:'Age', 3:'EstimatedSalary', 4:'Purchased'}, './Tarea5/src/Data/Social_Network_Ads.csv')
        fabrica.crea_matriz_de_datos()
        x_train, y_train, x_test, y_test = fabrica.crea_tablas_entrenamiento_validacion(80)
        regresion_lineal = RegresionLinealSalarios.RegresionLinealSalarios(x_train, y_train, x_test, y_test)

    

if __name__ == '__main__':
    unittest.main()