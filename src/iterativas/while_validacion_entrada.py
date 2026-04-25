# Este programa solicita al usuario un número hasta que ingrese un valor válido

# Se inicializa la variable entrada como cadena vacía
entrada = ""

# El bucle se ejecuta mientras la entrada NO sea un número
while not entrada.isdigit():
    # Se pide al usuario que introduzca un número
    entrada = input("Introduce un número: ")

# Cuando la condición deja de cumplirse (es número), se imprime el valor
print(f"Has introducido el número: {entrada}")