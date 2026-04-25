# Este programa evita divisiones por cero usando continue

numeros = [1, 2, 0, 4, 0, 6, 7]

for num in numeros:
    # Si el número es 0, se evita la división
    if num == 0:
        print("Omitiendo división por cero")
        continue

    # Se realiza la división segura
    resultado = 10 / num
    print(f"10 / {num} = {resultado}")