# Este programa muestra el uso de else en un while

def encontrar_raiz(numero, max_iteraciones=10):
    aproximacion = numero / 2
    iteracion = 0

    # El bucle se ejecuta mientras no se alcance la precisión
    while abs(aproximacion**2 - numero) > 0.001 and iteracion < max_iteraciones:
        aproximacion = (aproximacion + numero/aproximacion) / 2
        iteracion += 1
        print(f"Iteración {iteracion}: {aproximacion:.6f}")
    else:
        # Se ejecuta si el bucle termina normalmente
        if iteracion < max_iteraciones:
            print(f"Convergencia alcanzada en {iteracion} iteraciones")
            return aproximacion

    print("No se alcanzó convergencia")
    return aproximacion