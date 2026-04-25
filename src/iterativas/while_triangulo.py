# Este programa imprime un triángulo de asteriscos usando un bucle while

# Se define una función que recibe la altura del triángulo
def imprimir_triangulo(altura):
    # Se inicia la fila en 1
    fila = 1

    # El bucle se ejecuta mientras la fila sea menor o igual a la altura
    while fila <= altura:
        # Se imprime una cantidad de asteriscos igual al número de la fila
        print("*" * fila)

        # Se incrementa la fila en cada iteración
        fila += 1

# Se llama a la función con altura 5
imprimir_triangulo(5)