listalista=input()
lista=listalista.split(",")
print(listalista)

min=float(lista[0])
max=float(lista[0])

for x in (lista):
    if float(x)>max:
        max=x
    elif float(x)<min:
        min=x

lista.remove(max)
lista.remove(min)
print(lista)
sum=0
p=0

for y in (lista):
    sum=sum+int(y)
    p=p+1
media=round((sum/p), 2)
print(media)