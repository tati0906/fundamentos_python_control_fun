# Este programa combina break y continue en un mismo bucle

numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
limite = 50
suma = 0

for num in numeros:
    # Se omiten múltiplos de 3
    if num % 3 == 0:
        print(f"Omitiendo {num} (múltiplo de 3)")
        continue

    # Se suma el número
    suma += num
    print(f"Añadiendo {num}: suma = {suma}")

    # Si se supera el límite, se termina el bucle
    if suma > limite:
        print(f"Límite de {limite} superado")
        break