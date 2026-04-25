# Ejercicio: Calcular el área de un rectángulo usando una función

# Definimos la función con parámetros (datos de entrada)
def calcular_area_rectangulo(base, altura):
    # Calculamos el área multiplicando base por altura
    area = base * altura
    
    # Retornamos el resultado
    return area

# Llamamos a la función y guardamos el resultado
resultado = calcular_area_rectangulo(5, 3)

# Mostramos el resultado en pantalla
print(f"El área del rectángulo es: {resultado}")