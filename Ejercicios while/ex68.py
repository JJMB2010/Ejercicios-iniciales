# 68. Añade al ejercicio anterior la posibilidad de que el programa pregunte si deseas o no continuar introduciendo passwords. Ej. “¿Deseas introducir otro password s/n?

x=0
a=0

while x==0:
    n1=0
    n2=0
    l=0
    L=0
    s=0
    pos=0

    pas=str(input("Dime una contraseña: "))
    leng=len(pas)

    if (leng <= 8) and (6 <= leng): 
        for i in range(0,leng):
            p=pas[pos]

            if p.isalpha() and p.lower():
                l=l+1
            if p.isalpha() and p.upper():
                L=L+1
            if p in "*, _, @, &,/,#":
                s=s+1
            if p.isnumeric():
                p=int(p)
                if (1 <= p and p <= 5 ):
                    n1=n1+1
            p=str(p)
            if p.isnumeric():
                p=int(p)
                if(5 <= p and p <= 6 ):
                    n2=n2+1
            pos=pos+1

        if (n1>=2)and(n2>=1)and(l>=2)and(s>=2)and(L>=1):
            print("La contraseña es correcta")
            a=1
        else:
            print("La contraseña es incorrecta")

    else:
        print("Longitud incorrecta")
        
    res=str(input("Quieres volver a poner otra contraseña (n/s): "))

    if res in "Nn":
        x=1