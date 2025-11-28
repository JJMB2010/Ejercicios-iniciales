# 63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número de veces que se repite cada número.
import random

n1=0
n2=0
n3=0
n4=0
n5=0
n6=0

for x in range(0,100):
    n=random.randint(1,6)
    if n==1:
        n1=n1+1
    if n==2:
        n2=n2+1
    if n==3:
        n3=n3+1
    if n==4:
        n4=n4+1
    if n==5:
        n5=n5+1
    if n==6:
        n6=n6+1
print("Uno:",n1)
print("Dos:",n2)
print("Tres:",n3)
print("Cuatro:",n4)
print("Cinco:",n5)
print("Seis:",n6)