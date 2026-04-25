# Ejercicio: Calcular precio con impuesto

def calcular_precio_final(precio_base, impuesto):
    # Calcula el precio final sumando el impuesto
    return precio_base + (precio_base * impuesto)

# Uso
print(calcular_precio_final(100, 0.21))