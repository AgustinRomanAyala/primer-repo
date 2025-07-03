num1 = int(input("Primer numero a sumar: "))

num2 = int(input("Segundo numero a sumar: "))

if num1 > num2:
    print(num1, "es mayor que", num2)
elif num2 > num1:
    print(num1, "es menor que", num2)
else:
    print("los numeros son iguales")