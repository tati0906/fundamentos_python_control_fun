# Este programa valida usuario y contraseña con condicionales anidados

usuario = 'admin'
contrasena = '1234'

# Primero se verifica el usuario
if usuario == 'admin':

    # Solo si el usuario es correcto, se valida la contraseña
    if contrasena == '1234':
        print('Acceso concedido.')
    else:
        print('Contraseña incorrecta.')

else:
    print('Usuario no reconocido.')