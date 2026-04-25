# Este programa combina pass y else

def analizar_datos(valores, umbral):
    tiene_advertencias = False

    for valor in valores:
        # Si el valor supera el umbral
        if valor > umbral:
            tiene_advertencias = True
            print(f"Advertencia: valor {valor} excede el umbral {umbral}")
        else:
            pass  # No hacemos nada con valores normales
    else:
        # Se ejecuta al finalizar el bucle normalmente
        if not tiene_advertencias:
            print("Todos los valores están dentro del rango normal")
            return "OK"

    return "ADVERTENCIA"