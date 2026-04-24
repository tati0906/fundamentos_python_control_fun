# Este programa analiza la posición de un punto en el plano cartesiano

# Se define una tupla con coordenadas (x, y)
punto = (0, 0)

# Se evalúa la estructura del dato usando match
match punto:

    case (0, 0):
        # Coincide exactamente con el origen
        print("El punto está en el origen.")

    case (0, y):
        # x es 0, pero y puede ser cualquier valor
        # Se captura el valor de y automáticamente
        print(f"El punto está en el eje Y en y={y}.")

    case (x, 0):
        # y es 0, pero x puede ser cualquier valor
        print(f"El punto está en el eje X en x={x}.")

    case (x, y):
        # Cualquier otro punto
        print(f"El punto está en coordenadas x={x}, y={y}.")