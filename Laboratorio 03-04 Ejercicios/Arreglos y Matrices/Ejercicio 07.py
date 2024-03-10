
## Crea una matriz de números complejos.

def crear_matriz_compleja(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            # Generar un número complejo aleatorio
            real = float(input(f"Ingrese la parte real del número complejo en la fila {i+1}, columna {j+1}: "))
            imaginario = float(input(f"Ingrese la parte imaginaria del número complejo en la fila {i+1}, columna {j+1}: "))
            numero_complejo = complex(real, imaginario)
            fila.append(numero_complejo)
        matriz.append(fila)
    return matriz

filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

matriz_compleja = crear_matriz_compleja(filas, columnas)
print("La matriz compleja generada es:")
for fila in matriz_compleja:
    print(fila)
