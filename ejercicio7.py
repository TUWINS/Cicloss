# Función para verificar si un carácter es una vocal
def es_vocal(caracter):
    return caracter.lower() in 'aeiou'

# Bucle para solicitar caracteres al usuario
while True:
    caracter = input("Introduce un carácter (espacio para terminar): ")
    
    # Verificar si el carácter es un espacio para terminar el programa
    if caracter == ' ':
        break
    
    # Comprobar si el carácter es una vocal o no
    if es_vocal(caracter):
        print("VOCAL")
    else:
        print("NO VOCAL")
