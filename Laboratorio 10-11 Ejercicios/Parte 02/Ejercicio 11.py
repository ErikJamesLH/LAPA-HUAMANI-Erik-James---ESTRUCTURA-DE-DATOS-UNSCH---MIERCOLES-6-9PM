
## Eliminar duplicados:
## 11. Eliminar los elementos duplicados de una pila

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

def eliminar_duplicados_pila(pila):
    conjunto = set()
    pila_sin_duplicados = Pila()

    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento not in conjunto:
            conjunto.add(elemento)
            pila_sin_duplicados.apilar(elemento)

    # Invertir la pila sin duplicados para mantener el orden original
    pila_temporal = Pila()
    while not pila_sin_duplicados.esta_vacia():
        pila_temporal.apilar(pila_sin_duplicados.desapilar())

    while not pila_temporal.esta_vacia():
        pila.apilar(pila_temporal.desapilar())

    return pila

# Ejemplo de uso
pila = Pila()
elementos = [3, 5, 2, 5, 7, 2, 8, 3]

for elemento in elementos:
    pila.apilar(elemento)

pila_sin_duplicados = eliminar_duplicados_pila(pila)

print("Pila original:")
while not pila.esta_vacia():
    print(pila.desapilar(), end=" ")

print("\nPila sin duplicados:")
while not pila_sin_duplicados.esta_vacia():
    print(pila_sin_duplicados.desapilar(), end=" ")
