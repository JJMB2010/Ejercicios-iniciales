milista=[1,2,3,4,5,6]
milistapordos=[]
milistacopiada=[]

#maximo=max(milista)
#minimo=min(milista)
#suma=sum(milista)

#print(milista)
#print("maximo:",maximo)
#print("minimo:",minimo)
#print("suma:",suma)

#for x in range (0,len(milista)):
#    a=milista[x]*2
#    milistapordos.append(a)

#print(milistapordos)

#for x in milista:
#    milistapordos.append(x*2)

#print(milistapordos)

#milistacondobles=[1,2,3,1,2,5,6,4,3,2,1,4,2,3,4]
#milistasindobles=[]

#milistasindobles=list(set(milistacondobles))

#print(milistasindobles)

listanumero=[]
listanonumeros=[]

frase=input("Introduce valores separados por un guión: ")

listatoda=list(frase.split("-"))

for x in listatoda:
    if x.isnumeric():
        listanumero.append(int(x))

#for x in range(len(listatoda)):
#    if listatoda[x].isnumeric():
#        listanumero.append(int(listatoda[x]))
#    else:
#        listanonumeros.append(listatoda[x])

#print(listanumero)
#print(sum(listanumero))

#print(listanonumeros)