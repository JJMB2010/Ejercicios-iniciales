# 73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se repiten y cuales no.

lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
a=[]
b=[]

for x in lista1:
    if x in lista2:
        a.append(str(x))
    else:
        b.append(str(x))

print(a)
print(b)