#Password_v2

for x in range(0,3):
    n=0
    l=0
    s=0
    pos=0
    r=""
    r1=""
    r2=""
    pas=str(input("Dime una contraseña: "))
    leng=len(pas)

    for i in range(0,leng):
        p=pas[pos]
        if p.isalpha():
            l=l+1
        elif p.isnumeric():
            n=n+1
        else:
            s=s+1
        pos=pos+1
    
    if (n>=3)and(l>=3)and(s>=2):
        print("La contraseña es correcta")
    else:
        if n < 3:
            r="El mumero de numeros es incorrecto, porque " & str(n)  & " no es igual o mayor que 3 "
        if l < 3:
            r1="El mumero de letras es incorrecto, porque " + str(l) + " no es igual o mayor que 3 "
        if s < 2:
            r2="El mumero de simbolos es incorrecto, porque " + str(s) + " no es igual o mayor que 2 "
            
    print(r+r1+r2)