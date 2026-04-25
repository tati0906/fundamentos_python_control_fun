# Diccionario con información de usuario
usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"}

# Itera sobre las claves del diccionario
for clave in usuario:
    # Accede al valor usando la clave
    print(f"Clave: {clave}, Valor: {usuario[clave]}")

# Itera sobre pares clave-valor usando items()
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

# Itera solo sobre los valores del diccionario
for valor in usuario.values():
    print(valor)