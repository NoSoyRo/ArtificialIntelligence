import math

class MiniMaxGato():
    humano = 'O'
    maquina = 'X'

    tablero = [
        ['_','_','_'],
        ['_','_','_'],
        ['_','_','_']
    ]

    # Metodo que revisa si el estado actual es terminal
    def evaluaEstadoTerminal(self):
        for fila in MiniMaxGato.tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] != '_':
                if fila[0] == MiniMaxGato.maquina:
                    return 3  
                else:
                    return -3
        for col in range(3):
            if MiniMaxGato.tablero[0][col] == MiniMaxGato.tablero[1][col] == MiniMaxGato.tablero[2][col] and MiniMaxGato.tablero[0][col] != '_':
                return 3 if MiniMaxGato.tablero[0][col] == MiniMaxGato.maquina else -3
        if MiniMaxGato.tablero[0][0] == MiniMaxGato.tablero[1][1] == MiniMaxGato.tablero[2][2] and MiniMaxGato.tablero[0][0] != '_':
            return 3 if MiniMaxGato.tablero[0][0] == MiniMaxGato.maquina else -3
        if MiniMaxGato.tablero[0][2] == MiniMaxGato.tablero[1][1] == MiniMaxGato.tablero[2][0] and MiniMaxGato.tablero[0][2] != '_':
            return 3 if MiniMaxGato.tablero[0][2] == MiniMaxGato.maquina else -3
        return 0  

    # Metodo que revisa si quedan movimientos posibles
    def quedanMovimientos(self):
        for row in MiniMaxGato.tablero:
            if '_' in row:
                return True
        return False
    
    def algoritmoMiniMax(self, profundidad, esMaximizacion):
        puntaje = self.evaluaEstadoTerminal()

        if puntaje == 3:
            return puntaje - profundidad
        
        if puntaje == -3:
            return puntaje + profundidad
        
        if not self.quedanMovimientos():
            return 0
        
        # maximizamos el movimiento de la maquina

        if esMaximizacion:
            mejor = -math.inf # Inicializamos de esta manera para asegurar tomar todos los casos
            for i in range(3):
                for j in range(3):
                    if MiniMaxGato.tablero[i][j] == '_':
                        MiniMaxGato.tablero[i][j] = MiniMaxGato.maquina
                        mejor = max(mejor, self.algoritmoMiniMax(profundidad + 1, False))
                        MiniMaxGato.tablero[i][j] = '_'
            return mejor

        # minimizamos el movimeinto del humano

        else:
            mejor = math.inf
            for i in range(3):
                for j in range(3):
                    if MiniMaxGato.tablero[i][j] == '_':
                        MiniMaxGato.tablero[i][j] = MiniMaxGato.humano
                        mejor = min(mejor, self.algoritmoMiniMax(profundidad + 1, True))
                        MiniMaxGato.tablero[i][j] = '_'
            return mejor
        
    def encuentraMejorMovimiento(self):
        mejorValor = -math.inf
        mejorMovimiento = (-1, -1)
        
        for i in range(3):
            for j in range(3):
                if MiniMaxGato.tablero[i][j] == '_':
                    MiniMaxGato.tablero[i][j] = MiniMaxGato.maquina
                    movimiento = self.algoritmoMiniMax(0, False)
                    MiniMaxGato.tablero[i][j] = '_'
                    
                    if movimiento > mejorValor:
                        mejorMovimiento = (i, j)
                        mejorValor = movimiento
        return mejorMovimiento    
    
    def imprimeTablero(self):
        for fila in MiniMaxGato.tablero:
            print(' '.join(fila))
        print()

    def esJuegoTerminado(self):
        return self.evaluaEstadoTerminal() != 0 or not self.quedanMovimientos()