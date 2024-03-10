
## Toma un número entero y calcula la suma de sus dígitos

def suma_digitos(numero):
    numero = abs(numero)
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    return suma

num_suma_digitos = int(input("Ingrese un número entero para calcular la suma de sus dígitos: "))
print(f"La suma de los dígitos es: {suma_digitos(num_suma_digitos)}")
