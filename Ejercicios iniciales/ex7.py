#calculadora
import math

var1=int(input("dime un numero: "))
var2=int(input("introduce otro numero: "))

var3=(var1/var2)
var3=round(var3, 2)

print("la suma de estos valores es ", var1+var2)
print("la resta de estos valores es ",var1-var2)
print("la multiplicación de estos valores es ",var1*var2)
print("la división de estos valores es ",var3)
print("la potencia del primer numero elevado al segundo es de ",var1**var2)
print("la división exacta de estos valores es ",var1//var2)