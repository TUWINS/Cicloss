# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Solicitar la cantidad de números primos al usuario
cantidad = int(input("Introduce la cantidad de números primos que quieres mostrar: "))

# Inicializar variables
contador = 0
numero = 2

print(f"Los primeros {cantidad} números primos son:")

# Encontrar y mostrar los primeros N números primos
while contador < cantidad:
    if es_primo(numero):
        print(numero, end=" ")
        contador += 1
    numero += 1
