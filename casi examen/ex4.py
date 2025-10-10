
op=int(input("Opción: "))
k=int(input("kWh: "))

if op < 1 or 4 < op:
    print("ERROR")
else:
    if op == 1:
        fin=k*0.158
        print("El total a pagar es",fin)
        print("Con el descuento es",(fin-((fin*5)/100)))
    if op == 2:
        fin=k*0.192
        print("El total a pagar es",fin)
        print("Con el descuento es",fin)
    if op == 3:
        fin=k*0.143
        print("El total a pagar es",fin)
        print("Con el descuento es",(fin-((fin*8)/100)))
    if op == 4:
        fin=k*0.170
        print("El total a pagar es",fin)
        print("Con el descuento es",(fin-((fin*10)/100)))
