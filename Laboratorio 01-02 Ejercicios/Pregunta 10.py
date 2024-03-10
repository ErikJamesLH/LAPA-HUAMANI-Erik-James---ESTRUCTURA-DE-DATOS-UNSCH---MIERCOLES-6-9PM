
## Genera los primeros 10 números de la serie Fibonacci

def fibonacci(n):
    if n <= 0:
        return []
    
    elif n == 1:
        return [0]

    elif n == 2:
        return [0, 1]
    
    else:
        fib = [0, 1]
        for _ in range(2, n):
            # Agregar el siguiente número en la serie como la suma de los dos últimos números
            fib.append(fib[-1] + fib[-2])
        # Retornar la lista de Fibonacci completa
        return fib

# Imprimir
print("Primeros 10 números de la serie Fibonacci:", fibonacci(10))
