
## Ejercicio parte 01 – Colas:
## Verificar si una palabra es palíndroma
## 1. Implementa una función que determine si una palabra es palíndroma o no. Utiliza una cola para 
## comparar los caracteres de la palabra en orden original y reverso.

from collections import deque

def es_palindromo(palabra):
    cola = deque()

    # Encolar cada caracter de la palabra original
    for caracter in palabra:
        cola.append(caracter)

    # Construir la palabra inversa desencolando los caracteres de la cola
    palabra_inversa = ""
    while cola:
        palabra_inversa += cola.pop()

    return palabra == palabra_inversa

palabra = "reconocer"
if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')
