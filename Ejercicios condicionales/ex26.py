# 26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
import math

var1=str(input("dime una letra: "))

if (var1.isupper()):
    print("Es una letra mayuscula")
elif (var1.islower()):
    print("Es una letra minuscula")
else:
    print("Eso no es una letra")