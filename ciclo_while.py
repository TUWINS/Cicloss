'''

Estructura while


while exp_bool:
    instrucciones
    actualiza valor para exp_bool



'''
## Tabla de multiplicar con while
num=int(input('ingresa un número: '))
i = 1
while i <= 10:
    print(f'{ num } * { i } = { num * i }')
    i = i + 1



'''
 Do While 
   
 while True:
      instrucciones
      if exp_bool
      break
 
'''   
# Programa que sale hasta decirle salir 
while True:
    option = input('Escribir Salir: ')
    if option == 'Salir':
        break