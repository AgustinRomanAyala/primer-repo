num = int(input("Inegrese un numero para saber si es par o impar: "))

if num % 2 == 0:
    print(num, "Es un numero par")
elif num % 2 != 0:
    print(num, "Es un numero impar")
else:
    print("No se que es eso che")