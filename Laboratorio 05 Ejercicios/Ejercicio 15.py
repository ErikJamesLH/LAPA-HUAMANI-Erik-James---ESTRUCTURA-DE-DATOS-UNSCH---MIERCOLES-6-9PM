
## Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que  son primos y están ordenados de menor a mayor

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos_ordenados(conjunto_numeros):
    primos_ordenados = set()
    for numero in sorted(conjunto_numeros):
        if es_primo(numero):
            primos_ordenados.add(numero)
    return primos_ordenados

def obtener_conjunto_numeros_del_usuario():
    conjunto_numeros = set()
    cantidad_numeros = int(input("Ingrese la cantidad de números en el conjunto: "))
    print("Ingrese los números:")
    for i in range(cantidad_numeros):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        conjunto_numeros.add(numero)
    return conjunto_numeros

conjunto_numeros = obtener_conjunto_numeros_del_usuario()

primos_ordenados_conjunto = numeros_primos_ordenados(conjunto_numeros)
print("Números primos ordenados de menor a mayor:", primos_ordenados_conjunto)
