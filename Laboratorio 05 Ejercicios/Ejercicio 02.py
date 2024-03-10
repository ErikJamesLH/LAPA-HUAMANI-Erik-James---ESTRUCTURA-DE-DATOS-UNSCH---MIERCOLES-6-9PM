
## Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que comienzan con una letra determinada.

def palabras_que_comienzan_con_letra(conjunto_palabras, letra):
    palabras_comienzan_con_letra = set()
    for palabra in conjunto_palabras:
        if palabra.startswith(letra):
            palabras_comienzan_con_letra.add(palabra)
    return palabras_comienzan_con_letra

conjunto_palabras = {"manzana", "banana", "pera", "melón", "sandía", "naranja", "uva"}
letra = "m"

palabras_comienzan_m = palabras_que_comienzan_con_letra(conjunto_palabras, letra)
print("Palabras que comienzan con la letra 'm':", palabras_comienzan_m)
