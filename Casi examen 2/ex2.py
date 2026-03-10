lista=input().split("-")
seguro=[]
deb=[]
inv=[]
a=0
num=0
let=0
raro=0
max=lista[0]

for b in range(len(lista)):
    for x in lista[a]:
        if str(x).isnumeric():
            num+=1
        elif str(x).isalpha():
            let+=1
        else:
            raro+=1
    if raro>0:
        inv.append(lista[a])
    else:
        if num>0 and let>0 and len(lista[a])>=8:
            seguro.append(lista[a])
        elif num==0 and let>0 or num>0 and let==0 or len(lista[a])<8:
            deb.append(lista[a])
    if len(max)<len(lista[a]):
        max=lista[a]
    a+=1
    
print("Seguras",seguro)
print("Débil",deb)
print("Inválidas",inv)
print("La más larga",max)