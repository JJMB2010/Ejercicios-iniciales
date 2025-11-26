# 61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es superior o igual a 40. 

n=int(input("Dime un número:"))
x=0
nn=n

while x in range(0,10):
    print(n)
    if n < 40:
        n=n+nn
    else:
        print("Fin del programa")
        x=11
    x=x+1