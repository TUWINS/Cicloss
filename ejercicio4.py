# Función para imprimir la tabla de multiplicar de un número
def imprimir_tabla(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print()  # Línea en blanco para separar las tablas

# Imprimir las tablas de multiplicar del 1 al 5
for num in range(1, 6):
    imprimir_tabla(num)
