
## Ejercicio 4: Escribe una función recursiva que imprima la pirámide de números invertidos del 1 al n

def piramide_numeros_invertidos(n):
    if n < 1:
        return

    fila = list(range(n, 0, -1))
    print(' '.join(map(str, fila)))
    
    piramide_numeros_invertidos(n - 1)

n = int(input("Ingrese un número entero para la pirámide: "))
piramide_numeros_invertidos(n)
