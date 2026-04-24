# Este programa evita una división por cero usando un ternario

dividendo = 10
divisor = 0

# Se evalúa primero si el divisor es diferente de 0
# Si lo es → realiza la división
# Si no → devuelve un mensaje
resultado = dividendo / divisor if divisor != 0 else "División por cero no permitida"

print(resultado)