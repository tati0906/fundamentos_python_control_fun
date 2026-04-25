# Saldo inicial
saldo = 1000

# El bucle se ejecuta mientras haya saldo disponible
while saldo > 0:
    # Muestra el saldo actual
    print(f"Saldo actual: {saldo}€")
    
    # Solicita una cantidad a gastar
    gasto = float(input("Introduce la cantidad a gastar (0 para salir): "))

    # Si el usuario ingresa 0, se rompe el bucle
    if gasto == 0:
        break  # Termina el bucle inmediatamente

    # Si el gasto es mayor al saldo, no se permite
    if gasto > saldo:
        print("No tienes suficiente saldo.")
        continue  # Vuelve al inicio del bucle

    # Resta el gasto al saldo
    saldo -= gasto

# Muestra el saldo final
print(f"Saldo final: {saldo}€")