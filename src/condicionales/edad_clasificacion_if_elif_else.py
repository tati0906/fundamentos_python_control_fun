# Este programa clasifica a una persona según su edad

# Se define la variable edad
edad = 45

# Se evalúan rangos de edad usando comparaciones encadenadas

if edad < 18:
    # Si la edad es menor de 18
    print("Eres menor de edad.")

elif 18 <= edad < 65:
    # Si la edad está entre 18 y 64
    print("Eres adulto.")

else:
    # Si la edad es 65 o más
    print("Eres mayor de 65 años.")