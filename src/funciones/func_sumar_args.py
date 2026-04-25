# Ejercicio: Uso de *args

def sumar(*numeros):
    # Suma todos los números recibidos
    total = 0
    for n in numeros:
        total += n
    return total

print(sumar(1, 2, 3))
print(sumar(5, 10, 15, 20))