
##  Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que no  están duplicados.

def numeros_no_duplicados(conjunto_numeros):
    numeros_unicos = set()
    numeros_duplicados = set()
    
    for numero in conjunto_numeros:
        if numero in numeros_unicos:
            numeros_duplicados.add(numero)
        else:
            numeros_unicos.add(numero)
    
    numeros_no_duplicados = conjunto_numeros - numeros_duplicados
    
    return numeros_no_duplicados

def obtener_conjunto_numeros_del_usuario():
    conjunto_numeros = set()
    cantidad_numeros = int(input("Ingrese la cantidad de números en el conjunto: "))
    print("Ingrese los números:")
    for i in range(cantidad_numeros):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        conjunto_numeros.add(numero)
    return conjunto_numeros

conjunto_numeros = obtener_conjunto_numeros_del_usuario()

numeros_no_duplicados_conjunto = numeros_no_duplicados(conjunto_numeros)
print("Números que no están duplicados en el conjunto:", numeros_no_duplicados_conjunto)
