# Ejercicio: Función más completa

def formatear_texto(texto, mayusculas=False, prefijo="", sufijo="", separador=" "):
    # Convertimos a mayúsculas si se solicita
    if mayusculas:
        texto = texto.upper()

    # Separamos el texto en palabras
    palabras = texto.split()

    # Aplicamos prefijo y sufijo
    palabras_formateadas = []
    for palabra in palabras:
        palabras_formateadas.append(f"{prefijo}{palabra}{sufijo}")

    # Unimos con separador
    return separador.join(palabras_formateadas)

print(formatear_texto("python es genial", mayusculas=True, prefijo="#"))