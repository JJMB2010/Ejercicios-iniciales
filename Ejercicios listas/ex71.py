# 71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas.

x=0
lista=[]

while x == 0:
    y=1
    while y != 0:
        b=input("Dime una letra: ")
        if b.isalpha():
            lista.append(str(b))
            y=0
    c=str(input("Quieres seguir (s/n): "))
    if c in ("Nn"):
        x=1
lista=list(set(lista))
print(lista)