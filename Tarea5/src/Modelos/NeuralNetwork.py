import numpy as np

class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        # Inicialización de pesos con Xavier
        self.W1 = np.random.rand(input_size, hidden_size)
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.rand(hidden_size, output_size)
        self.b2 = np.zeros((1, output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)  # x debe ser la salida de la función sigmoide

    def forward_pass(self, X):
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)  # Usando sigmoide
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.z2  # Aplicar sigmoide en la salida
        return self.a2  # Salida final

    def backward_pass(self, X, y):
        output = self.a2  # Usar la salida de la red
        error = output - y  # Cálculo del error

        # Gradientes para la capa de salida
        dW2 = np.dot(self.a1.T, error) / error.shape[0]  # Promediar sobre el número de ejemplos
        db2 = np.sum(error, axis=0, keepdims=True) / error.shape[0]  # Promediar el error

        # Propagar el error hacia atrás
        dA1 = np.dot(error, self.W2.T)
        dZ1 = dA1 * self.sigmoid_derivative(self.a1)  # Aplicar la derivada de la sigmoide
        dW1 = np.dot(X.T, dZ1) / dZ1.shape[0]  # Promediar el gradiente
        db1 = np.sum(dZ1, axis=0, keepdims=True) / dZ1.shape[0]  # Promedio del gradiente

        # Actualizar pesos y sesgos
        self.W2 -= self.learning_rate * dW2
        self.b2 -= self.learning_rate * db2
        self.W1 -= self.learning_rate * dW1
        self.b1 -= self.learning_rate * db1

    def train(self, X, y, epochs=10000):
        for epoch in range(epochs):
            fwd = self.forward_pass(X)
            self.backward_pass(X, y)  # Pasar X y y a backward_pass

    def predict(self, X):
        return self.forward_pass(X)


