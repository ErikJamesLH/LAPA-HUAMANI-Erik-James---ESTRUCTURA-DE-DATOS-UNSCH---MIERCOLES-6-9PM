
## Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos, tienen una longitud determinada y están ordenadas de menor a mayor

def palabras_palindromos_longitud_ordenadas(conjunto_palabras, longitud):
    palindromos_filtrados = set()
    for palabra in sorted(conjunto_palabras):
        if len(palabra) == longitud and palabra == palabra[::-1]:
            palindromos_filtrados.add(palabra)
    return palindromos_filtrados

def obtener_conjunto_palabras_del_usuario():
    conjunto_palabras = set()
    cantidad_palabras = int(input("Ingrese la cantidad de palabras en el conjunto: "))
    print("Ingrese las palabras:")
    for i in range(cantidad_palabras):
        palabra = input(f"Ingrese la palabra {i + 1}: ").strip().lower()
        conjunto_palabras.add(palabra)
    return conjunto_palabras

conjunto_palabras = obtener_conjunto_palabras_del_usuario()
longitud = int(input("Ingrese la longitud de las palabras que desea buscar: "))

palindromos_longitud_ordenados = palabras_palindromos_longitud_ordenadas(conjunto_palabras, longitud)
print(f"Palíndromos de longitud {longitud} y ordenados de menor a mayor:", palindromos_longitud_ordenados)
