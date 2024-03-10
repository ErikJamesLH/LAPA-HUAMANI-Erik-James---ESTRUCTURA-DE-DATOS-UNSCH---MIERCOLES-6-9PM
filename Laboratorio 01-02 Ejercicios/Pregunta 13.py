
## Crea un programa que genere la tabla de multiplicar de un número ingresado por el usuario.

num_tabla_multiplicar = int(input("Ingrese un número para generar su tabla de multiplicar: "))

# Imprimir encabezado de la tabla
print(f"Tabla de multiplicar de {num_tabla_multiplicar}:")

# Generar y mostrar la tabla de multiplicar
for i in range(1, 13):
    resultado = num_tabla_multiplicar * i
    print(f"{num_tabla_multiplicar} x {i} = {resultado}")
