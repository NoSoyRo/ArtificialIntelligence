from Models import Variable
from CSP import CSP

class FabricaDeCSP():
    def __init__(self, nReinas) -> None:
        self.nReinas = nReinas
    def creaCSP(self):
        return CSP.CSP(self.creaVariables())
    def creaVariables(self):
        conjVariables = []
        dominioComun = set([i for i in range(1, self.nReinas + 1)])
        for i in range(self.nReinas):
            variableI = Variable.Variable(0, dominioComun, i)
            conjVariables.append(variableI)
        return conjVariables

        