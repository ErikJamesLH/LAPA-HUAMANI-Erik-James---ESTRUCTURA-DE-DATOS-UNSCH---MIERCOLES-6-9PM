
## 9 Implementar una función que calcule la profundidad de un nodo (la longitud del camino desde la raíz 
## hasta el nodo).

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def calcular_profundidad(arbol, valor_nodo, profundidad_actual=0):
    if arbol is None:
        return -1  # El nodo no se encuentra en el árbol

    if arbol.valor == valor_nodo:
        return profundidad_actual

    profundidad_izquierda = calcular_profundidad(arbol.izquierda, valor_nodo, profundidad_actual + 1)
    if profundidad_izquierda != -1:
        return profundidad_izquierda

    profundidad_derecha = calcular_profundidad(arbol.derecha, valor_nodo, profundidad_actual + 1)
    return profundidad_derecha

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

# Calculamos la profundidad del nodo con valor 8
valor_nodo = 8
profundidad_nodo = calcular_profundidad(arbol, valor_nodo)
if profundidad_nodo != -1:
    print(f"La profundidad del nodo con valor {valor_nodo} es:", profundidad_nodo)
else:
    print(f"No se encontró el nodo con valor {valor_nodo} en el árbol.")
