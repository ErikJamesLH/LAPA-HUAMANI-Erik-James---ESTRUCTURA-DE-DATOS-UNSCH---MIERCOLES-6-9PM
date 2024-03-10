
## Validar la igualdad de dos objetos.

objeto1 = "Hola mundo"
objeto2 = "Holaaaaa"

try:
    # Verificar la igualdad de los objetos
    assert objeto1 == objeto2, "Los objetos no son iguales"
except AssertionError as e:
    print("Error:", e)
