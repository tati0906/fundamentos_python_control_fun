# Ejercicio: Combinar parámetros

def calcular_pago(horas, tarifa=15, moneda="USD"):
    # Calcula el pago total
    total = horas * tarifa
    return f"{total} {moneda}"

print(calcular_pago(40))
print(calcular_pago(30, 20))
print(calcular_pago(25, moneda="EUR"))