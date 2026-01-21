# 83. Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así sucesivamente. Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas. Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar . PISTA.. ¿existe algún método que permita sumar el contenido de una lista?
import random
l=["casa","barco","gato","perro","madera","agua","puente","pantalón"]

y=1
puntuación=[]
c=8
intentos=1

while y==1:
    x=str(random.choice(l))
    print(x)
    while c!=0:
        a=str(input("Cual es la palabra secreta: "))
        if a == x:
            print("ACERTASTE")
            puntuación.append(c)
            c=1
        else:
            print("SIQUE INTENTANDOLO")
        c=c-1
    b=int(input("Queres continuar 1(si), 2(no): "))
    if b==2:
        y=2
    else:
        intentos=intentos+1
        c=8

print("La puntuación ha sido de:", puntuación)
print("Puntuación total de:", sum(puntuación))
print("La media de las partidas realizadas es de:",intentos*4)
if sum(puntuación)>intentos*4:
    print("Tienes buena suerte")
else:
    print("Dedicate al parchís")