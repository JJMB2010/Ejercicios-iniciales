# 28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif
import math

var1=str(input("dime una letra/numero: "))

if (var1.isupper()):
    print("Es una letra mayuscula")
elif (var1.islower()):
    print("Es una letra minuscula")
elif (var1.isnumeric()):
    print("Esto es un número")
else:
    print("Eso es un símbolo")