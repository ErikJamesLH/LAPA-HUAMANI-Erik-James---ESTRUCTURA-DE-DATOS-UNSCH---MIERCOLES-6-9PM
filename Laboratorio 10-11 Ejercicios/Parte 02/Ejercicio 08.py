
## Evaluar expresión posfija:
## 8. Crear un programa que evalúe una expresión matemática en notación posfija utilizando una pila.

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()


def evaluar_expresion_posfija(expresion):
    pila = Pila()
    operadores = {'+', '-', '*', '/'}

    for elemento in expresion.split():
        if elemento not in operadores:
            pila.apilar(float(elemento))
        else:
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()

            if elemento == '+':
                resultado = operando1 + operando2
            elif elemento == '-':
                resultado = operando1 - operando2
            elif elemento == '*':
                resultado = operando1 * operando2
            elif elemento == '/':
                resultado = operando1 / operando2

            pila.apilar(resultado)

    return pila.desapilar()

expresion_posfija = "3 4 + 2 *"
resultado = evaluar_expresion_posfija(expresion_posfija)
print("El resultado de la expresión posfija es:", resultado)
