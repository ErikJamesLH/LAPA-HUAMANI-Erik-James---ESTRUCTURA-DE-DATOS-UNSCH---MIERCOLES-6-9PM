
## Verifica si un número ingresado por el usuario es primo o no

num_primo = int(input("Ingrese un número para verificar si es primo: "))

# Verificar si el número es primo
if num_primo < 2:
    es_primo = False
else:
    es_primo = True
    for i in range(2, int(num_primo ** 0.5) + 1):
        if num_primo % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"{num_primo} es un número primo.")
else:
    print(f"{num_primo} no es un número primo.")
