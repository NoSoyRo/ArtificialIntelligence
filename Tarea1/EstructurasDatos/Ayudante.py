class Ayudante():
    def __init__(self) -> None:
        pass
    @staticmethod
    def productoPunto(A,B):
        suma = sum(a * b for a, b in zip(A, B))
        return suma
