# Ejercicio: Convertir grados Celsius a Fahrenheit

# Definimos la función de conversión
def celsius_a_fahrenheit(celsius):
    # Aplicamos la fórmula de conversión
    return (celsius * 9/5) + 32

# Llamamos la función
temperatura = celsius_a_fahrenheit(25)

# Mostramos el resultado
print(f"25°C equivalen a {temperatura}°F")