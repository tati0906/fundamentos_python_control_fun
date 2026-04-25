# Ejercicio: Uso de **kwargs

def mostrar_datos(**datos):
    # Recorre el diccionario e imprime clave y valor
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_datos(nombre="Python", version=3.12)