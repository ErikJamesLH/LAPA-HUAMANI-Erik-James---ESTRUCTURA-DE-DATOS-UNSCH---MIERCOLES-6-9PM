
## Ordenar una pila:
## 10. Ordenar los elementos de una pila de manera ascendente utilizando estructuras adicionales.

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

def ordenar_pila(pila):
    pila_ordenada = Pila()

    while not pila.esta_vacia():
        temp = pila.desapilar()

        while not pila_ordenada.esta_vacia() and pila_ordenada.items[-1] > temp:
            pila.apilar(pila_ordenada.desapilar())

        pila_ordenada.apilar(temp)

    return pila_ordenada

# Ejemplo de uso
pila = Pila()
elementos = [5, 3, 8, 1, 6]

for elemento in elementos:
    pila.apilar(elemento)

pila_ordenada = ordenar_pila(pila)

print("Pila original:")
while not pila.esta_vacia():
    print(pila.desapilar(), end=" ")

print("\nPila ordenada:")
while not pila_ordenada.esta_vacia():
    print(pila_ordenada.desapilar(), end=" ")
