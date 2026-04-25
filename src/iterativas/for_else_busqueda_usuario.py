# Este programa busca un usuario y lo crea si no existe

def buscar_usuario(usuarios, nombre):
    for usuario in usuarios:
        # Se busca el usuario por nombre
        if usuario["nombre"] == nombre:
            print(f"Usuario encontrado: {usuario}")
            return usuario
    else:
        # Si no se encuentra, se crea uno nuevo
        print(f"Usuario '{nombre}' no encontrado, creando nuevo perfil...")
        nuevo_usuario = {"nombre": nombre, "nivel": 1}
        usuarios.append(nuevo_usuario)
        return nuevo_usuario