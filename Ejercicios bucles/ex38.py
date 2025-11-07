# 38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10.

numb=int(input("Introduce el número de notas que deseas introducir: "))

for x in range(numb):
    a=float(input("Dime tu nota: "))
    if (a<0) or (a>10):
        print("Nota equivocada")
    else:
        if a >= 5:
           print("Asignatura aprovada")

        else:
            print("Asignatura suspendida")