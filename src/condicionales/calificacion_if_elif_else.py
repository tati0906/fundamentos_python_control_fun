# Este programa asigna una calificación según una nota numérica

# Se define la variable nota
nota = 87

# Se evalúan las condiciones en orden de arriba hacia abajo

if nota >= 90:
    # Si la nota es 90 o más
    print("Calificación: Sobresaliente")

elif nota >= 80:
    # Si no fue >= 90 pero sí >= 80
    print("Calificación: Notable")

elif nota >= 70:
    # Si no cumplió las anteriores pero sí >= 70
    print("Calificación: Aprobado")

else:
    # Si no cumple ninguna condición anterior
    print("Calificación: Suspenso")

# IMPORTANTE:
# Solo se ejecuta el primer bloque verdadero y los demás se ignoran