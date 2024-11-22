# Inicializar variables
pago_inicial = 10
total_pagado = 0

print("Mes\tPago Mensual\tTotal Acumulado")

# Calcular los pagos mensuales y el total acumulado
for mes in range(1, 21):
    pago_mensual = pago_inicial * (2 ** (mes - 1))
    total_pagado += pago_mensual
    print(f"{mes}\t{pago_mensual}\t\t{total_pagado}")

# Mostrar el total pagado después de 20 meses
print(f"\nTotal pagado después de 20 meses: {total_pagado} euros")
