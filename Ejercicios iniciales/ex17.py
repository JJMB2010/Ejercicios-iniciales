#17.Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.
import math

peso=float(input("dime tu peso:"))
h=float(input("dime tu altura:"))

imc=peso/h**2
imc=round(imc, 2)

if (imc <= 25):
    print("Si pesas",peso,"kilos y mides",h,", tu IMC es:",imc)
else:
    print("Si pesas",peso,"kilos y mides",h,", tu IMC es:",imc,". Hay sobrepeso")