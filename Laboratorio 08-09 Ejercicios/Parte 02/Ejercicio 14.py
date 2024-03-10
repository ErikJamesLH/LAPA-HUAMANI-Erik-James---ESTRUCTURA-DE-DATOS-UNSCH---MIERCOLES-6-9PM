
## Crea una función que elimine los nodos duplicados de una lista enlazada simple

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

    def eliminar_duplicados(self):
        if self.cabeza is None:
            return

        nodos_vistos = set()
        previo = None
        actual = self.cabeza

        while actual is not None:
            if actual.dato in nodos_vistos:
                previo.siguiente = actual.siguiente
            else:
                nodos_vistos.add(actual.dato)
                previo = actual
            actual = actual.siguiente

lista = ListaEnlazada()
lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
lista.insertar(2)
lista.insertar(4)
lista.insertar(1)

print("Lista antes de eliminar duplicados:")
actual = lista.cabeza
while actual is not None:
    print(actual.dato, end=" -> ")
    actual = actual.siguiente
print("None")

lista.eliminar_duplicados()

print("Lista después de eliminar duplicados:")
actual = lista.cabeza
while actual is not None:
    print(actual.dato, end=" -> ")
    actual = actual.siguiente
print("None")
