
## Invertir la Lista:
## 5. Crea una lista con al menos 6 nodos, invierte el orden de la lista (el último elemento se convierte en el 
## primero y viceversa) e imprime la lista hacia adelante y hacia atrás

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

# Crear lista con al menos 6 nodos
lista = ListaEnlazada()
datos = [1, 2, 3, 4, 5, 6]
for dato in datos:
    lista.insertar(dato)

# Invertir la lista
lista.invertir()

print("Lista hacia adelante:")
lista.imprimir_adelante()
print("Lista hacia atrás:")
lista.imprimir_atras()
