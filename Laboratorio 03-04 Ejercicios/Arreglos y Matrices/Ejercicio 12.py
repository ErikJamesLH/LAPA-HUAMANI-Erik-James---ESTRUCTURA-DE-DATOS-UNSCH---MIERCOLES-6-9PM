
## Calcula la media de los elementos de una matriz

def calcular_media_matriz(matriz):
    total_elementos = 0
    suma_elementos = 0

    for fila in matriz:
        total_elementos += len(fila)
        suma_elementos += sum(fila)

    media = suma_elementos / total_elementos
    return media

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

media = calcular_media_matriz(matriz)
print("La media de los elementos de la matriz es:", media)
