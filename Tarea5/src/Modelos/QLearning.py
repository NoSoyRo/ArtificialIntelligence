import numpy as np
import random

class FrozenLake:
    def __init__(self, map_string, slip_probability=0.2):
        self.map = self.parse_map(map_string)
        self.n_rows = len(self.map)
        self.n_cols = len(self.map[0])
        self.start = (0, 0)  # posición inicial
        self.goal = (self.n_rows - 1, self.n_cols - 1)  # posición del objetivo
        self.position = self.start
        self.slip_probability = slip_probability
        self.done = False

    def parse_map(self, map_string):
        # """Convierte una cadena de mapa en una lista de listas."""
        return [list(row) for row in map_string.strip().split("\n")]

    def reset(self):
        # """Reinicia el entorno a su estado inicial."""
        self.position = self.start
        self.done = False
        return self.get_state()

    def step(self, action):
        # """Realiza un paso en el entorno basado en la acción."""
        if self.done:
            raise Exception("El episodio ha terminado. Reinicie el entorno.")

        # Posiciones posibles de movimiento
        moves = {
            0: (0, -1),  # izquierda
            1: (1, 0),   # abajo
            2: (0, 1),   # derecha
            3: (-1, 0),  # arriba
        }

        # Aplicar el movimiento
        intended_move = moves[action]
        next_position = (self.position[0] + intended_move[0], self.position[1] + intended_move[1])

        # Verificar si hay deslizamiento
        if random.random() < self.slip_probability:
            slip_direction = random.choice(list(moves.values()))
            next_position = (self.position[0] + slip_direction[0], self.position[1] + slip_direction[1])

        # Limitar a los bordes del mapa
        next_position = self.limit_position(next_position)

        self.position = next_position
        reward = self.get_reward()
        self.done = self.position == self.goal
        return self.get_state(), reward, self.done

    def limit_position(self, position):
        # """Limita la posición al tamaño del mapa."""
        row, col = position
        if row < 0:
            row = 0
        elif row >= self.n_rows:
            row = self.n_rows - 1
        if col < 0:
            col = 0
        elif col >= self.n_cols:
            col = self.n_cols - 1
        return (row, col)

    def get_state(self):
        # """Devuelve el estado actual como un número entero."""
        return self.position[0] * self.n_cols + self.position[1]

    def get_reward(self):
        # """Devuelve la recompensa basada en la posición actual."""
        if self.position == self.goal:
            return 1  # Recompensa por alcanzar el objetivo
        elif self.map[self.position[0]][self.position[1]] == 'H':
            return 0  # Sin recompensa por caer en un agujero
        return 0  # Sin recompensa por moverse sobre el hielo

class QLearningAgent:
    def __init__(self, state_size, action_size, learning_rate=0.1, discount_factor=0.95, exploration_rate=1.0, exploration_decay=0.995, min_exploration_rate=0.01):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay
        self.min_exploration_rate = min_exploration_rate
        
        # Inicializar la tabla Q
        self.q_table = np.zeros((state_size, action_size))

    def choose_action(self, state):
        if random.uniform(0, 1) < self.exploration_rate:
            return random.randint(0, self.action_size - 1)  # Explorar
        return np.argmax(self.q_table[state])  # Explotar

    def update_q_value(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.discount_factor * self.q_table[next_state][best_next_action]
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += self.learning_rate * td_error

    def decay_exploration(self):
        if self.exploration_rate > self.min_exploration_rate:
            self.exploration_rate *= self.exploration_decay


    