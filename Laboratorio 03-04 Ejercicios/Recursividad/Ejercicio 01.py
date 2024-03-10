
## Ejercicio 1: Escribe una función recursiva que imprima los números pares del 1 al 100.

def imprimir_pares_recursivo(n):
    if n > 0:
        imprimir_pares_recursivo(n - 1)
        if n % 2 == 0:
            print(n)

imprimir_pares_recursivo(100)
