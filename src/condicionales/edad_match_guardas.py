# Este programa clasifica la edad usando match con guardas (condiciones adicionales)

# Se define la variable edad
edad = 20

# Se evalúa la variable edad con condiciones extra (guardas)
match edad:

    case edad if edad < 18:
        # Si la edad es menor a 18
        print("Eres menor de edad.")

    case edad if edad >= 18 and edad < 65:
        # Si está entre 18 y 64
        print("Eres adulto.")

    case edad if edad >= 65:
        # Si es 65 o más
        print("Eres adulto mayor.")