
## 6. Implementar una función que cuente la cantidad de nodos hoja (que no tienen hijos).

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def contar_nodos_hoja(arbol):
    if arbol is None:
        return 0
    elif arbol.izquierda is None and arbol.derecha is None:
        return 1
    else:
        return contar_nodos_hoja(arbol.izquierda) + contar_nodos_hoja(arbol.derecha)

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

# Contamos la cantidad de nodos hoja en el árbol
cantidad_nodos_hoja = contar_nodos_hoja(arbol)
print("Cantidad de nodos hoja en el árbol:", cantidad_nodos_hoja)
