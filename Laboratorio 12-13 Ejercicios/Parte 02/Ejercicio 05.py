
## Contar nodos:
## 5. Implementar una función que cuente la cantidad de nodos en el árbol

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def contar_nodos(arbol):
    if arbol is None:
        return 0
    else:
        return 1 + contar_nodos(arbol.izquierda) + contar_nodos(arbol.derecha)

# Ejemplo de uso
# Creamos un árbol de ejemplo
arbol = Nodo(1)
arbol.izquierda = Nodo(2)
arbol.derecha = Nodo(3)
arbol.izquierda.izquierda = Nodo(4)
arbol.izquierda.derecha = Nodo(5)
arbol.derecha.izquierda = Nodo(6)

# Contamos la cantidad de nodos en el árbol
cantidad_nodos = contar_nodos(arbol)
print("Cantidad de nodos en el árbol:", cantidad_nodos)
