
## Buscar el mínimo y el máximo:
## 10. Implementar una función que encuentre el nodo con el valor mínimo en el árbol

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def encontrar_valor_minimo(arbol):
    if arbol is None:
        return None

    nodo_actual = arbol
    while nodo_actual.izquierda is not None:
        nodo_actual = nodo_actual.izquierda

    return nodo_actual.valor

# Ejemplo de uso
# Creamos un árbol de ejemplo
arbol = Nodo(10)
arbol.izquierda = Nodo(5)
arbol.derecha = Nodo(15)
arbol.izquierda.izquierda = Nodo(3)
arbol.izquierda.derecha = Nodo(7)

# Encontramos el valor mínimo en el árbol
valor_minimo = encontrar_valor_minimo(arbol)
print("Valor mínimo en el árbol:", valor_minimo)
