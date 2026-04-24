# Este programa clasifica un número como positivo, negativo o cero

# Se define la variable numero
numero = 0

# Se evalúa si el número es mayor que 0
if numero > 0:
    # Si se cumple, el número es positivo
    print("El número es positivo.")

# Si no se cumple la primera condición, se evalúa esta
elif numero < 0:
    # Si se cumple, el número es negativo
    print("El número es negativo.")

# Si ninguna de las condiciones anteriores se cumple
else:
    # Significa que el número es exactamente 0
    print("El número es cero.")