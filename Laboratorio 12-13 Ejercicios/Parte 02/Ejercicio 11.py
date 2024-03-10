
## 11 Implementar una función que encuentre el nodo con el valor máximo en el árbol

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def encontrar_valor_maximo(arbol):
    if arbol is None:
        return None

    nodo_actual = arbol
    while nodo_actual.derecha is not None:
        nodo_actual = nodo_actual.derecha

    return nodo_actual.valor

# Ejemplo de uso
# Creamos un árbol de ejemplo
arbol = Nodo(10)
arbol.izquierda = Nodo(5)
arbol.derecha = Nodo(15)
arbol.izquierda.izquierda = Nodo(3)
arbol.izquierda.derecha = Nodo(7)
arbol.derecha.izquierda = Nodo(12)
arbol.derecha.derecha = Nodo(20)

# Encontramos el valor máximo en el árbol
valor_maximo = encontrar_valor_maximo(arbol)
print("Valor máximo en el árbol:", valor_maximo)
