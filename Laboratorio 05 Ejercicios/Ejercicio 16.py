
## Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son  palíndromos y están ordenadas de menor a mayor

def es_palindromo(palabra):
    return palabra == palabra[::-1]

def palabras_palindromas_ordenadas(conjunto_palabras):
    palindromos_ordenados = set()
    for palabra in sorted(conjunto_palabras):
        if es_palindromo(palabra):
            palindromos_ordenados.add(palabra)
    return palindromos_ordenados

def obtener_conjunto_palabras_del_usuario():
    conjunto_palabras = set()
    cantidad_palabras = int(input("Ingrese la cantidad de palabras en el conjunto: "))
    print("Ingrese las palabras:")
    for i in range(cantidad_palabras):
        palabra = input(f"Ingrese la palabra {i + 1}: ").strip().lower()
        conjunto_palabras.add(palabra)
    return conjunto_palabras

conjunto_palabras = obtener_conjunto_palabras_del_usuario()

palindromos_ordenados_conjunto = palabras_palindromas_ordenadas(conjunto_palabras)
print("Palíndromos ordenados de menor a mayor:", palindromos_ordenados_conjunto)
