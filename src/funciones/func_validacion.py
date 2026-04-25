# Ejercicio: Validar argumentos

def calcular_descuento(precio, porcentaje):
    # Validamos precio
    if precio < 0:
        raise ValueError("Precio inválido")

    # Validamos porcentaje
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("Porcentaje inválido")

    return precio - (precio * porcentaje / 100)

print(calcular_descuento(100, 10))