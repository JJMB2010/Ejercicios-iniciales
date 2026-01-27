dni=input("Dime tu NIF, són 8 números: ")
lista_intentos=[]
lista_bien=[]
lista_mal=[]
lista_letras=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]

if len(str(dni))==8:
    if dni.isnumeric():
        a=int(dni)%23
        c=0
        for x in range(0,22):
            if x==a:
                b=lista_letras[x]
                c=1
        if c==0:
            lista_intentos.append("2")
            lista_mal.append(dni)
            print("ERROR")
        else:
            lista_intentos.append("3")
            dni=(str(dni) + "-" + str(b))
    else:
        lista_intentos.append("1")
        lista_mal.append(dni)
else:
    lista_intentos.append("0")
    lista_mal.append(dni)

print(lista_intentos)
print(dni)