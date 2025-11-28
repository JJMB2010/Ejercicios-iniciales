
l=int(input("Longitud: "))
a=str(input("Cifra: "))
pr=1
par=0
y=0
if len(str(a)) == l:
    for x in range(0,l):
        p=a[y]
        p=int(p)
        if p%2 == 0:
            par=par+1
        pr=pr*p
        y=y+1
    print("Producto:",pr)
    print("Pares:",par)

else:
    print("Longitud incorrecta")