def convertir_a_binario(numero):
    """Convierte un número entero a su representación binaria usando ciclos."""
    if numero == 0:
        return "0"  # El binario de 0 es 0

    binario = ""
    negativo = False

    # Si el número es negativo, lo convertimos a positivo y marcamos la bandera
    if numero < 0:
        negativo = True
        numero = -numero

    while numero > 0:
        # Agregar el residuo (0 o 1) al inicio de la cadena binaria
        binario = str(numero % 2) + binario
        # Dividir el número por 2
        numero //= 2

    return "-" + binario if negativo else binario

def main():
    while True:
        try:
            # Pedir  un número entero al usuario
            numero = int(input("Introduce un número entero: "))
            break  # Salir del bucle si la entrada es válida
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

    # Convertir el número a binario y mostrar el resultado
    binario = convertir_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")

if __name__ == "__main__":
    main()

