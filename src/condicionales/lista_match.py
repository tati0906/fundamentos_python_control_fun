# Este programa analiza una lista usando patrones en match

# Se define una lista de números
numeros = [1, 2, 3, 4]

# Se evalúa la estructura de la lista
match numeros:

    case []:
        # Lista vacía
        print("La lista está vacía.")

    case [uno]:
        # Lista con un solo elemento
        print(f"Un solo elemento: {uno}.")

    case [uno, dos]:
        # Lista con dos elementos
        print(f"Dos elementos: {uno} y {dos}.")

    case [uno, *resto]:
        # Lista con más de dos elementos
        # uno = primer elemento
        # resto = lista con los demás elementos
        print(f"Primer elemento: {uno}, resto de la lista: {resto}.")