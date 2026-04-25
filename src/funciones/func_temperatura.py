# Ejercicio: Conversión completa

def convertir_temperatura(valor, origen, destino):
    # Validamos unidades
    if origen not in ['C', 'F'] or destino not in ['C', 'F']:
        return None

    if origen == destino:
        return valor

    if origen == 'C':
        return (valor * 9/5) + 32
    else:
        return (valor - 32) * 5/9

print(convertir_temperatura(25, 'C', 'F'))