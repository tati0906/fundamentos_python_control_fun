# Este programa muestra cómo funciona el orden de los operadores lógicos

a = True
b = False
c = not b  # NOT se evalúa primero → c = True

# Aquí AND se evalúa antes que OR
resultado = a or b and c

print(resultado)  # Resultado: True

# Explicación:
# b and c → False and True → False
# a or False → True