# Este programa clasifica números como pares o impares usando ternarios en una lista

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Se crea una nueva lista usando comprensión de listas
# Para cada número:
# - Si es par → "par"
# - Si no → "impar"
paridad = ["par" if n % 2 == 0 else "impar" for n in numeros]

print(paridad)