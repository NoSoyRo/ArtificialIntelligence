class VariableColoreado():

    # El dominio de colores y los vecinos son datos que todas las variables deben de conocer
    dominioComunColores = []

    def __init__(self, vecinos, region) -> None:
        self.region = region
        self.vecinos = vecinos
        self.color = 0
        self.restricciones = []
        self.valoresAdmisiblesExistentes = []
    def creaValoresAdmisiblesExistentes(self):
        self.valoresAdmisiblesExistentes = set(VariableColoreado.dominioComunColores) - set(self.restricciones)
    def __str__(self) -> str:
        string = ''
        for i in self.vecinos:
            string += '|' + str(i) + '|'
        return string
