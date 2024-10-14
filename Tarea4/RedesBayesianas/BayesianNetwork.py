from itertools import product

class BayesianNetwork:
    def __init__(self):
        self.variables = {}  # Almacena variables y sus valores posibles
        self.dependencies = {}  # Almacena dependencias (padres)
        self.probabilities = {}  # Almacena tablas de probabilidad condicional (CPT)

    def add_variable(self, variable, values):
        self.variables[variable] = values

    def add_dependency(self, child, parents):
        self.dependencies[child] = parents

    def add_probability(self, variable, cpt):
        self.probabilities[variable] = cpt

    def print_network(self):
        print("Variables:")
        for var, vals in self.variables.items():
            print(f"{var}: {vals}")
        print("\nDependencias:")
        for child, parents in self.dependencies.items():
            print(f"{child}: {parents}")
        print("\nProbabilidades:")
        for var, cpt in self.probabilities.items():
            print(f"{var}: {cpt}")
    
    def is_d_separated(self, x, y, z):
        # Convierte a conjuntos para fácil manejo
        x = set([x]) if isinstance(x, str) else set(x)
        y = set([y]) if isinstance(y, str) else set(y)
        z = set(z) if isinstance(z, (list, tuple)) else {z}

        # Encuentra todos los caminos entre cada variable en X y cada variable en Y
        for x_var in x:
            for y_var in y:
                paths = self.find_all_paths(x_var, y_var)

                # Verifica si algún camino está bloqueado por Z
                for path in paths:
                    if not self.is_path_blocked(path, z):
                        return False  # Si hay un camino no bloqueado, no están D-separados

        return True  # Si todos los caminos están bloqueados, están D-separados


    def find_all_paths(self, x, y, visited=None, path=[]):
        if visited is None:
            visited = set()

        visited.add(x)  # Cambia union por add
        path = path + [x]

        if x == y:
            return [path]

        paths = []
        for neighbor in self.dependencies.get(x, []):
            if neighbor not in visited:
                new_paths = self.find_all_paths(neighbor, y, visited, path)
                for new_path in new_paths:
                    paths.append(new_path)

        visited.remove(x)
        return paths


    def is_path_blocked(self, path, z):
        for i in range(len(path) - 1):
            if path[i] in z:
                # Verifica si es un colider
                if (i > 0 and i < len(path) - 1 and path[i - 1] in self.dependencies.get(path[i], []) 
                        and path[i + 1] in self.dependencies.get(path[i], [])):
                    continue  # Es un colider, sigue buscando
                else:
                    return True  # Camino bloqueado
        return False  # Camino no bloqueado
    
    # --- Métodos para inferencia mediante busqueda exaustiva ---

    def inference(self, query, evidence):
        # Paso 1: Obtener todas las variables no observadas
        hidden_vars = set(self.variables.keys()) - set(evidence.keys()) - {query}

        # Paso 2: Enumerar todas las posibles asignaciones de valores para las variables ocultas
        hidden_var_combinations = list(product(*[self.variables[var] for var in hidden_vars]))

        # Paso 3: Sumar las probabilidades conjuntas para las distintas asignaciones
        true_prob = 0.0
        false_prob = 0.0
        
        for assignment in hidden_var_combinations:
            # Crear un diccionario que contenga la evidencia, la consulta y la asignación actual
            full_assignment = {query: 'True'}  # Consulta para 'query=True'
            full_assignment.update(evidence)
            full_assignment.update({var: val for var, val in zip(hidden_vars, assignment)})
            
            # Calcular la probabilidad conjunta para esta asignación
            prob = self.joint_probability(full_assignment)
            true_prob += prob
            
            # Ahora considerar la consulta para 'query=False'
            full_assignment[query] = 'False'
            prob = self.joint_probability(full_assignment)
            false_prob += prob

        # Paso 4: Normalizar los resultados
        total_prob = true_prob + false_prob
        normalized_false_prob = true_prob / total_prob if total_prob > 0 else 0
        normalized_true_prob = false_prob / total_prob if total_prob > 0 else 0

        return {query: {"True": normalized_true_prob, "False": normalized_false_prob}}

    def joint_probability(self, assignment):
        joint_prob = 1.0
        
        # Para cada variable, multiplicamos la probabilidad condicional
        for var, value in assignment.items():
            parents = self.dependencies.get(var, [])
            parent_assignment = tuple(assignment[parent] for parent in parents)  # Asignación de los padres

            cpt = self.probabilities.get(var)

            # Asegurarse de que la asignación de los padres esté formateada correctamente
            if len(parents) == 0:  # Caso sin padres
                prob = cpt.get(())  # No hay condicionamiento, usar la tabla directamente
            else:
                prob = cpt.get(parent_assignment)  # Obtener la probabilidad condicional para la asignación
            
            # Verificamos si prob es None
            if prob is None:
                raise ValueError(f"No se encontró la probabilidad para {var} con padres {parent_assignment}.")

            # Verificar si estamos evaluando para 'True' o 'False'
            if value in [True, 'true']:  # Tratar 'True' como 'true'
                joint_prob *= prob[0]  # Probabilidad para 'true'
            else:
                joint_prob *= prob[1]  # Probabilidad para 'false'

        return joint_prob
