
## Suma dos matrices de diferentes tamaños.

def suma_matrices(matriz1, matriz2):
    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    columnas_matriz2 = len(matriz2[0])

    if filas_matriz1 != filas_matriz2 or columnas_matriz1 != columnas_matriz2:
        return None  # No se pueden sumar las matrices

    resultado = []
    for i in range(filas_matriz1):
        fila_resultado = []
        for j in range(columnas_matriz1):
            suma_elementos = matriz1[i][j] + matriz2[i][j]
            fila_resultado.append(suma_elementos)
        resultado.append(fila_resultado)

    return resultado

matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matriz2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

resultado = suma_matrices(matriz1, matriz2)
if resultado is not None:
    print("La suma de las matrices es:")
    for fila in resultado:
        print(fila)
else:
    print("Las matrices no tienen las mismas dimensiones y no se pueden sumar.")
