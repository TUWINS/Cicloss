# Solicitar la cantidad de números al usuario
cantidad = int(input("Introduce la cantidad de números a introducir: "))

# Inicializar contadores
mayores_que_cero = 0
menores_que_cero = 0
iguales_a_cero = 0

# Solicitar los números y actualizar los contadores
for _ in range(cantidad):
    numero = float(input("Introduce un número: "))
    if numero > 0:
        mayores_que_cero += 1
    elif numero < 0:
        menores_que_cero += 1
    else:
        iguales_a_cero += 1

# Mostrar los resultados
print(f"Números mayores que 0: {mayores_que_cero}")
print(f"Números menores que 0: {menores_que_cero}")
print(f"Números iguales a 0: {iguales_a_cero}")
