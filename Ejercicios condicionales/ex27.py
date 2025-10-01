# 27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla
import math

var1=str(input("dime una letra/numero: "))

if (var1.isupper()):
    print("Es una letra mayuscula")
elif (var1.islower()):
    print("Es una letra minuscula")
elif (var1.isnumeric()):
    print("Esto es un número")
else:
    print("Eso es una cosa rara")