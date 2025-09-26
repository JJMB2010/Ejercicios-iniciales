# 19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales
import math

var1=float(input("dime un numero:"))
var2=float(input("dime otro numero:"))

if (var1 == var2):
    print("el numero",var1,"es igual a",var2)
elif (var1 < var2):
    print("el numero",var1,"es menor que",var2)
elif (var1 > var2):
    print("el numero",var1,"es mayor que",var2)