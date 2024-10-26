import os
import numpy as np

class RegresionLinealSalarios():
    def __init__(self, x_train,
                 y_train,
                 x_test,
                 y_test):
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test

    def entrena_modelo(self):
        X = self.x_train
        y = self.y_train
        self.X_b = np.c_[np.ones((X.shape[0], 1)), X]
        self.beta = np.linalg.inv(self.X_b.T.dot(self.X_b)).dot(self.X_b.T).dot(y)
    
    def imprime_predicciones(self):
        self.predictions_train = self.X_b.dot(self.beta)

        # Mostrar coeficientes e intercepto
        print("Intercepto:", self.beta[0])
        print("Coeficientes para Gender y Age:", self.beta[1:])
        print("Predicciones de salario estimado en train:", self.predictions_train)
    


    