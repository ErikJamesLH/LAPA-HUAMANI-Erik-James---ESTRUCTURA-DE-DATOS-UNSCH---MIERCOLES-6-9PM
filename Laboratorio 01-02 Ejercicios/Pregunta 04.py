
## Crea una función que calcule la factorial de un número

def factorial(n):
    if n < 0:
        return "No se puede calcular el factorial de un número negativo"
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# Ejemplo de uso
numero = int(input("Ingrese un número entero para calcular su factorial: "))
print("El factorial de es:", factorial(numero))
