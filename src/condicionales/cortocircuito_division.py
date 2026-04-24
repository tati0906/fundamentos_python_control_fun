# Este programa evita una división por cero usando cortocircuito

dividendo = 10
divisor = 0

# Primero se evalúa si el divisor es diferente de 0
# Si es False → NO se ejecuta la división
if divisor != 0 and dividendo / divisor > 1:
    print("El resultado es mayor que 1.")
else:
    print("No es posible dividir entre cero.")