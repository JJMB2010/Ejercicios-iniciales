import math

lado=int(input("dime el lado del triangulo: "))

a=(math.sqrt(3)/4)*(lado**2)
afin=round(a,2)

print("el area es:",afin)