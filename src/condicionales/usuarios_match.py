# Este programa analiza el rol de diferentes usuarios usando diccionarios

# Lista de usuarios representados como diccionarios
usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "usuario"},
    {"nombre": "Marta", "rol": "moderador"}
]

# Se recorre la lista con un ciclo for
for usuario in usuarios:

    # Se evalúa cada diccionario
    match usuario:

        case {"rol": "admin"}:
            # Si el rol es admin
            print(f"{usuario['nombre']} tiene permisos de administrador.")

        case {"rol": "moderador"}:
            # Si el rol es moderador
            print(f"{usuario['nombre']} puede moderar contenidos.")

        case {"rol": "usuario"}:
            # Si el rol es usuario
            print(f"{usuario['nombre']} es un usuario regular.")

        case _:
            # Caso por defecto
            print(f"Rol de {usuario['nombre']} desconocido.")