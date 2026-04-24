# Este programa muestra el uso de any() y all() con cortocircuito

# any(): se detiene cuando encuentra un True
numeros = [0, 0, 1, 0]

if any(numeros):
    print("Al menos un número es diferente de cero.")

# all(): se detiene cuando encuentra un False
condiciones = [True, True, False, True]

if all(condiciones):
    print("Todas son verdaderas.")
else:
    print("Al menos una es falsa.")