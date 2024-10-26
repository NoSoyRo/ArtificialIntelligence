import os
import numpy as np

class FabricaDeTablas():
    def __init__(self, diccionario_columnas, direccion_csv):
        self.diccionario_columnas = diccionario_columnas
        self.direccion_csv = direccion_csv

    def crea_matriz_de_datos(self):
        self.data = np.genfromtxt(self.direccion_csv, delimiter=',', skip_header=1, dtype=[('UserID', 'i8'), ('Gender', 'U10'), ('Age', 'i8'), ('EstimatedSalary', 'i8'), ('Purchased', 'i8')])
        # Convertir 'Male' a 0 y 'Female' a 1 en la columna 'Gender'
        gender_numeric = np.where(self.data['Gender'] == 'Male', 0, 1)
        self.data = np.column_stack((gender_numeric, self.data['Age'], self.data['EstimatedSalary']))

    def crea_tablas_entrenamiento_validacion(self, porcentaje_entrenamiento):
        n = int(self.data.shape[0] * (porcentaje_entrenamiento/100))
        x_train = self.data[:n,0:2]
        y_train = self.data[:n,-1]
        x_test = self.data[n:,0:2]
        y_test = self.data[n:,-1]
        return x_train, y_train, x_test, y_test