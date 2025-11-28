# 58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random

ns=random.randint(1,5)
x=0

while x<3:
    n=int(input("Dime un número: "))

    if n == ns:
        print("Número correcto")
        x=4
    else:
        print("Número incorrecto")
        x=x+1