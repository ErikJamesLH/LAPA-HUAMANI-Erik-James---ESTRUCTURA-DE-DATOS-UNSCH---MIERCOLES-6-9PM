
## Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que contienen una letra determinada y están ordenadas de mayor a menor.

def palabras_con_letra_ordenadas(conjunto_palabras, letra):
    palabras_filtradas = set()
    for palabra in sorted(conjunto_palabras, reverse=True):
        if letra in palabra:
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
letra = input("Ingrese la letra que desea buscar: ").strip().lower()

palabras_con_letra_ordenadas = palabras_con_letra_ordenadas(conjunto_palabras, letra)
print(f"Palabras que contienen la letra '{letra}' y están ordenadas de mayor a menor:", palabras_con_letra_ordenadas)
