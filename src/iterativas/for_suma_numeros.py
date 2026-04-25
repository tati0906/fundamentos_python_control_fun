# Número hasta el cual queremos sumar
n = 10

# Variable acumuladora inicializada en 0
suma = 0

# Recorremos los números del 1 hasta n (incluyendo n)
for i in range(1, n + 1):
    # En cada iteración sumamos el valor de i a la variable suma
    suma += i

# Mostramos el resultado final
print(f"La suma de los primeros {n} números es: {suma}")