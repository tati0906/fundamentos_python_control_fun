# Este programa muestra continue en bucles anidados

for i in range(1, 4):
    print(f"Grupo {i}:")

    for j in range(1, 6):
        # Se salta el número 3 en el bucle interno
        if j == 3:
            print("  Saltando el elemento 3")
            continue

        print(f"  Elemento {j}")

    print("Fin del grupo\n")