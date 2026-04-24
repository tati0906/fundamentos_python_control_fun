# Este programa evalúa si una persona puede obtener licencia de conducir

edad = 16
permiso_padres = True

# Primera condición
if edad >= 18:
    print('Puedes obtener la licencia de conducir.')

else:
    # Segundo nivel de decisión
    if edad >= 16:

        # Tercer nivel (anidado dentro del segundo)
        if permiso_padres:
            print('Puedes obtener la licencia con permiso de tus padres.')
        else:
            print('Necesitas el permiso de tus padres para obtener la licencia.')

    else:
        print('Eres demasiado joven para conducir.')