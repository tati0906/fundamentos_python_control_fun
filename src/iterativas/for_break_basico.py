# Este programa muestra el uso de break en un bucle for

for numero in range(1, 11):
    # Si el número es 5, se interrumpe el bucle
    if numero == 5:
        print("¡Encontrado el 5! Saliendo del bucle...")
        break

    # Se imprime el número actual mientras no sea 5
    print(f"Número actual: {numero}")

# Este mensaje se imprime después de salir del bucle
print("Bucle terminado")