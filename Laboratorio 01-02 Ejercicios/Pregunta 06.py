
## Toma una cadena de texto y muestra su inversión.

cadena_original = input("Ingrese una cadena de texto para invertir: ")
cadena_invertida = ""

# Iterar sobre la cadena original en orden inverso
for i in range(len(cadena_original) - 1, -1, -1):
    # Agregar cada carácter al principio de la cadena invertida
    cadena_invertida += cadena_original[i]

print(f"Inversión de la cadena: {cadena_invertida}")

