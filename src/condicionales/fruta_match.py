# Este programa identifica una fruta ingresada por el usuario

# Se solicita al usuario que ingrese una fruta
fruta = input("Introduzca una fruta: ")

# La estructura match evalúa el valor de la variable fruta
match fruta:
    # Cada case compara el valor con un patrón específico

    case "manzana":
        # Si el valor es "manzana"
        print("La fruta es una manzana.")

    case "naranja":
        # Si el valor es "naranja"
        print("La fruta es una naranja.")

    case "plátano":
        # Si el valor es "plátano"
        print("La fruta es un plátano.")

    case _:
        # El guion bajo (_) es un comodín
        # Se ejecuta si ningún caso anterior coincide
        print("Fruta desconocida.")