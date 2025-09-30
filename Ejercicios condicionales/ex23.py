# 23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
import math

nota=float(input("dime tu nota:"))

if (nota < 0):
    print("la nota no está entre 0 y 10")
    breakpoint
elif (nota > 10):
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