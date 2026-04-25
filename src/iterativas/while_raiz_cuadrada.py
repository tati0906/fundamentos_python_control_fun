# Función para calcular la raíz cuadrada usando aproximaciones
def calcular_raiz_cuadrada(numero, precision=0.0001):
    # Valor inicial de aproximación
    aproximacion = numero / 2
    
    # Mientras el error sea mayor a la precisión
    while abs(aproximacion**2 - numero) > precision:
        # Fórmula de aproximación (método de Newton)
        aproximacion = (aproximacion + numero/aproximacion) / 2
    
    return aproximacion

# Ejemplos de uso
print(f"Raíz cuadrada de 25: {calcular_raiz_cuadrada(25):.6f}")
print(f"Raíz cuadrada de 7: {calcular_raiz_cuadrada(7):.6f}")