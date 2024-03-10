
## Contar Nodos Pares e Impares:
##2. Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato par y cuántos tienen un dato  impar e imprime la lista hacia adelante y hacia atrás.

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def contar_pares_impares(self):
        nodos_pares = 0
        nodos_impares = 0
        actual = self.cabeza
        while actual is not None:
            if actual.dato % 2 == 0:
                nodos_pares += 1
            else:
                nodos_impares += 1
            actual = actual.siguiente
        return nodos_pares, nodos_impares

    def imprimir_adelante(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def imprimir_atras(self):
        nodos = []
        actual = self.cabeza
        while actual is not None:
            nodos.append(actual.dato)
            actual = actual.siguiente
        nodos.reverse()
        for dato in nodos:
            print(dato, end=" -> ")
        print("None")

# Crear lista original
lista = ListaEnlazada()
for dato in range(1, 10):
    lista.insertar(dato)

# Contar nodos pares e impares
nodos_pares, nodos_impares = lista.contar_pares_impares()

# Imprimir la lista
print("Lista hacia adelante:")
lista.imprimir_adelante()
print("Lista hacia atrás:")
lista.imprimir_atras()

print(f"Cantidad de nodos pares: {nodos_pares}")
print(f"Cantidad de nodos impares: {nodos_impares}")
