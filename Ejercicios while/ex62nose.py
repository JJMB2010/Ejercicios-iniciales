# 62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números hay ares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo. 

a=int(input("Dime un número: "))
b=int(input("Dime otro número: "))
x=1
if a<b:
    z=b-a
else:
    z=a-b

f=a
while x in range(1,z):

    if a>b:
        print(f, end="-")
        f=f-2

    if b>a:
        print(f, end="-")
        f=f+2
    x=x+1
print(b)