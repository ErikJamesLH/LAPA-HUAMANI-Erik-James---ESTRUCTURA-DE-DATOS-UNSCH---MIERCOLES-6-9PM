
##  Asegurar que una función retorna un valor específico.

def funcion_ejemplo():
    resultado = 42
    
    return resultado

valor_esperado = 42
valor_retornado = funcion_ejemplo()

if valor_retornado == valor_esperado:
    print("La función retornó el valor esperado:", valor_esperado)
else:
    print("Error: La función no retornó el valor esperado.")
