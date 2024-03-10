
## Escribe una función que encuentre la matriz de covarianza de dos matrices

import numpy as np

def matriz_covarianza(matriz1, matriz2):
    covarianza = np.cov(matriz1, matriz2)
    return covarianza

matriz1 = np.random.rand(3, 3)
matriz2 = np.random.rand(3, 3)

matriz_cov = matriz_covarianza(matriz1, matriz2)
print("Matriz de covarianza:")
print(matriz_cov)
