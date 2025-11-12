# 43. Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra.

a=str(input("Dime una palabra: "))
p=len(a)
for x in range(0,p):
    print("En la posición",x,"está la",a[x])