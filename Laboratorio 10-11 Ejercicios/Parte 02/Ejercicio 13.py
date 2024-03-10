
## Comprobar palíndromos:
## 13. Utilizar una pila para comprobar si una palabra o frase es un palíndromo.

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

def es_palindromo(palabra):
    pila = Pila()

    for caracter in palabra:
        pila.apilar(caracter)

    palabra_invertida = ""
    while not pila.esta_vacia():
        palabra_invertida += pila.desapilar()

    return palabra == palabra_invertida

# Ejemplo de uso
palabra = "reconocer"
if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')
