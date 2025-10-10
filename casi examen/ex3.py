import math

r=float(input("radio = "))
h=float(input("altura = "))
si=input("Formato:")

fin=math.pi*(r**2)*h

if si in "mayúscula":
    fra=(str.upper("el volumen del cilindro es:"))
    print(fra,fin)
else:
    print("el volumen del cilindro es:",fin)