# Este programa clasifica a una persona según su edad y estado civil

# Variables
edad = 30
estado_civil = 'soltero'

# Primer condicional: verifica si es mayor de edad
if edad >= 18:

    # Este condicional está dentro del primero (anidado)
    # Solo se ejecuta si edad >= 18
    if estado_civil == 'casado':
        print('Eres un adulto casado.')
    else:
        print('Eres un adulto soltero.')

else:
    # Este bloque se ejecuta si NO es mayor de edad
    print('Eres menor de edad.')