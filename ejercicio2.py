import random

# Generar un número aleatorio entre 1 y 100
numero_aleatorio = random.randint(1, 100)

# Número de intentos permitidos
intentos_restantes = 10

print("¡Bienvenido al juego de adivinar el número!")
print("Tienes que elegir  un número entre 1 y 100. Tienes 10 intentos para adivinarlo.")

#  Intentos
while intentos_restantes > 0:
    #  Número al usuario
    intento = int(input("Introduce tu número: "))
    
    # Reducir el número de intentos restantes
    intentos_restantes -= 1
    
    # Comprobar si el número es correcto
    if intento == numero_aleatorio:
        print(f"¡Felicidades! Has adivinado el número en {10 - intentos_restantes} intentos.")
        break
    elif intento < numero_aleatorio:
        print(f"El número a adivinar es mayor que {intento}. Te quedan {intentos_restantes} intentos.")
    else:
        print(f"El número a adivinar es menor que {intento}. Te quedan {intentos_restantes} intentos.")
    
    # Los  intentos 
    if intentos_restantes == 0:
        print(f"Lo siento, se agotaron tu numeros de intentos . El número es..... {numero_aleatorio}.")

print("Gracias por jugar. ¡ Nos vemos  hasta la  próxima!")
