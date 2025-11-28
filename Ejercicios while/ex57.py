# 57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5 
import random

ns=random.randint(1,5)
n=int(input("Dime un número: "))

if n == ns:
    print("Número correcto")
else:
    print("Número incorrecto")