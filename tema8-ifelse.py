# Angel Eduardo Juarez Alvizo IDGS801
print("Suma de numeros")
num1=int(input("Dame n1: "))
num2=int(input("Dame n2: "))
if num1 > num2:
    print("el {} es mayor que el {}".format(num1,num2))
else:
    print("el {} es mayor que el {}".format(num2,num1))

print("---------------    pedir edad ------------------")
edad=int(input("ingresa tu edad"))
if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Eres igual de edad")
else:
    print("No eres mayor de edad")