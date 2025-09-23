# 15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math

r=float(input("dime el radio:"))
al=float(input("dime la altura:"))

area=2*math.pi*r*(r+al)
vol=math.pi*r**2*al

area=round(area, 2)
vol=round(vol, 2)

print("el area del cilindro es:",area)
print("el volument del cilindro es:",vol)