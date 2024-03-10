
## Crea una función que devuelva la longitud de una lista enlazada simple

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

    def longitud(self):
        longitud = 0
        actual = self.cabeza
        while actual is not None:
            longitud += 1
            actual = actual.siguiente
        return longitud

lista = ListaEnlazada()
lista.insertar(5)
lista.insertar(10)
lista.insertar(15)

longitud_lista = lista.longitud()
print("La longitud de la lista enlazada es:", longitud_lista)
