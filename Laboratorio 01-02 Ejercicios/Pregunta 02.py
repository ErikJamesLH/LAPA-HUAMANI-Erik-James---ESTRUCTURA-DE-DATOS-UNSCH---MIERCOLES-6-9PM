
## Solicita un número al usuario y determina si es par o impar.

def par_impar():
    numero = int(input("Ingrese un número: "))

    # Verificar si el número es par o impar
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")

par_impar()
