
## Asegurar que una lista no esté vacía

lista = []

try:
    assert len(lista) > 0, "La lista está vacía"
except AssertionError:
    print("La lista está vacía, por favor, agregue elementos antes de continuar.")
    # Aquí puedes agregar el código para manejar la situación de lista vacía
