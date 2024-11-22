def main():
    meses = 12
    ahorros_mensuales = []  # Lista para almacenar los ahorros de cada mes

    print("Programa para calcular ahorros anuales.")
    
    # Recolectar ahorros para cada mes
    for mes in range(1, meses + 1):
        while True:
            try:
                ahorro = float(input(f"Introduce el ahorro para el mes {mes}: "))
                if ahorro < 0:
                    print("Por favor, introduce una cantidad válida (no negativa).")
                else:
                    ahorros_mensuales.append(ahorro)
                    break
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número.")

    # Calcular el total ahorrado
    total_ahorrado = sum(ahorros_mensuales)

    # Mostrar los ahorros mensuales y el total
    print("\nAhorros mensuales:")
    for mes, ahorro in enumerate(ahorros_mensuales, start=1):
        print(f"Mes {mes}: ${ahorro:.2f}")

    print(f"\nTotal ahorrado al final del año: ${total_ahorrado:.2f}")

if __name__ == "__main__":
    main()