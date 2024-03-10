
##  Validar la edad de un usuario.

def validar_edad(edad):
    try:
        edad = int(edad)
        assert edad >= 0, "La edad no puede ser un número negativo."
        assert edad >= 18, "Debes ser mayor de edad para acceder."
        assert edad <= 120, "Edad no válida. Verifica tu edad e intenta nuevamente."
        return True, "Edad válida. Puedes continuar."
    except ValueError:
        return False, "Por favor, ingresa un número entero como edad."
    except AssertionError as error:
        return False, str(error)

while True:
    edad_usuario = input("Por favor, ingresa tu edad: ")

    es_valida, mensaje = validar_edad(edad_usuario)

    if es_valida:
        print(mensaje)
        break
    else:
        print("Error:", mensaje)

