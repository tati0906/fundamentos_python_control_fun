# Bucle infinito controlado con break
while True:
    # Solicita una respuesta al usuario
    respuesta = input("¿Quieres continuar? (s/n): ").lower()

    # Si el usuario responde "n", se termina el programa
    if respuesta == "n":
        print("Programa finalizado.")
        break

    # Si responde "s", continúa
    if respuesta == "s":
        print("Continuando...")
    else:
        # Maneja respuestas inválidas
        print("Respuesta no válida. Introduce 's' o 'n'.")