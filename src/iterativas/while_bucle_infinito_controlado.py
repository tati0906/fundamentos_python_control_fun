# Este programa muestra un ejemplo de bucle infinito controlado con break

while True:
    # Se solicita al usuario si desea continuar
    respuesta = input("¿Quieres continuar? (s/n): ").lower()

    # Si el usuario escribe 'n', se termina el programa
    if respuesta == "n":
        print("Programa finalizado.")
        break

    # Si el usuario escribe 's', continúa el bucle
    if respuesta == "s":
        print("Continuando...")
    else:
        # Si la respuesta no es válida
        print("Respuesta no válida. Introduce 's' o 'n'.")