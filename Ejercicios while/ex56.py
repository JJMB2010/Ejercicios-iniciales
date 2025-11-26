# 56.  Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la realización de un pedido, si quiere gestionar otro. 

print("MENÚ") 
print("1. Bocadillo de calamares- 9 €")
print("2. Bocadillo de chistorra - 4.5 €")
print("3. Bikini de jamón - 2.5 €") 
print("ACOMPAÑAMIENTO") 
print("1. Patatas finas - 1.5 €") 
print("2. Patatas gruesas - 1.75 €") 
print("3. Patatas rústicas - 2 €") 
print("BEBIDAS") 
print("1. Coca cola - 2 €")
print("2. Acuarius - 1.5 €") 
print("3. Agua - 1 €")

x=0
s=0
p=0
while x==0:
    a=0
    r11=str(input("Quieres menú (s/n): "))
    if r11 in "Ss":
        r1=int(input("Que quieres de menú (1/2/3): "))
        if r1==1:
            s=s+9
        if r1==2:
            s=s+4.5
        if r1==3:
            s=s+2.5
    r11=str(input("Quieres acompañamiento (s/n): "))
    if r11 in "Ss":
        r2=int(input("Que quieres de acompañamiento (1/2/3): "))
        if r2==1:
            s=s+1.5
        if r2==2:
            s=s+1.75
        if r2==3:
            s=s+2
    r11=str(input("Quieres bebida (s/n): "))
    if r11 in "Ss":
        r3=int(input("Que quieres de bebidas (1/2/3): "))
        if r3==1:
            s=s+2
        if r3==2:
            s=s+1.5
        if r3==3:
            s=s+1
    p=p+1

    while a==0:
        res=str(input("Quieres otro pedido (s/n):"))
        if res in "snSN":
            if res in "nN":
                print("Número de pedidos:",p)
                print("Total a pagar:",s)
                print("Total con iva:",s+(10*s/100))
                if s > 30:
                    print("Precio total con descuento del 15%:",(s+(10*s/100))-((s+(10*s/100))*15/100))
                elif (s <= 30) and (20 <= s):
                    print("Precio total con descuento del 5%:",(s+(10*s/100))-((s+(10*s/100))*5/100))
                x=1
            a=1   