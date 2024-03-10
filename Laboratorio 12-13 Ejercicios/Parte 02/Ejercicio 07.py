
## 7 Implementar una función que cuente la cantidad de nodos internos (que tienen al menos un hijo)

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def contar_nodos_internos(arbol):
    if arbol is None:
        return 0
    elif arbol.izquierda is not None or arbol.derecha is not None:
        return 1 + contar_nodos_internos(arbol.izquierda) + contar_nodos_internos(arbol.derecha)
    else:
        return 0

# Ejemplo de uso
# Creamos un árbol de ejemplo
arbol = Nodo(1)
arbol.izquierda = Nodo(2)
arbol.derecha = Nodo(3)
arbol.izquierda.izquierda = Nodo(4)
arbol.izquierda.derecha = Nodo(5)
arbol.derecha.izquierda = Nodo(6)
arbol.derecha.derecha = Nodo(7)
arbol.derecha.derecha.izquierda = Nodo(8)

# Contamos la cantidad de nodos internos en el árbol
cantidad_nodos_internos = contar_nodos_internos(arbol)
print("Cantidad de nodos internos en el árbol:", cantidad_nodos_internos)
