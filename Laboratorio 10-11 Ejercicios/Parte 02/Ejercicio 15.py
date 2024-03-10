
## Simular el proceso de deshacer (undo):
## 14. Implementar un sistema simple de "deshacer" utilizando dos pilas, una para las acciones y otra para los 
## deshaceres

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

def deshacer(acciones, deshaceres):
    if not acciones.esta_vacia():
        accion_deshacer = acciones.desapilar()
        deshaceres.apilar(accion_deshacer)
        print(f"Deshaciendo: {accion_deshacer}")
    else:
        print("No hay acciones para deshacer.")

def rehacer(acciones, deshaceres):
    if not deshaceres.esta_vacia():
        accion_rehacer = deshaceres.desapilar()
        acciones.apilar(accion_rehacer)
        print(f"Rehaciendo: {accion_rehacer}")
    else:
        print("No hay acciones para rehacer.")

acciones = Pila()
deshaceres = Pila()

acciones.apilar("Escribir texto")
acciones.apilar("Eliminar texto")
acciones.apilar("Copiar texto")

deshacer(acciones, deshaceres)  # Deshacer: Copiar texto
rehacer(acciones, deshaceres)   # Rehacer: Copiar texto
