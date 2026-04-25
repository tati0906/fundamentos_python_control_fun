# Este programa filtra temperaturas positivas usando continue

temperaturas = [22, -5, 28, 31, -15, 19, 26, -8]

print("Temperaturas positivas:")

for temp in temperaturas:
    # Se ignoran temperaturas menores o iguales a 0
    if temp <= 0:
        continue

    # Se imprimen solo las temperaturas positivas
    print(f"{temp}°C")