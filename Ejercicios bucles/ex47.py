# 47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b la secuencia en descenso.

a=int(input("Dime un número: "))
b=int(input("Dime otro número: "))

if a>b:
    f=a
    for x in range(b,a):
        print(f, end="-")
        f=f-1
    print(b)
if b>a:
    f=a
    for x in range(a,b):
        print(f, end="-")
        f=f+1
    print(b)