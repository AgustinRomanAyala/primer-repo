# Importar una libreria de numeros random
import random

# Seleccionar los numeros de 1 a 100
random.randint(1, 100)

# Pedir cargar un numero entero
num = int(input("Adivina un numero de 1 a 100: "))

# Variable de intento para enumerarlos
intentos = 0

# Solicitar ingresar solo numeros hasta 100
if num > 100:
    num = int(input("DIJE HASTA 100! Tira de nuevo pa: "))

#Mientras el numero no sea 13 y no tengo mas de 7 intentos (1 inicial + 6), continuar
while num != 13 and intentos < 6:
    intentos += 1
    num = int(input("Tira de nuevo pa: "))

# Controlar nuevamente que el numero no sea mayor a 100
    if num > 100:
        print("Te dije hasta 100, gil de goma")

# El numero 13 es el correcto   
if num == 13:
    print("BIEN BOLUDITO!!")

# Si se agotan los intentos, terminar    
else:
    print("Volviste a perder, perdedor!")