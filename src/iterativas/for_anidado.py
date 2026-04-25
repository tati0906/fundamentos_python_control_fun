# Bucle externo (filas)
for i in range(1, 4):
    # Bucle interno (columnas)
    for j in range(1, 4):
        # Multiplica i por j y lo imprime en formato tabla
        print(f"{i} × {j} = {i*j}", end="\t")
    
    # Salto de línea después de cada fila
    print()