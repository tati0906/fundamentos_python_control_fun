# Ejercicio: Retornar múltiples valores

def estadisticas(lista):
    total = sum(lista)
    promedio = total / len(lista)
    minimo = min(lista)
    maximo = max(lista)

    return total, promedio, minimo, maximo

print(estadisticas([1, 2, 3, 4, 5]))