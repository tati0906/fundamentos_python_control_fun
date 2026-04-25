# Ejercicio: Separar lógica y salida

def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

notas = [3, 4, 5]
print(calcular_promedio(notas))