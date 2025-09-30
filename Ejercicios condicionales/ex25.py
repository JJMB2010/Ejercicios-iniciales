# 25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
import math

nota=float(input("dime tu nota:"))

if (nota < 0)or(nota > 10):
    print("la nota no está entre 0 y 10")
    breakpoint

else:
    if nota >= 5:
        if nota <= 6.5:
            print("has aprovado con un",nota,", has sacado un satisfactorio")
            breakpoint
        elif nota <= 8.5:
            print("has aprovado con un",nota,", has sacado un notable")
            breakpoint
        elif nota <= 10:
            print("has aprovado con un",nota,", has sacado un excelente")
            breakpoint

    else:
        print("has suspendido con un",nota,", has sacado un insuficiente")