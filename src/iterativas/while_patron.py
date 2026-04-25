# Función que imprime un triángulo de asteriscos
def imprimir_triangulo(altura):
    # Variable que controla la fila actual
    fila = 1
    
    # Mientras la fila sea menor o igual a la altura
    while fila <= altura:
        # Imprime una cantidad de asteriscos igual a la fila
        print("*" * fila)
        
        # Incrementa la fila
        fila += 1

# Llamada a la función
imprimir_triangulo(5)