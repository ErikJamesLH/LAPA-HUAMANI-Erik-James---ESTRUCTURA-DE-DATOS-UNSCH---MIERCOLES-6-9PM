
## Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que  tienen una longitud determinada y están ordenadas de menor a mayor

def palabras_con_longitud_ordenadas(conjunto_palabras, longitud):
    palabras_filtradas = set()
    for palabra in sorted(conjunto_palabras):
        if len(palabra) == longitud:
            palabras_filtradas.add(palabra)
    return palabras_filtradas

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

palabras_longitud_ordenadas = palabras_con_longitud_ordenadas(conjunto_palabras, longitud)
print(f"Palabras de longitud {longitud} y ordenadas de menor a mayor:", palabras_longitud_ordenadas)
