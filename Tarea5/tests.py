import unittest
from datetime import datetime
import numpy as np
from src.Fabricas import FabricaDeTablas
from src.Modelos import RegresionLinealSalarios
from src.Modelos import NeuralNetwork
from src.Modelos import KMeans
# import gymnasium as gym
from src.Modelos import QLearning


def train_agent(episodes):
    # Definir el mapa
    map_string = """
    SFFF
    FHFF
    FHFH
    FFFG
    """
    env = QLearning.FrozenLake(map_string)
    agent = QLearning.QLearningAgent(state_size=env.n_rows * env.n_cols, action_size=4)

    for episode in range(episodes):
        state = env.reset()
        done = False

        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.update_q_value(state, action, reward, next_state)
            state = next_state
        
        agent.decay_exploration()
        if episode % 100 == 0:
            print(f'Episode: {episode}, Exploration Rate: {agent.exploration_rate:.4f}')

    return agent

def test_agent(agent, episodes):
    map_string = """
    SFFF
    FHFF
    FHFH
    FFFG
    """
    env = QLearning.FrozenLake(map_string)
    total_rewards = 0

    for episode in range(episodes):
        state = env.reset()
        done = False
        episode_reward = 0

        while not done:
            action = np.argmax(agent.q_table[state])  # Explotar
            next_state, reward, done = env.step(action)
            episode_reward += reward
            state = next_state
        
        total_rewards += episode_reward

    print(f'Average Reward over {episodes} episodes: {total_rewards / episodes}')


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

    def test_q_learning(self):
        trained_agent = train_agent(episodes=10000)
        test_agent(trained_agent, episodes=1000)


if __name__ == '__main__':
    unittest.main()