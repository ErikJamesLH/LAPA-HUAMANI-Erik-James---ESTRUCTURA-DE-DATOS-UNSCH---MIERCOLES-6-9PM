
## Pide el radio de un círculo al usuario y calcula su área.

import math

def area_circulo(radio):
    return math.pi * radio**2

radio_circulo = float(input("Ingrese el radio de un círculo para calcular su área: "))
print(f"El área del círculo es: {area_circulo(radio_circulo)}")
