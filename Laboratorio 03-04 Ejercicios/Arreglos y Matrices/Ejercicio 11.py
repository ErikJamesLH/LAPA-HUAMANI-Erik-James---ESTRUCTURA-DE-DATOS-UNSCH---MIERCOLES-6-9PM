
## Multiplica una matriz por un número.

def multiplicar_matriz_por_numero(matriz, numero):
    resultado = []
    for fila in matriz:
        fila_resultado = [elemento * numero for elemento in fila]
        resultado.append(fila_resultado)
    return resultado

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
numero = 2

resultado = multiplicar_matriz_por_numero(matriz, numero)

print("La matriz resultante después de la multiplicación es:")
for fila in resultado:
    print(fila)
