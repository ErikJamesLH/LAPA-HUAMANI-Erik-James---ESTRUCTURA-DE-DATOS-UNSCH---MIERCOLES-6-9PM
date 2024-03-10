
## Verifica si una palabra ingresada por el usuario es un palíndromo.

def es_palindromo(palabra):
    palabra = palabra.lower()
    # Eliminar los espacios en blanco de la palabra
    palabra_sin_espacios = palabra.replace(" ", "")
    # Verificar si la palabra sin espacios es igual a su inversa
    return palabra_sin_espacios == palabra_sin_espacios[::-1]

palabra = input("Ingrese una palabra para verificar si es un palíndromo: ")
if es_palindromo(palabra):
    print("La palabra", palabra, "es un palíndromo.")
else:
    print("La palabra", palabra, "no es un palíndromo.")
