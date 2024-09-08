
# Las variables son dueñas de sus dominios y sus restricciones y varibales es un set() de variable
class CSPColoreado():
    def __init__(self, variables) -> None:
        self.variables = variables #Lista ordenada con base en la cantidad de vecinos de mayor a menor.
        self.variablesOrdenadas = sorted(variables.copy(), key=lambda variable: len(variable.vecinos), reverse = True)
