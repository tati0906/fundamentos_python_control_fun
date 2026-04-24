# Este programa clasifica una persona según su edad usando ternarios anidados

edad = 20

# Se usan múltiples ternarios
# - Si edad < 18 → "Menor"
# - Si no, se evalúa otro ternario:
#     - edad < 30 → "Joven Adulto"
#     - si no → "Adulto"
categoria = "Menor" if edad < 18 else ("Joven Adulto" if edad < 30 else "Adulto")

print(categoria)

# NOTA:
# Aunque funciona, usar muchos ternarios anidados puede dificultar la lectura