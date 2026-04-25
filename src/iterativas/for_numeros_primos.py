# Función que determina si un número es primo
def es_primo(num):
    # Los números menores que 2 no son primos
    if num < 2:
        return False

    # Probamos divisores desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(num**0.5) + 1):
        # Si el número es divisible, no es primo
        if num % i == 0:
            return False

    # Si no tuvo divisores, es primo
    return True

# Lista donde guardaremos los números primos
primos = []

# Recorremos números del 2 al 19
for num in range(2, 20):
    # Verificamos si es primo
    if es_primo(num):
        # Si lo es, lo agregamos a la lista
        primos.append(num)

# Mostramos la lista de números primos
print(f"Números primos entre 2 y 19: {primos}")