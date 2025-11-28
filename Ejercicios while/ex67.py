# 67. Realiza de nuevo el programa de Password (fase 2). El password debe tener las siguientes consideraciones:  Debe tener una longitud entre 6 y 8 caracteres. Debe contener como mínimo: 2 números mayores o iguales que 1 y menor o igual que 5 2 letras minúsculas 1 letra mayúscula 2 símbolos (*, _, @, &,/,#) 1 número mayor o igual que 6 y menor o igual que 5

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
    x=1