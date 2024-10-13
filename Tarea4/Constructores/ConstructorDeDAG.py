from RedesBayesianas import BayesianNetwork
import os

class ConstructorDeDAG():
    def __init__(self,file_name):
        self.file_name = file_name
        self.network = None
    def parse_bif(self):
        file_name = self.file_name
        network = BayesianNetwork.BayesianNetwork()
        print(os.getcwd())
        with open(file_name, 'r') as file:
            lines = file.readlines()

        variable = None
        parents = []
        cpt = {}

        for line in lines:
            line = line.strip().rstrip(';')  # Eliminar espacios y el ';' al final de la línea
            if line.startswith("variable"):
                # Leer nombre de la variable
                parts = line.split()
                variable = parts[1]
            elif line.startswith("type"):
                # Leer valores discretos de la variable
                values = line.split("{")[1].replace("}", "").split(", ")
                values = [v.strip() for v in values]
                network.add_variable(variable, values)
            elif line.startswith("probability"):
                # Leer variable y sus padres
                parts = line.replace("probability", "").replace("(", "").replace(")", "").replace("{", "").replace("}", "").strip().split("|")

                variable = parts[0].strip()
                if len(parts) > 1:
                    parents = [p.strip() for p in parts[1].split(",")]
                else:
                    parents = []
                network.add_dependency(variable, parents)
                cpt = {}  # Reiniciar CPT
            elif line.startswith("table"):
                # Leer probabilidades no condicionadas
                prob_values = [float(p) for p in line.replace("table", "").strip().split(",")]
                cpt[()] = prob_values  # Guardar tabla para variable sin padres
                network.add_probability(variable, cpt)
            elif line.startswith("("):
                # Leer probabilidades condicionadas
                condition, prob_values = line.split(")")
                condition = tuple(condition.replace("(", "").split(", "))
                prob_values = [float(p) for p in prob_values.strip().split(",")]
                cpt[condition] = prob_values
                network.add_probability(variable, cpt)
        self.network = network
        return network