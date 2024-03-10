
## Implementar una calculadora sencilla:
## 12. Crear una calculadora que pueda realizar operaciones básicas (+, -, *, /) utilizando una pila para evaluar 
## expresiones.

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

def calcular(expresion):
    pila = Pila()
    operadores = {'+', '-', '*', '/'}

    for caracter in expresion.split():
        if caracter not in operadores:
            pila.apilar(float(caracter))
        else:
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()

            if caracter == '+':
                resultado = operando1 + operando2
            elif caracter == '-':
                resultado = operando1 - operando2
            elif caracter == '*':
                resultado = operando1 * operando2
            elif caracter == '/':
                if operando2 == 0:
                    return "Error: División por cero"
                resultado = operando1 / operando2

            pila.apilar(resultado)

    return pila.desapilar()

# Ejemplo de uso
expresion = "3 4 + 2 *"
resultado = calcular(expresion)
print("El resultado de la expresión es:", resultado)
