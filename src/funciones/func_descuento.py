# Ejercicio: Calcular precio con descuento usando parámetro por defecto

# Definimos la función con un valor por defecto (10%)
def calcular_descuento(precio, porcentaje=10):
    # Calculamos el valor del descuento
    descuento = precio * (porcentaje / 100)
    
    # Calculamos el precio final
    precio_final = precio - descuento
    
    # Retornamos el resultado
    return precio_final

# Llamamos la función sin especificar porcentaje (usa 10%)
print(calcular_descuento(100))

# Llamamos la función con un porcentaje personalizado
print(calcular_descuento(200, 20))