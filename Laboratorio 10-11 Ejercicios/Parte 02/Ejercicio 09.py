
## Validar operadores anidados:
## 9. Verificar si los operadores en una expresión matemática están correctamente anidados utilizando una 
## pila.

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

def operadores_anidados(expresion):
    pila = Pila()
    operadores_abiertos = "([{"
    operadores_cerrados = ")]}"

    for caracter in expresion:
        if caracter in operadores_abiertos:
            pila.apilar(caracter)
        elif caracter in operadores_cerrados:
            if pila.esta_vacia():
                return False
            else:
                ultimo_operador = pila.desapilar()
                if operadores_abiertos.index(ultimo_operador) != operadores_cerrados.index(caracter):
                    return False

    return pila.esta_vacia()

expresion1 = "((3 + 4) * 2)"
expresion2 = "{[5 - 3] / 2}"
expresion3 = "(2 * 3] - 5)"

print("La expresión 1 está correctamente anidada:", operadores_anidados(expresion1))
print("La expresión 2 está correctamente anidada:", operadores_anidados(expresion2))
print("La expresión 3 está correctamente anidada:", operadores_anidados(expresion3))
