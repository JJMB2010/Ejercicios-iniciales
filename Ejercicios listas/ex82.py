# 82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine la palabra
import random
l=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
x=str(random.choice(l))
y=1
while y==1:
    a=str(input("Cual es la palabra secreta: "))
    if a in x:
        print("ACERTASTE")
        y=2
    else:
        print("SIQUE INTENTANDOLO")