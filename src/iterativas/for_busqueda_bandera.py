# Este programa usa una bandera para salir de bucles anidados

encontrado = False

for i in range(5):
    for j in range(5):
        # Se busca una condición específica
        if i * j > 10:
            print(f"Valor encontrado: {i} * {j} = {i*j}")
            encontrado = True
            break  # Sale del bucle interno

    # Si ya se encontró, se sale del bucle externo
    if encontrado:
        break