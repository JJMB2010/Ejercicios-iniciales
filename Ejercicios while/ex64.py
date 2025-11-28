# 64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:

p=0
i=0
pos=0
neg=0
c=0
total=0

n=int(input("Dime un número: "))

while n != -99:
    if n%2 == 0:
        p=p+1
    else:
        i=i+1
    if n < 0:
        neg=neg+1
    else:
        pos=pos+1
    if n == 0:
        c=c+1
    total=total+n
    n=int(input("Dime un número: "))

print("RESUMEN")
print("Total de pares:",p)
print("Total de impares:",i)
print("Total de numeros positivos:",pos)
print("Total de numeros negativos:",neg)
print("Total de ceros:",c)
print("El total es:",total)