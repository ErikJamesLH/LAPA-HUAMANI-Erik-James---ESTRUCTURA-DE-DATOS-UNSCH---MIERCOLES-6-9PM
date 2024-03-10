
## Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son anagramas

def obtener_palabras_anagramas(conjunto_palabras):
    anagramas = set()
    palabras_procesadas = set()  # Para evitar comparar una palabra consigo misma
    for palabra in conjunto_palabras:
        if palabra in palabras_procesadas:
            continue
        palabras_procesadas.add(palabra)
        anagrama_encontrado = False
        for otra_palabra in conjunto_palabras:
            if otra_palabra != palabra and sorted(otra_palabra) == sorted(palabra):
                anagramas.add(palabra)
                anagramas.add(otra_palabra)
                anagrama_encontrado = True
        if not anagrama_encontrado:
            palabras_procesadas.add(palabra)
    return anagramas

def obtener_conjunto():
    conjunto_palabras = set()
    cantidad_palabras = int(input("Ingrese la cantidad de palabras en el conjunto: "))
    print("Ingrese las palabras:")
    for i in range(cantidad_palabras):
        palabra = input(f"Ingrese la palabra {i + 1}: ").strip().lower()
        conjunto_palabras.add(palabra)
    return conjunto_palabras

# Ejemplo de uso
conjunto_palabras = obtener_conjunto()
palabras_anagramas = obtener_palabras_anagramas(conjunto_palabras)

print("Palabras que son anagramas:")
for palabra in palabras_anagramas:
    print(palabra)
