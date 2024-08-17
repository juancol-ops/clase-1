
x=input("Dame un numero: ")
y=input("Dame otro numero: ")

x=int(x)
y=int(y)
resultado = input("Que desea realizar, si desea realizar una suma ingresa el numero 1, si desea realizar una resta el 2, una division el 3 o multiplicacion el 4 : ")
resultado = int(resultado)


if resultado == 1:
    print(f"El resultado de la suma es: {x + y} ")
elif resultado == 2:
    print(f"El resultado de la resta es: {x-y} ")
elif resultado == 3:
    print(f"El resultado de la division es: {x/y} ")
elif resultado == 4:
    print(f"El resultado de la multiplicacion es: {x*y} ")
else:
    print("El numero no es correcto")






