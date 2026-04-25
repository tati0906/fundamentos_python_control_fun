# Variable inicial vacía
entrada = ""

# El bucle se ejecuta mientras la entrada NO sea un número
while not entrada.isdigit():
    # Solicita al usuario que ingrese un número
    entrada = input("Introduce un número: ")

# Cuando la condición deja de cumplirse, se imprime el valor válido
print(f"Has introducido el número: {entrada}")