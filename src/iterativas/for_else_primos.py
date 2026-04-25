# Este programa usa else en un for para validar búsqueda

numeros = [4, 6, 8, 9, 10, 12]

for num in numeros:
    # Se intenta encontrar un número primo simple
    if num % 2 != 0 and num % 3 != 0:
        print(f"¡Encontrado un primo: {num}!")
        break
else:
    # Se ejecuta si no se encontró ningún número primo
    print("No se encontró ningún número primo en la lista")