from Models import VariableColoreado
from CSP import CSPColoreado

class FabricaDeCSPColoreado():
    def creaCSP(self, opcion):
        if opcion == 1:
             return CSPColoreado.CSPColoreado(self.creaVariables5())
        if opcion == 2:
             return CSPColoreado.CSPColoreado(self.creaVariables50())
        if opcion == 3:
             return CSPColoreado.CSPColoreado(self.creaVariables1000())
    
    def creaVariables1000(self):
        listaVariables = []
        with open('./Tarea2/Fabricas/Datos/gc_1000_9', 'r') as file:
                lines = file.readlines()
        nRegiones, nArcos = int(lines[0].split(' ')[0]), int(lines[0].split(' ')[1])
        for i in range(nRegiones):
            listaVariables.append(VariableColoreado.VariableColoreado([], i))
        for i in range(1,nArcos + 1):
            regionIzq, regionDer = int(lines[i].split(' ')[0]), int(lines[i].split(' ')[1])
            # Los indices nos dicen cual es la region
            listaVariables[regionIzq].vecinos.append(regionDer)
            listaVariables[regionDer].vecinos.append(regionIzq)
        # Se crea copia y se ordena lista de variables ocn base en la cantidad de elementos
        return listaVariables

    def creaVariables50(self):
        listaVariables = []
        with open('./Tarea2/Fabricas/Datos/gc_50_7', 'r') as file:
                lines = file.readlines()
        nRegiones, nArcos = int(lines[0].split(' ')[0]), int(lines[0].split(' ')[1])
        for i in range(nRegiones):
            listaVariables.append(VariableColoreado.VariableColoreado([], i))
        for i in range(1,nArcos + 1):
            regionIzq, regionDer = int(lines[i].split(' ')[0]), int(lines[i].split(' ')[1])
            # Los indices nos dicen cual es la region
            listaVariables[regionIzq].vecinos.append(regionDer)
            listaVariables[regionDer].vecinos.append(regionIzq)
        # Se crea copia y se ordena lista de variables ocn base en la cantidad de elementos
        return listaVariables
    
    def creaVariables5(self):
        listaVariables = []
        with open('./Tarea2/Fabricas/Datos/gc_5_7', 'r') as file:
                lines = file.readlines()
        nRegiones, nArcos = int(lines[0].split(' ')[0]), int(lines[0].split(' ')[1])
        for i in range(nRegiones):
            listaVariables.append(VariableColoreado.VariableColoreado([], i))
        for i in range(1,nArcos + 1):
            regionIzq, regionDer = int(lines[i].split(' ')[0]), int(lines[i].split(' ')[1])
            # Los indices nos dicen cual es la region
            listaVariables[regionIzq].vecinos.append(regionDer)
            listaVariables[regionDer].vecinos.append(regionIzq)
        # Se crea copia y se ordena lista de variables ocn base en la cantidad de elementos
        return listaVariables