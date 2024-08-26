from datetime import datetime
import logging


class Ayudante():
    def __init__(self) -> None:
        pass
    @staticmethod
    def productoPunto(A,B):
        suma = sum(a * b for a, b in zip(A, B))
        return suma
    @staticmethod
    def loggeaTexto(texto):
        logging.basicConfig(
            filename='./LOGS/mochila_log.log',            # Nombre del archivo de log
            level=logging.DEBUG,              # Nivel de registro mínimo (DEBUG es el más bajo)
            format='%(asctime)s - %(levelname)s - %(message)s'  # Formato de los mensajes de log
        )

        logging.debug('captura de tiempo: DE: -------->' + texto)

