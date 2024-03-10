
## Insertar Nodo en Posición Específica:
## 3. Crea una lista con al menos 5 nodos, inserta un nuevo nodo con el dato 15 en la posición 3 e imprime la  lista hacia adelante y hacia atrás.

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

    def insertar_en_posicion(self, dato, posicion):
        nuevo_nodo = Nodo(dato)
        if posicion == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            contador = 0
            while contador < posicion - 1:
                actual = actual.siguiente
                contador += 1
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

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
for dato in range(1, 6):
    lista.insertar(dato)

# Insertar nodo en posición específica
dato_nuevo = 15
posicion_nuevo_nodo = 2
lista.insertar_en_posicion(dato_nuevo, posicion_nuevo_nodo)

print("Lista hacia adelante:")
lista.imprimir_adelante()
print("Lista hacia atrás:")
lista.imprimir_atras()
