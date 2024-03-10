
## Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que  tienen una longitud determinada.

def palabras_con_longitud_determinada(conjunto_palabras, longitud):
    palabras_longitud_determinada = set()
    for palabra in conjunto_palabras:
        if len(palabra) == longitud:
            palabras_longitud_determinada.add(palabra)
    return palabras_longitud_determinada

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

palabras_con_longitud = palabras_con_longitud_determinada(conjunto_palabras, longitud)
print(f"Palabras con longitud {longitud}: {palabras_con_longitud}")
