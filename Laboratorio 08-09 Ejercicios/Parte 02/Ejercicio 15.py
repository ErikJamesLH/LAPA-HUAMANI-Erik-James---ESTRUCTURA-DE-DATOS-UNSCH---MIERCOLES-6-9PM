
## Implementa una función que invierta el orden de una lista enlazada simple

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

    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual is not None:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior

    def imprimir(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

lista = ListaEnlazada()
lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
lista.insertar(4)

print("Lista original:")
lista.imprimir()

lista.invertir()

print("Lista invertida:")
lista.imprimir()
