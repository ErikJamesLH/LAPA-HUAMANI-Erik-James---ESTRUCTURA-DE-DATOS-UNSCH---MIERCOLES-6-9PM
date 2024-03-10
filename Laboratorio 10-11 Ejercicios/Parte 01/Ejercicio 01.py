
## Crea una lista con al menos 4 nodos, duplica cada nodo de la lista e imprime la lista original y la lista duplicada hacia adelante y hacia atrás

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

    def duplicar_nodos(self):
        actual = self.cabeza
        while actual is not None:
            nuevo_nodo = Nodo(actual.dato)
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
            actual = nuevo_nodo.siguiente

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
lista_original = ListaEnlazada()
lista_original.insertar(1)
lista_original.insertar(2)
lista_original.insertar(3)
lista_original.insertar(4)

# Duplicar nodos
lista_original.duplicar_nodos()

print("Lista Original hacia adelante:")
lista_original.imprimir_adelante()
print("Lista Original hacia atrás:")
lista_original.imprimir_atras()

