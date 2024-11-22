# Solicitar un número al usuario
num = int(input("Introduce un número: "))

# Inicializar el resultado del factorial
factorial = 1

# Calcular el factorial
if num < 0:
    print("El factorial no está definido para números negativos.")
elif num == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"El factorial de {num} es {factorial}.")
