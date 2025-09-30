# 22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
import math

nota=float(input("dime tu nota:"))

if (nota < 0)or(nota > 10):
    print("la nota no está entre 0 y 10")
    breakpoint

else:
    if nota >= 5:
        print("has aprovado con un",nota)
    else:
        print("has suspendido con un",nota)