# 20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
import math

var1=float(input("dime un numero:"))
var2=float(input("dime otro numero:"))

if (var1 > 10)or(var1 < 0)or(var2 > 10)or(var2 < 0):
    print("Uno o los dos números están fuera de los límites establecidos")

elif (var1 == var2):
    print("el numero",var1,"es igual a",var2)
elif (var1 < var2):
    print("el numero",var1,"es menor que",var2)
elif (var1 > var2):
    print("el numero",var1,"es mayor que",var2)