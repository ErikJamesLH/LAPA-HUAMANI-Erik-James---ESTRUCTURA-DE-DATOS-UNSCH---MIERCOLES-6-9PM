
## Ejercicio 3: Escribe una función recursiva que imprima la pirámide de números del 1 al n

def piramide_numeros(n, i=1):
    if i > n:
        return
    else:
        # Imprimir los espacios en blanco
        print(" " * (n - i), end="")
        
        # Imprimir números ascendentes
        for j in range(1, i + 1):
            print(j, end="")
        
        # Imprimir números descendentes
        for j in range(i - 1, 0, -1):
            print(j, end="")
       
        print()
        piramide_numeros(n, i + 1)

n = int(input("Ingrese un número entero para la pirámide: "))
piramide_numeros(n)
