# Este programa muestra el uso de continue para saltar iteraciones

for numero in range(1, 11):
    # Si el número es par, se salta esta iteración
    if numero % 2 == 0:
        continue

    # Solo se imprimen números impares
    print(f"Número impar: {numero}")