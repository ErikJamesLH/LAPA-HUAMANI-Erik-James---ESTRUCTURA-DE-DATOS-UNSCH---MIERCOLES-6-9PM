
## Diseño de un sistema de gestión de pedidos
## 2. Crea un sistema de gestión de pedidos que utilice una cola para procesar los pedidos en el orden en que 
## fueron recibidos. Implementa funciones para agregar pedidos, procesar pedidos y mostrar el estado 
## actual de la cola

from collections import deque

class SistemaGestionPedidos:
    def __init__(self):
        self.cola_pedidos = deque()

    def agregar_pedido(self, pedido):
        self.cola_pedidos.append(pedido)
        print(f"Pedido añadido a la cola: {pedido}")

    def procesar_pedido(self):
        if self.cola_pedidos:
            pedido = self.cola_pedidos.popleft()
            print(f"Procesando pedido: {pedido}")
        else:
            print("No hay pedidos en la cola para procesar.")

    def mostrar_estado_cola(self):
        print("Estado actual de la cola de pedidos:")
        if self.cola_pedidos:
            for idx, pedido in enumerate(self.cola_pedidos, start=1):
                print(f"{idx}. {pedido}")
        else:
            print("La cola de pedidos está vacía.")

# Ejemplo de uso
sistema = SistemaGestionPedidos()

sistema.agregar_pedido("Pizza")
sistema.agregar_pedido("Hamburguesa")
sistema.agregar_pedido("Ensalada")

sistema.mostrar_estado_cola()

sistema.procesar_pedido()
sistema.procesar_pedido()
sistema.procesar_pedido()
sistema.procesar_pedido()

sistema.mostrar_estado_cola()
