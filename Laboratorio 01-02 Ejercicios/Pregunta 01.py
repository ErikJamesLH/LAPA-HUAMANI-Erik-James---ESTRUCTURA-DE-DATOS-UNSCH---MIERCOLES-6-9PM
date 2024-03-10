
## Realiza la suma, resta, multiplicación y división de dos números ingresados por el usuario

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

resultado_suma = suma(num1, num2)
resultado_resta = resta(num1, num2)
resultado_multiplicacion = multiplicacion(num1, num2)
resultado_division = division(num1, num2)

print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
print("Multiplicación:", resultado_multiplicacion)
print("División:", resultado_division)
