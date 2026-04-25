# Este programa usa pass para no hacer nada en ciertos casos

for numero in range(1, 10):
    # Si el número es par, no se hace nada
    if numero % 2 == 0:
        pass
    else:
        # Se procesan solo números impares
        print(f"Procesando número impar: {numero}")