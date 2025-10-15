print("GASOLINERA: ")
print("1. Sin plomo 95")
print("2. Sin plomo 98")
print("3. Gasóleo A")
print("3. Gasóleo A+")

ti=int(input("Introduce el tipo de combustiblre (1,2,3,4): "))
lit=int(input("Introduce el numero de litros: "))

g1=round(lit*1.765,1)
g2=round(lit*1.913,2)
g3=round(lit*1.746,2)
g4=round(lit*1.839,2)

if ti == 1:
    print("El total a pagar es:",g1)
elif ti == 2:
    print("El total a pagar es:",g2,"y con descuento es:",round(g2-(10*g2/100),2))
elif ti == 3:
    print("El total a pagar es:",g3)
elif ti == 4:
    print("El total a pagar es:",g4,"y con descuento es:",round(g4-(12*g4/100),2))
else:
    print("El numero establecido no es 1, 2, 3 o 4")
