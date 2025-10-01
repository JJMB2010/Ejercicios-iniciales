# 30. Realiza un programa que controle si la longitud de una frase introducida por teclado es igual, menor o mayor de 11 caracteres. Utiliza elif
import math

si=str(input("Dime una frase: "))

num=len(si)

if num == 11:
    print("El numero de caracteres es igual a 11")
elif num < 11:
    print("El numero de caracteres es menor que 11")
elif num > 11:
    print("El numero de caracteres es mayor a 11")