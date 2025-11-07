# 39. Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.

numb=int(input("Introduce la cantidad de números que deseas introducir: "))
p=0
c=0
n=0
for x in range(numb):
    a=float(input("Dime un número: "))

    if a > 0:
        p=p+1

    elif a == 0:
        c=c+1

    elif a < 0:
        n=n+1
print("La cantidad de números positivos es:",p)
print("La cantidad de números negativos es:",n)
print("La cantidad de ceros es:",c)