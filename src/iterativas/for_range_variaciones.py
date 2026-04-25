# Números del 3 al 7
# range(3, 8) inicia en 3 y termina en 7
for i in range(3, 8):
    # end=" " permite imprimir en la misma línea separados por espacio
    print(i, end=" ")

# Imprime un salto de línea
print()

# Números pares del 2 al 10
# El tercer parámetro (2) indica el incremento
for i in range(2, 11, 2):
    print(i, end=" ")

print()

# Cuenta regresiva
# Empieza en 10, termina en 1 y decrementa de 1 en 1
for i in range(10, 0, -1):
    print(i, end=" ")