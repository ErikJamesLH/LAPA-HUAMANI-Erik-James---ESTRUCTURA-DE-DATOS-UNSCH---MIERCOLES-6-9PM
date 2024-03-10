
## Validar el rango de una calificación.

def validar_calificacion(calificacion, rango_minimo, rango_maximo):
    try:
        calificacion = float(calificacion)
        if calificacion < rango_minimo or calificacion > rango_maximo:
            return False, f"La calificación debe estar en el rango de {rango_minimo} a {rango_maximo}."
        else:
            return True, "Calificación válida. Puedes continuar."
    except ValueError:
        return False, "Por favor, ingresa una calificación válida como número."

rango_minimo = 0
rango_maximo = 20

while True:
    calificacion_usuario = input("Por favor, ingresa tu calificación: ")

    es_valida, mensaje = validar_calificacion(calificacion_usuario, rango_minimo, rango_maximo)

    if es_valida:
        print(mensaje)
        break
    else:
        print("Error:", mensaje)
