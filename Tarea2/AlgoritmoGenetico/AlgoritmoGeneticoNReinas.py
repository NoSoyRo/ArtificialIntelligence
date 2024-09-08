import random

class AlgoritmoGeneticoNReinas():
    def __init__(self, nReinas, nPoblacion, razonMutacion, maxGeneraciones) -> None:
        self.nReinas = nReinas
        self.nPoblacion = nPoblacion
        self.razonMutacion = razonMutacion
        self.maxGeneraciones = maxGeneraciones
    
    def creaPoblacion(self):
        poblacion = []
        for i in range(self.nPoblacion):
            individuo = random.sample(range(self.nReinas), self.nReinas)
            poblacion.append(individuo)
        return poblacion
    
    def calculaFitness(self, individuo):
        parejasSinAtacarse = 0
        for i in range(self.nReinas):
            for j in range(i+1, self.nReinas):
                if abs(i-j) != abs(individuo[i] - individuo[j]):
                    parejasSinAtacarse += 1
        return parejasSinAtacarse
    
    def seleccionNatural(self):
        tamanioRoundRobin = 5
        torneo = random.sample(self.poblacion, tamanioRoundRobin)
        torneo.sort(key=lambda x: self.calculaFitness(x), reverse=True)
        return torneo[0], torneo[1]
    
    def apareamiento(self, padre1, padre2):
        indiceDeMezcla = random.randint(0, self.nReinas - 1)
        hijo1 = padre1[:indiceDeMezcla] + padre2[indiceDeMezcla:]
        hijo2 = padre2[:indiceDeMezcla] + padre1[indiceDeMezcla:]
        return hijo1, hijo2
    
    def muta(self, individuo):
        if random.random() < self.razonMutacion:
            i, j = random.sample(range(self.nReinas), 2)  
            individuo[i], individuo[j] = individuo[j], individuo[i]  # la mutacion consiste en intercambiar valores de cada individuo de forma aleatoria

    def algoritmoGenetico(self):
        self.poblacion = self.creaPoblacion()

        for generacion in range(self.maxGeneraciones): # limite de tiempo para converger
            nuevaPob = []
            for i in range(self.nPoblacion // 2):
                padre1, padre2 = self.seleccionNatural()
                hijo1, hijo2 = self.apareamiento(padre1, padre2)
                self.muta(hijo1)
                self.muta(hijo2)

                nuevaPob.append(hijo1)
                nuevaPob.append(hijo2)

            self.poblacion = nuevaPob

            mejorIndividuo = max(self.poblacion, key=lambda x: self.calculaFitness(x))
            mejorFitness = self.calculaFitness(mejorIndividuo)

            if mejorFitness == self.nReinas * (self.nReinas - 1) // 2: # Si no hay pares de reunbas que se ataquen
                print(mejorIndividuo)
                break
        else:
            print("No se encontró solución óptima.")

    