
## Calcular altura y profundidad:
## 8. Implementar una función que calcule la altura del árbol (la longitud del camino más largo desde la raíz 
## hasta una hoja).

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def calcular_altura(arbol):
    if arbol is None:
        return 0
    else:
        altura_izquierda = calcular_altura(arbol.izquierda)
        altura_derecha = calcular_altura(arbol.derecha)

        return 1 + max(altura_izquierda, altura_derecha)

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

# Calculamos la altura del árbol
altura_arbol = calcular_altura(arbol)
print("Altura del árbol:", altura_arbol)
