# Inicializar el acumulador y el contador
suma = 0
contador = 0

# Pedir la cantidad de números al usuario
cantidad = int(input("Introduce la cantidad de números a introducir: "))

# Pedir los números y actualizar el acumulador y el contador
for _ in range(cantidad):
    numero = float(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
    contador += 1

# Calcular la media
if contador == 0:
    media = 0
else:
    media = suma / contador

# Imprimir la suma y la media
print(f"La suma de los números introducidos es: {suma}")
print(f"La media de los números introducidos es: {media}")
