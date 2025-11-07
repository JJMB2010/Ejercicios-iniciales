# 37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.

numb=int(input("Introduce el número de notas que deseas introducir: "))

for x in range(numb):
    a=float(input("Dime tu nota: "))

    if a >= 5:
        print("Asignatura aprovada")

    else:
        print("Asignatura suspendida")