import random  # Importamos el módulo para generar números aleatorios

# Genera un número aleatorio entre 1 y 10
objetivo = random.randint(1, 10)

# Contador de intentos
intentos = 0

# Variable booleana para saber si se adivinó
adivinado = False

# El bucle se ejecuta mientras no se haya adivinado y haya intentos disponibles
while not adivinado and intentos < 3:
    # Aumenta el número de intentos
    intentos += 1
    
    # Solicita un número al usuario
    numero = int(input(f"Intento {intentos}/3: Adivina un número del 1 al 10: "))

    # Verifica si el número es correcto
    if numero == objetivo:
        print(f"¡Correcto! Has adivinado en {intentos} intentos.")
        adivinado = True
    else:
        # Da una pista si el número es mayor o menor
        pista = "mayor" if numero < objetivo else "menor"
        print(f"Incorrecto. El número es {pista} que {numero}.")

# Si no se adivinó en los intentos disponibles
if not adivinado:
    print(f"Se acabaron los intentos. El número era {objetivo}.")