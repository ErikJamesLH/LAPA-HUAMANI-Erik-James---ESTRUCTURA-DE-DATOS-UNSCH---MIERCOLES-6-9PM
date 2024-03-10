
## Escribe una función que encuentre la submatriz de mayor suma de una matriz.

import numpy as np

def encontrar_submatriz_max_suma(matriz):
    submatriz_max = np.zeros((2, 2))
    max_suma = 0

    for i in range(len(matriz) - 1):
        for j in range(len(matriz[i]) - 1):
            submatriz = matriz[i:i+2, j:j+2]
            suma_submatriz = np.sum(submatriz)

            if suma_submatriz > max_suma:
                max_suma = suma_submatriz
                submatriz_max = submatriz

    return submatriz_max

submatriz_maxima = encontrar_submatriz_max_suma(matriz_aleatoria)
print("Submatriz de mayor suma:")
print(submatriz_maxima)
