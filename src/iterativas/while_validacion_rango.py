# Función que valida que un número esté en un rango
def obtener_numero_en_rango(mensaje, minimo, maximo):
    while True:
        try:
            # Solicita un número al usuario
            valor = int(input(mensaje))
            
            # Verifica si está dentro del rango
            if minimo <= valor <= maximo:
                return valor
            
            print(f"Error: El número debe estar entre {minimo} y {maximo}.")
        
        except ValueError:
            # Maneja el error si no es un número entero
            print("Error: Debes introducir un número entero.")

# Solicita la edad validada
edad = obtener_numero_en_rango("Introduce tu edad (0-120): ", 0, 120)

# Imprime la edad
print(f"Edad registrada: {edad} años")