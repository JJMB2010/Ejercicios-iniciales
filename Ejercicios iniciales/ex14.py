# 14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
import math

var1=float(input("dime el diámetro de un círculo: "))

per=math.pi*var1
per=round(per, 1)
ar=math.pi*(var1/2)**2
ar=round(ar, 1)
print("el perimetro es",per)
print("el apea del círculo es",ar)
