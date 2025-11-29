# 62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo. 

a=int(input("Dime un número: "))
b=int(input("Dime otro número: "))
x=0
si=""

f=a
for x in range(a,b):

    if a>b:
        if f%2==0:
            si=si+(str(f)+"-")
        f=f-1

    if b>a:
        if f%2==0:
            si=si+(str(f)+"-")
        f=f+1

if f%2==0:
    print(si+str(f))
else:
    print(si[:-1])