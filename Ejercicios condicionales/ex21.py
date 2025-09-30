# 21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math

a=float(input("dime un numero:"))
b=float(input("dime un numero:"))
c=float(input("dime un numero:"))

if a == 0:
    print("esto no es una ecuación de segundo grado")
    breakpoint

pa1=b**2-4*a*c

if pa1 <= 0:
    print("La raíz no puede ser un valor negativo")
    breakpoint

else:
    x1=((-b)+math.sqrt(pa1))/(2*a)
    x2=((-b)-math.sqrt(pa1))/(2*a)
    print("el valor de x1 es",x1)
    print("el valor de x2 es",x2)