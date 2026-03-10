lista=input().split("-")
maximo=0
lista_producto=[]
lista_precio=[]
lista_stock=[]
nada=[]
suma=0

for x in range(len(lista)):
    listalista=lista[x].split(":")
    lista_producto.append(listalista[0])
    lista_precio.append(listalista[1])
    lista_stock.append(listalista[2])
    suma+=int(listalista[1])*int(listalista[2])
maximo=max(lista_precio)
b=lista_precio.index(maximo)
caro=lista_producto[b]

ñ=0
z=0
for y in lista_stock:
    if int(y)==0:
        nada.append(lista_producto[int(z)-int(ñ)])
        lista_producto.pop(int(z)-int(ñ))
        lista_precio.pop(int(z)-int(ñ))
        lista_stock.pop(int(z)-int(ñ))
        ñ+=1
    z+=1

print(lista_producto)
print(lista_precio)
print(lista_stock)
print(nada)
print(suma)
print(caro)