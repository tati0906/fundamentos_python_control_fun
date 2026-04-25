# Ejercicio: Return anticipado

def dividir_seguro(a, b):
    if b == 0:
        print("Error: división por cero")
        return None

    return a / b

print(dividir_seguro(10, 2))
print(dividir_seguro(10, 0))