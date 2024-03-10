
## Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos.

def obtener_palabras_palindromas(conjunto_palabras):
    palindromos = set()
    for palabra in conjunto_palabras:
        if palabra == palabra[::-1]: 
            palindromos.add(palabra)
    return palindromos

def obtener_conjunto_palabras_del_usuario():
    conjunto_palabras = set()
    cantidad_palabras = int(input("Ingrese la cantidad de palabras en el conjunto: "))
    print("Ingrese las palabras:")
    for i in range(cantidad_palabras):
        palabra = input(f"Ingrese la palabra {i + 1}: ").strip().lower()
        conjunto_palabras.add(palabra)
    return conjunto_palabras

conjunto_palabras = obtener_conjunto_palabras_del_usuario()
palabras_palindromas = obtener_palabras_palindromas(conjunto_palabras)

print("Palabras que son palíndromos:")
for palabra in palabras_palindromas:
    print(palabra)
