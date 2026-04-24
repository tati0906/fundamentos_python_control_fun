# Este programa evalúa si una persona puede obtener licencia de conducir

# Variables
edad = 17
permiso_parental = True

# Se combinan AND y OR
# Condiciones:
# - Mayor de 18
# O
# - Mayor de 16 Y tiene permiso
if (edad >= 18) or (edad >= 16 and permiso_parental):
    print("Puedes obtener la licencia de conducir.")
else:
    print("No cumples los requisitos para la licencia.")