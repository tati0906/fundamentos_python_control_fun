# Este ejemplo muestra cómo evitar ejecutar funciones costosas innecesariamente

usuario_autenticado = False

def operacion_costosa():
    print("Ejecutando operación costosa...")
    return True

# Si usuario_autenticado es False
# Python NO ejecuta la función operacion_costosa()
if usuario_autenticado and operacion_costosa():
    print("Operación realizada.")