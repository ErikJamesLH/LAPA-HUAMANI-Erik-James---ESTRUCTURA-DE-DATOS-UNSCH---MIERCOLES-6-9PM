
## Calcula la suma de los números pares en un rango especificado por el usuario.

def suma_pares_en_rango(inicio, fin):
    suma = 0
    for num in range(inicio, fin + 1):
        if num % 2 == 0:
            suma += num
    return suma


inicio = int(input("Ingrese el número de inicio del rango: "))
fin = int(input("Ingrese el número final del rango: "))

resultado = suma_pares_en_rango(inicio, fin)
print("La suma de los números pares en el rango de", inicio, "a", fin, "es:", resultado)
