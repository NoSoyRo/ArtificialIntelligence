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
    
    # --- Métodos para inferencia mediante eliminación de variables ---
    
    def restrict_factor(self, factor, variable, value):
        restricted_factor = {}
        for assignment, prob in factor.items():
            if assignment[variable] == value:
                new_assignment = assignment.copy()
                del new_assignment[variable]
                restricted_factor[tuple(new_assignment.items())] = prob
        return restricted_factor

    def multiply_factors(self, factor1, factor2):
        common_vars = set(factor1.keys()) & set(factor2.keys())
        result_factor = {}
        for assignment1, prob1 in factor1.items():
            for assignment2, prob2 in factor2.items():
                if all(assignment1[var] == assignment2[var] for var in common_vars):
                    new_assignment = {**assignment1, **assignment2}
                    result_factor[tuple(new_assignment.items())] = prob1 * prob2
        return result_factor

    def marginalize_factor(self, factor, variable):
        marginalized_factor = {}
        for assignment, prob in factor.items():
            new_assignment = assignment.copy()
            del new_assignment[variable]
            marginalized_factor[tuple(new_assignment.items())] = marginalized_factor.get(new_assignment, 0) + prob
        return marginalized_factor

    def normalize(self, factor):
        total_prob = sum(factor.values())
        return {k: v / total_prob for k, v in factor.items()}

    def inference(self, query, evidence):
        variables = set(self.variables.keys())
        query_var = query
        factors = []
        
        # Paso 1: Restricción de factores por la evidencia
        for var, cpt in self.probabilities.items():
            factor = self.create_factor(var, cpt)
            for ev_var, ev_val in evidence.items():
                if ev_var in factor:
                    factor = self.restrict_factor(factor, ev_var, ev_val)
            factors.append(factor)
        
        # Paso 2: Eliminación de variables no relacionadas
        hidden_vars = variables - set([query_var]) - set(evidence.keys())
        for hidden_var in hidden_vars:
            # Multiplicar todos los factores que contengan la variable oculta
            related_factors = [f for f in factors if hidden_var in f]
            new_factor = related_factors[0]
            for factor in related_factors[1:]:
                new_factor = self.multiply_factors(new_factor, factor)
            # Marginalizar la variable oculta
            marginalized_factor = self.marginalize_factor(new_factor, hidden_var)
            # Actualizar la lista de factores
            factors = [f for f in factors if hidden_var not in f] + [marginalized_factor]
        
        # Paso 3: Multiplicar factores restantes
        final_factor = factors[0]
        for factor in factors[1:]:
            final_factor = self.multiply_factors(final_factor, factor)
        
        # Paso 4: Normalización
        return self.normalize(final_factor)
    
    def create_factor(self, variable, cpt):
        factor = {}
        for assignment, prob in cpt.items():
            factor[assignment] = prob  # Usa assignment directamente como la clave
        return factor
