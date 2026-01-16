# 74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de entre las 2 listas.

lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
a=[]
b=[]

for x in lista1:
    if x in lista2:
        a.append(str(x))
    else:
        b.append(str(x))
for x in lista2:
    if x in lista1:
        a.append(str(x))
    else:
        b.append(str(x))

print(list(set(a)))
print(b)