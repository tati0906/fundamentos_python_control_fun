# Este programa valida una contraseña ingresada por el usuario

# Se solicita al usuario que ingrese una contraseña
contrasena = input("Introduce la contraseña: ")

# Se compara la contraseña ingresada con la correcta
if contrasena == "secreta123":
    # Si coincide, se concede el acceso
    print("Acceso concedido.")
else:
    # Si no coincide, se deniega el acceso
    print("Contraseña incorrecta. Acceso denegado.")