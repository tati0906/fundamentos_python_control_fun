# Función que calcula el factorial de un número
def calcular_factorial(n):
    # Variable acumuladora
    resultado = 1
    
    # Mientras n sea mayor que 0
    while n > 0:
        # Multiplica el resultado por n
        resultado *= n
        
        # Decrementa n
        n -= 1
    
    # Retorna el resultado final
    return resultado

# Número a calcular
numero = 5

# Imprime el factorial
print(f"El factorial de {numero} es {calcular_factorial(numero)}")