# Genera una lista con los cuadrados del 1 al 5
# x toma valores de 1 a 5 y se eleva al cuadrado
cuadrados = [x**2 for x in range(1, 6)]

# Imprime la lista resultante
print(cuadrados)

# Genera una lista de números pares del 0 al 9
# Solo incluye valores donde x % 2 == 0
pares = [x for x in range(10) if x % 2 == 0]

# Imprime la lista de números pares
print(pares)