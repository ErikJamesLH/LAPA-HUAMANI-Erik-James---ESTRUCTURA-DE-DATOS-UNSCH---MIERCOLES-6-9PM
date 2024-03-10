
## Eliminar Nodos Duplicados:
## 4. Crea una lista con nodos que contengan datos duplicados, elimina todos los nodos duplicados, dejando 
## solo una instancia de cada dato e imprime la lista hacia adelante y hacia atrás.

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

# Crear lista con nodos que contienen datos duplicados
lista = ListaEnlazada()
datos = [1, 2, 2, 3, 4, 4, 4, 5]
for dato in datos:
    lista.insertar(dato)

# Eliminar nodos duplicados
lista.eliminar_duplicados()

# Imprimir la lista
print("Lista hacia adelante:")
lista.imprimir_adelante()
print("Lista hacia atrás:")
lista.imprimir_atras()
