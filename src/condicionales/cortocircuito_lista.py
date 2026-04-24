# Este programa evita un error al acceder a una lista vacía

# Lista vacía
lista = []

# Se usa evaluación de cortocircuito con AND
# Primero se evalúa 'lista'
# Si la lista está vacía → es False
# Entonces NO se evalúa 'lista[0]'
if lista and lista[0] == 'Python':
    print("El primer elemento es 'Python'.")

# Esto evita un error de tipo IndexError