# Ejemplo de un bucle infinito por error (NO incrementa la variable)

contador = 1

while contador <= 5:
    print(contador)
    # ERROR: falta actualizar contador, esto genera un bucle infinito