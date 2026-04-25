# Este programa valida que todas las edades sean correctas

def validar_edades(lista_edades):
    for edad in lista_edades:
        # Se verifica si la edad es inválida
        if not isinstance(edad, int) or edad < 0:
            print(f"Edad inválida encontrada: {edad}")
            break
    else:
        # Se ejecuta si todas las edades son válidas
        print("Todas las edades son válidas")
        return True

    return False