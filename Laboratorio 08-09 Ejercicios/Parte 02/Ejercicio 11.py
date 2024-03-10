
## Implementa una función que sume todos los nodos de una lista enlazada simple.

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

    def sumar_nodos(self):
        suma = 0
        actual = self.cabeza
        while actual is not None:
            suma += actual.dato
            actual = actual.siguiente
        return suma

lista = ListaEnlazada()
lista.insertar(5)
lista.insertar(10)
lista.insertar(15)

suma_total = lista.sumar_nodos()
print("La suma de todos los nodos de la lista enlazada es:", suma_total)
