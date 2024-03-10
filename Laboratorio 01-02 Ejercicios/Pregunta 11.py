
## Ordena una lista de números ingresados por el usuario de menor a mayor.

def ordenar_lista(lista):
    n = len(lista)

    # Iterar sobre la lista
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

    return lista

numeros = input("Ingrese números separados por espacio para ordenar: ").split()
lista_desordenada = [int(x) for x in numeros]

print("Lista ordenada:", ordenar_lista(lista_desordenada))
