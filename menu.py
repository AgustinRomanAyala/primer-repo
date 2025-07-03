print("1) Saludar")
print("2) Muestra el doble de un numero")
print("3) Salir")
orden = int(input("Marca una opcion: "))

if orden == 1:
        print("Hola wachin")

elif orden == 2:
    pedido = int(input("Decime un numero y lo duplico: "))
    print(pedido * 2)

else:
    print("chau papino")

while orden != 3:

    print("1) Saludar")
    print("2) Muestra el doble de un numero")
    print("3) Salir")
    orden = int(input("Marca una opcion: "))

    if orden == 1:
        print("Hola wachin")

    elif orden == 2:
        pedido = int(input("Decime un numero y lo duplico: "))
        print(pedido * 2)

else:
    print("chau papino")