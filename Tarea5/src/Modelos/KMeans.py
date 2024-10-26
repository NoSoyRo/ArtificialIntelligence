import numpy as np

class KMeans:
    def __init__(self, n_clusters=3, max_iters=100):
        self.n_clusters = n_clusters  # Número de clústeres
        self.max_iters = max_iters  # Número máximo de iteraciones
        self.centroids = None  # Centroides de los clústeres

    def fit(self, X):
        # Inicializar centroides aleatorios
        np.random.seed(42)  # Para reproducibilidad
        random_indices = np.random.choice(X.shape[0], size=self.n_clusters, replace=False)
        self.centroids = X[random_indices]

        for _ in range(self.max_iters):
            # Paso 1: Asignar cada punto al clúster más cercano
            labels = self._assign_clusters(X)

            # Paso 2: Recalcular los centroides
            new_centroids = self._compute_centroids(X, labels)

            # Verificar la convergencia
            if np.all(new_centroids == self.centroids):
                break

            self.centroids = new_centroids

    def _assign_clusters(self, X):
        # Calcular la distancia entre cada punto y cada centroide
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)  # Etiquetas de los clústeres

    def _compute_centroids(self, X, labels):
        centroids = np.zeros((self.n_clusters, X.shape[1]))
        for i in range(self.n_clusters):
            centroids[i] = X[labels == i].mean(axis=0)  # Calcular el nuevo centroide
        return centroids

    def predict(self, X):
        # Asignar clústeres a nuevos datos
        return self._assign_clusters(X)

   
