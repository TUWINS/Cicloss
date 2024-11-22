def calcular_promedio():
    acumulador = 0  # Acumulador para la suma de los números
    contador = 0  # Contador para la cantidad de números introducidos

    # Bucle para pedir 10 números
    for i in range(10):
        numero = float(input(f"Introduce el número {i + 1}: "))  # Solicita un número al usuario
        acumulador += numero  # Acumula el número en la suma
        contador += 1  # Incrementa el contador

    # Calcula el promedio
    if contador > 0:
        promedio = acumulador / contador  # Evita la división por cero
    else:
        promedio = 0

    # Imprime el resultado
    print(f"La suma de los números introducidos es: {acumulador}")
    print(f"El promedio de los números introducidos es: {promedio}")

# Ejecutar la función
calcular_promedio()
