
## Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que son divisibles por un número determinado.

def numeros_divisibles_por_numero(conjunto_numeros, divisor):
    numeros_divisibles = set()
    for numero in conjunto_numeros:
        if numero % divisor == 0:
            numeros_divisibles.add(numero)
    return numeros_divisibles

conjunto_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
divisor = 3

numeros_divisibles = numeros_divisibles_por_numero(conjunto_numeros, divisor)
print("Números divisibles por", divisor, ":", numeros_divisibles)
