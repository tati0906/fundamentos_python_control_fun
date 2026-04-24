# Este programa simula un retiro de dinero de una cuenta bancaria

# Se define el saldo disponible y el monto a retirar
saldo = 300
retiro = 500

# Se verifica si hay suficiente saldo para realizar el retiro
if saldo >= retiro:
    # Si hay suficiente saldo, se realiza el retiro
    saldo -= retiro  # Se resta el monto retirado al saldo
    print("Retiro exitoso.")
    print(f"Nuevo saldo: {saldo}")  # Se muestra el saldo actualizado
else:
    # Si no hay suficiente saldo, se muestra un mensaje de error
    print("Fondos insuficientes.")
    print(f"Saldo actual: {saldo}")