
## Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que contienen una letra determinada

def palabras_con_letra_determinada(conjunto_palabras, letra):
    palabras_con_letra = set()
    for palabra in conjunto_palabras:
        if letra in palabra:
            palabras_con_letra.add(palabra)
    return palabras_con_letra

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

palabras_con_letra = palabras_con_letra_determinada(conjunto_palabras, letra)
print(f"Palabras que contienen la letra '{letra}': {palabras_con_letra}")
