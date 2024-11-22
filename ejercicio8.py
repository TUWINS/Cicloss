# Solicitar los dos números al usuario
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

# Asegurarse de que num1 sea menor que num2
if num1 > num2:
    num1, num2 = num2, num1

# Imprimir los números pares entre num1 y num2
print(f"Números pares entre {num1} y {num2}:")
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(i)
