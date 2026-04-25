# Ejercicio: Parámetros con valor por defecto

def saludar(nombre, mensaje="¡Bienvenido!"):
    # Imprime saludo con mensaje opcional
    print(f"Hola {nombre}. {mensaje}")

saludar("Carlos")
saludar("Ana", "¿Cómo estás?")