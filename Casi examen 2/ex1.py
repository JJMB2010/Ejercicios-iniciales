lista=input().split(",")

lista=[int(x) for x in lista]
print(lista)

minim=min(lista)
maxim=max(lista)

lista.remove(maxim)
lista.remove(minim)
print(lista)
suma=0
p=0

media=sum(lista)/len(lista)
print(media)

if media<5:
    print("Rendimiento bajo")
elif media>=5 and media<10:
    print("Rendimiento medio")
else:
    print("Rendimiento alto")