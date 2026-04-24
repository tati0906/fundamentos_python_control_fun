# Este programa determina si un número es par o impar

# Se define la variable numero
numero = 15

# Se utiliza el operador módulo (%) para obtener el residuo de la división entre 2
# Si el residuo es 0, el número es par
if numero % 2 == 0:
    print("El número es par.")
else:
    # Si el residuo no es 0, el número es impar
    print("El número es impar.")