
## Pide la base y la altura de un triángulo al usuario y calcula su área

def calcular_area_triangulo():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))

    # Calcular el área del triángulo
    area = (base * altura) / 2

    print("El área del triángulo es:", area)

calcular_area_triangulo()
