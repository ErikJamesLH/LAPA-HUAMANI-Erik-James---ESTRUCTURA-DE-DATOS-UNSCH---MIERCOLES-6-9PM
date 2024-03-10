
## Asegurar que un módulo se ha importado correctamente

try:
    import math
    print("El módulo 'math' se ha importado correctamente.")
except ImportError:
    print("Error al importar el módulo 'math'.")
