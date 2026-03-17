import random

ns=random.randint(1,20)

n=int(input("Dime un numero del 1 al 20: "))


while ns!=n:
    if n<0 and n>20:
        print("Ese no es el numero")
        if n<ns:
            print("Más alto")
        else:
            print("Más bajo")
        n=int(input("Dime un numero del 1 al 20: "))
    else:
        print("No está en el rango")
        n=int(input("Dime un numero del 1 al 20: "))

print("Numero correcto")
