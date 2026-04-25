# Este programa suma solo valores numéricos válidos

datos = ["25", "error", "42", "texto", "17"]

suma = 0

for valor in datos:
    # Si el valor no es numérico, se ignora
    if not valor.isdigit():
        print(f"Valor no numérico ignorado: '{valor}'")
        continue

    # Se suma el valor convertido a entero
    suma += int(valor)

print(f"La suma de los valores válidos es: {suma}")