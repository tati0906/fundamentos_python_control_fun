# Ejercicio: Crear usuario con varios parámetros

def crear_usuario(nombre, apellido, edad, email, activo=True):
    # Retorna un diccionario con los datos del usuario
    return {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "email": email,
        "activo": activo
    }

usuario = crear_usuario("Juan", "Perez", 25, "juan@mail.com")
print(usuario)