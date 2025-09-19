# 10. Introduce por teclado dos números y muestre por pantalla la siguiente información:cociente, resto y si el dividendo es par o impar
import math

var1=float(input("introduce un numero:"))
var2=float(input("introduce otro numero:"))

print("el cociente es:",var1//var2)
print("el resto es:",var1%var2)

if var1%2==0:
    print("el dividendo es par")
else:
    print("el dividendo es impar")