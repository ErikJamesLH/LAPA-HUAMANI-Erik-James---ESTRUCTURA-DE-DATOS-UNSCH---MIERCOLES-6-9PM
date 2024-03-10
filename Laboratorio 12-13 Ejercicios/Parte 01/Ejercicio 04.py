
## Diseño de un sistema de gestión de tareas (Avanzado)
## 4. Implementa un sistema de gestión de tareas que permita agregar tareas, marcar tareas como 
## completadas y mostrar la próxima tarea pendiente.

class SistemaGestionTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, nombre):
        tarea = {"nombre": nombre, "completada": False}
        self.tareas.append(tarea)
        print(f"Tarea '{nombre}' agregada correctamente.")

    def marcar_tarea_completada(self, nombre):
        for tarea in self.tareas:
            if tarea["nombre"] == nombre:
                tarea["completada"] = True
                print(f"Tarea '{nombre}' marcada como completada.")
                return
        print(f"No se encontró la tarea '{nombre}'.")

    def mostrar_proxima_tarea_pendiente(self):
        for tarea in self.tareas:
            if not tarea["completada"]:
                print(f"Próxima tarea pendiente: '{tarea['nombre']}'")
                return
        print("No hay tareas pendientes.")

# Ejemplo de uso
sistema = SistemaGestionTareas()

sistema.agregar_tarea("Hacer la compra")
sistema.agregar_tarea("Llamar al cliente")
sistema.agregar_tarea("Enviar informe")

sistema.mostrar_proxima_tarea_pendiente()

sistema.marcar_tarea_completada("Hacer la compra")

sistema.mostrar_proxima_tarea_pendiente()
