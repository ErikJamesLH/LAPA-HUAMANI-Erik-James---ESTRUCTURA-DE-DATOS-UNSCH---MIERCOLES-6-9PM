
## Asegurar que un ciclo while se ejecuta al menos una vez

def ejecutar_ciclo_al_menos_una_vez():
    continuar = True
    
    while continuar:
        respuesta = input("¿Quieres continuar? (s/n): ")
        if respuesta.lower() == 'n':
            continuar = False
            print("Saliendo del ciclo.")
        else:
            print("Continuando el ciclo.")

ejecutar_ciclo_al_menos_una_vez()
