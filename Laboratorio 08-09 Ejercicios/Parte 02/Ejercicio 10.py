
## Desarrollar el código de buscar nodo en la lista enlazada simple

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

    def buscar(self, dato):
        actual = self.cabeza
        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

lista = ListaEnlazada()
lista.insertar(5)
lista.insertar(10)
lista.insertar(15)

dato_buscar = 10
if lista.buscar(dato_buscar):
    print(f"El nodo con el dato {dato_buscar} se encuentra en la lista.")
else:
    print(f"El nodo con el dato {dato_buscar} no se encuentra en la lista.")
