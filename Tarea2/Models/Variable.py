
# dominio es un set de valores tipo inf, float, etc
# valores admisibles es un set de int, float, whatever
# vecinos es un set de variable
# restricciones es un set
class Variable():
    def __init__(self, valor, dominio, valoresAdmisibles, vecinos, restricciones, columna) -> None:
        # columnas van de 0 a n donde n es el numero de damas
        self.columna = columna
        # la variable se inicializa en valor = 0
        self.valor = valor
        self.dominio = dominio
        self.valoresAdmisibles = valoresAdmisibles
        self.vecinos = vecinos
        self.restricciones = restricciones
    def creaValoresAdmisibles(self):
        self.valoresAdmisibles = self.dominio - self.restricciones
