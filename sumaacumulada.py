numeros = []

for i in range(5):
    pedido = int(input(f"Ingresa un numero entero {i + 1}: "))
    numeros.append(pedido)

suma = sum(pedido)

print("La suma total es: ", suma)