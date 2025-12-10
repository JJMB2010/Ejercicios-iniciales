#Password_v2

for x in range(0,3):
    n=0
    l=0
    s=0
    pos=0
    #Aquí añadiremos nuevas variables:
    a=0
    max=0
    min=0
    mid=0
    r=""
    r1=""
    r2=""
    r3=""
    r4=""
    r5=""
    r6=""

    pas=str(input("Dime una contraseña: "))
    leng=len(pas)

    #Aquí hay unas contraseñas para poder testear mi código:
    #  1. pPPpPBHJojphu, Bhjuvuiv, YBvyvjkbybju
    #  2. 234b8HBy6, 32h89fhfb2, d7g21873gfr1
    #  3. 27BNdbqi(%), 3hR(sw57HOs), 3snio/kH79Bui3
    #  4. (/)/(Y(/&$R%E@))), """""@@@@@@@", /%&$@@#€#¬
    #  5. 358358358, 84325765887, 5782346589
    #  6.  ,     ,,
    #  7. 27BNdbqi(%), """""@@@@@@@", 358358358
    #  8. HHHhhh&&&@259, IHhuHh·%&@2598,"@2HHl5ai/()9
    #  9. IHhuHh·%&@2598, 234b8HBy6, YBvyvjkbybju
    #  10. "@2HHl5ai/()9,,     a

    for i in range(0,leng):
        p=pas[pos]

        if p.isalpha():
            l=l+1
        elif p.isnumeric():
            n=n+1
            if float(p) <= 3:
                min=min+1
            if float(p) == 5:
                mid=mid+1
            if 8 <= float(p):
                max=max+1
        else:
            s=s+1
            if str(p) in "@":
                a=a+1
        pos=pos+1
    
    if (n>=3)and(l>=3)and(s>=2)and(a>=1)and(min>=2)and(mid>=3)and(max>=1):
        print("La contraseña es correcta")
    else:
        if n < 3:
            r=" El mumero de numeros es incorrecto, porque " + str(n)  + " no es igual o mayor que 3"
        if l < 3:
            r1=" El mumero de letras es incorrecto, porque " + str(l) + " no es igual o mayor que 3"
        if s < 2:
            r2=" El mumero de simbolos es incorrecto, porque " + str(s) + " no es igual o mayor que 2"
        if a < 1:
            r3=" Te falta el símbolo secreto"
        if min < 2:
            r4=" La cantidad de numeros menores es insuficiente"
        if mid < 3:
            r5=" La cantidad de numeros medianos es insuficiente"
        if max < 1:
            r6=" La cantidad de numeros mayores es insuficiente"
        
            
    print((r+r1+r2+r4+r5+r6+r3))

# RESUMEN
# Prueva 1:
# 