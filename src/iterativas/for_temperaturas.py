# Lista de temperaturas registradas
temperaturas = [22, 19, 24, 25, 21, 23, 20]

# Lista de días de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Encontrar la temperatura máxima
max_temp = max(temperaturas)

# Obtener el índice de la temperatura máxima
indice_max = temperaturas.index(max_temp)

# Mostrar el día más caluroso
print(f"El día más caluroso fue {dias[indice_max]} con {max_temp}°C")

# Calcular el promedio de temperaturas
promedio = sum(temperaturas) / len(temperaturas)

# Mostrar el promedio
print(f"Temperatura promedio: {promedio:.1f}°C")

# Recorrer los días para encontrar los que están por encima del promedio
for i in range(len(dias)):
    # Comparar cada temperatura con el promedio
    if temperaturas[i] > promedio:
        print(f"{dias[i]}: {temperaturas[i]}°C (por encima del promedio)")