
## Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están en el segundo conjunto pero no en el primero.

def obtener_conjuntos():
    conjunto1 = obtener_conjunto("primer")
    conjunto2 = obtener_conjunto("segundo")
    return conjunto1, conjunto2

def obtener_conjunto(nombre):
    conjunto = set()
    cantidad = int(input(f"Ingrese la cantidad de números en el {nombre} conjunto: "))
    print(f"Ingrese los {cantidad} números del {nombre} conjunto:")
    for i in range(cantidad):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        conjunto.add(numero)
    return conjunto

def numeros_en_segundo_conjunto_no_en_primero(conjunto1, conjunto2):
    return conjunto2.difference(conjunto1)

# Ejemplo de uso
conjunto1, conjunto2 = obtener_conjuntos()

numeros_en_segundo_no_en_primero = numeros_en_segundo_conjunto_no_en_primero(conjunto1, conjunto2)
print("Números en el segundo conjunto pero no en el primero:", numeros_en_segundo_no_en_primero)
