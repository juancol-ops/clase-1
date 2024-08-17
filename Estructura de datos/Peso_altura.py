x=input("Dame tu peso en kilos: ")
x=float(x)
y=input("Dame tu altura en metros: ")
y=float(y)

imc= x/(y*y)
if 30>imc>25 :
    print("Usted tiene sobrepeso")
else:
    print("Usted no tiene sobrepeso")
