
## Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están ordenados de menor a mayor y que no están duplicados

def numeros_ordenados_sin_duplicados(conjunto_numeros):
    numeros_ordenados = sorted(conjunto_numeros)
    numeros_sin_duplicados = set(numeros_ordenados)
    return numeros_sin_duplicados

def obtener_conjunto_numeros_del_usuario():
    conjunto_numeros = set()
    cantidad_numeros = int(input("Ingrese la cantidad de números en el conjunto: "))
    print("Ingrese los números:")
    for i in range(cantidad_numeros):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        conjunto_numeros.add(numero)
    return conjunto_numeros

conjunto_numeros = obtener_conjunto_numeros_del_usuario()

numeros_ordenados_sin_duplicados = numeros_ordenados_sin_duplicados(conjunto_numeros)
print("Números ordenados de menor a mayor y sin duplicados:", numeros_ordenados_sin_duplicados)
