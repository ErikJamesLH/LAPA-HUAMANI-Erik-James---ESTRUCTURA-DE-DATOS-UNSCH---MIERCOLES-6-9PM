
## Ejercicio 2: Escribe una función recursiva que imprima la suma de los números del 1 al n.

def suma_hasta_n_recursivo(n):
    if n == 1:
        return 1
    return n + suma_hasta_n_recursivo(n - 1)

resultado = suma_hasta_n_recursivo(100)
print(resultado)
