# Ejercicio: Verificar si un número es par

# Definimos la función que recibe un número
def es_par(numero):
    # Retorna True si el número es divisible por 2, de lo contrario False
    return numero % 2 == 0

# Probamos la función
print(es_par(4))  # True
print(es_par(7))  # False