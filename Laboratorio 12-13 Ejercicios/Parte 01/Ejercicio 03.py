
## Búsqueda de rutas en un laberinto
## 3. Desarrolla un programa que encuentre el camino más corto a través de un laberinto. Utiliza una cola 
## para realizar un recorrido en anchura (BFS) desde el punto de inicio hasta el punto de destino.

from collections import deque

def encontrar_camino_mas_corto(laberinto, inicio, destino):
    # Definir la cola para el recorrido BFS
    cola = deque([(inicio, [])])
    visitados = set()

    # Dimensiones del laberinto
    filas = len(laberinto)
    columnas = len(laberinto[0])

    # Direcciones para moverse (arriba, abajo, izquierda, derecha)
    movimientos = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    while cola:
        (fila, columna), camino = cola.popleft()

        # Si hemos llegado al destino, devolvemos el camino
        if (fila, columna) == destino:
            return camino + [(fila, columna)]

        # Marcar el nodo como visitado
        visitados.add((fila, columna))

        # Explorar los vecinos del nodo actual
        for mov in movimientos:
            fila_vecino = fila + mov[0]
            columna_vecino = columna + mov[1]

            # Verificar si el vecino está dentro de los límites del laberinto
            if 0 <= fila_vecino < filas and 0 <= columna_vecino < columnas:
                # Verificar si el vecino no está bloqueado y no ha sido visitado
                if laberinto[fila_vecino][columna_vecino] != '#' and (fila_vecino, columna_vecino) not in visitados:
                    cola.append(((fila_vecino, columna_vecino), camino + [(fila, columna)]))
                    visitados.add((fila_vecino, columna_vecino))

    return None

laberinto = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '#', '.', '.', '.', '#'],
    ['#', '#', '#', '.', '#', '.', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#']
]

inicio = (1, 1)
destino = (3, 7)

camino = encontrar_camino_mas_corto(laberinto, inicio, destino)

if camino:
    print("Camino más corto encontrado:")
    for fila, columna in camino:
        print(f"({fila}, {columna}) -> ", end="")
    print("Destino alcanzado!")
else:
    print("No se encontró un camino hasta el destino.")
