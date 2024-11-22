# Solicitar los límites del intervalo al usuario
while True:
    limite_inferior = int(input("Introduce el límite inferior del intervalo: "))
    limite_superior = int(input("Introduce el límite superior del intervalo: "))
    if limite_inferior < limite_superior:
        break
    else:
        print("El límite inferior debe ser menor que el límite superior. Inténtalo de nuevo.")

# Inicializar variables
suma_dentro_intervalo = 0
numeros_fuera_intervalo = 0
igual_a_limite = False

# Solicitar números al usuario hasta que se introduzca un 0
while True:
    numero = int(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break
    if limite_inferior < numero < limite_superior:
        suma_dentro_intervalo += numero
    else:
        numeros_fuera_intervalo += 1
    if numero == limite_inferior or numero == limite_superior:
        igual_a_limite = True

# Mostrar los resultados
print(f"La suma de los números dentro del intervalo es: {suma_dentro_intervalo}")
print(f"Números fuera del intervalo: {numeros_fuera_intervalo}")
if igual_a_limite:
    print("Se ha introducido algún número igual a los límites del intervalo.")
else:
    print("No se ha introducido ningún número igual a los límites del intervalo.")
