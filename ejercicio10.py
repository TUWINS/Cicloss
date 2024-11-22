# Solicitar la base y el exponente al usuario
base = float(input("Introduce la base (número real): "))
exponente = int(input("Introduce el exponente (entero positivo): "))

# Inicializar el resultado
resultado = 1

# Calcular la potencia usando un bucle
for _ in range(exponente):
    resultado *= base

# Mostrar el resultado
print(f"{base} elevado a {exponente} es {resultado}")
