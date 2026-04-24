# Este programa determina si es de mañana (buenos días)

# Se define la variable hora
hora = 10

# Se evalúa una condición compuesta usando el operador lógico AND
# La condición será verdadera solo si ambas partes se cumplen:
# 1. hora es mayor o igual a 6
# 2. hora es menor que 12
if hora >= 6 and hora < 12:
    # Si ambas condiciones son verdaderas, se ejecuta este bloque
    print("Buenos días.")

# Si alguna de las dos condiciones es falsa, no se imprime nada