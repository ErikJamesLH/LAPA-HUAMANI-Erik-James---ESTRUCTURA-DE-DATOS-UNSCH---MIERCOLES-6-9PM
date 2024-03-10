
## Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que  están ordenados de mayor a menor.

def numeros_ordenados_de_mayor_a_menor(conjunto_numeros):
    numeros_ordenados_lista = sorted(conjunto_numeros, reverse=True)
    return set(numeros_ordenados_lista)

def obtener_conjunto_numeros_del_usuario():
    conjunto_numeros = set()
    cantidad_numeros = int(input("Ingrese la cantidad de números en el conjunto: "))
    print("Ingrese los números:")
    for i in range(cantidad_numeros):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        conjunto_numeros.add(numero)
    return conjunto_numeros

conjunto_numeros = obtener_conjunto_numeros_del_usuario()

numeros_ordenados_conjunto = numeros_ordenados_de_mayor_a_menor(conjunto_numeros)
print("Números ordenados de mayor a menor:", numeros_ordenados_conjunto)
