# Este programa muestra cómo funciona el cortocircuito con OR

acceso_permitido = False
acceso_registrado = True

# OR: si la primera condición es True, no evalúa la segunda
if acceso_permitido or acceso_registrado:
    print("Acceso concedido.")

# En este caso:
# acceso_permitido = False
# acceso_registrado = True → se evalúa porque la primera fue False