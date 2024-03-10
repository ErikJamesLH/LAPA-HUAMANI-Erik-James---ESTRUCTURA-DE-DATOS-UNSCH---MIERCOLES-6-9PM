
## Accede al elemento central de una matriz.

def obtener_elemento_central(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])  

    fila_central = filas // 2
    columna_central = columnas // 2

    elemento_central = matriz[fila_central][columna_central]
    return elemento_central

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

elemento_central = obtener_elemento_central(matriz)
print("El elemento central de la matriz es:", elemento_central)
