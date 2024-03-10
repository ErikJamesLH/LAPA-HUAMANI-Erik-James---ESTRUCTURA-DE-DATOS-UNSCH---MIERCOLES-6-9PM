
## Validar el estado de una variable después de una operación.

# Definir una variable inicial
variable = 5

variable = variable * 2  # Por ejemplo, multiplicar por 2

valor_esperado = 10

if variable == valor_esperado:
    print("El estado de la variable después de la operación es el esperado:", valor_esperado)
else:
    print("Error: El estado de la variable después de la operación no es el esperado.")
