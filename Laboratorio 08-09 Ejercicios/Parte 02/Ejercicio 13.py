
## Implementa una función que concatene dos listas enlazadas simples.

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

    def concatenar(self, otra_lista):
        if self.cabeza is None:
            self.cabeza = otra_lista.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = otra_lista.cabeza

lista1 = ListaEnlazada()
lista1.insertar(1)
lista1.insertar(2)
lista1.insertar(3)

lista2 = ListaEnlazada()
lista2.insertar(4)
lista2.insertar(5)
lista2.insertar(6)

print("Lista 1:")
actual = lista1.cabeza
while actual is not None:
    print(actual.dato, end=" -> ")
    actual = actual.siguiente
print("None")

print("Lista 2:")
actual = lista2.cabeza
while actual is not None:
    print(actual.dato, end=" -> ")
    actual = actual.siguiente
print("None")

# Concatenar lista1 y lista2
lista1.concatenar(lista2)

print("Lista concatenada:")
actual = lista1.cabeza
while actual is not None:
    print(actual.dato, end=" -> ")
    actual = actual.siguiente
print("None")
