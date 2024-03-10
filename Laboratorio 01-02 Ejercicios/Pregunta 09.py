
## Cuenta el número de vocales en una cadena de texto

def contar_vocales(cadena):
    cadena = cadena.lower()
    vocales = ['a', 'e', 'i', 'o', 'u']
    contador = 0
    # Recorrer cada carácter en la cadena
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador

texto = input("Ingrese una cadena de texto para contar las vocales: ")
print("El número de vocales en la cadena es:", contar_vocales(texto))
