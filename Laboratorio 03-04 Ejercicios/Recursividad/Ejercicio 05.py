
## Ejercicio 5: Escribe una función recursiva que imprima la tabla de multiplicar del n.

def tabla_multiplicar_recursivo(n, multiplicador=1):
    if multiplicador <= 10:
        # Imprimir la fila actual de la tabla de multiplicar
        print(f"{n} x {multiplicador} = {n * multiplicador}")
        # Llamada recursiva para la siguiente fila
        tabla_multiplicar_recursivo(n, multiplicador + 1)

tabla_multiplicar_recursivo(10)
